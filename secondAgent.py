from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

# Initialize the LLM
try:
    hf_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7
    )
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Job database with required skills
JOBS = {
    "software engineer": {
        "titles": ["Junior Software Engineer", "Full Stack Developer"],
        "skills": ["python", "javascript", "sql", "git"]
    },
    "data scientist": {
        "titles": ["Data Analyst", "Machine Learning Engineer"],
        "skills": ["python", "sql", "statistics", "machine learning"]
    },
    "project manager": {
        "titles": ["Agile Project Manager", "Product Owner"],
        "skills": ["agile", "scrum", "communication", "leadership"]
    }
}

def analyze_profile(profile: str) -> str:
    """Analyze profile and return job recommendations."""
    # Extract skills
    profile_lower = profile.lower()
    found_skills = []
    all_skills = set()
    for job_data in JOBS.values():
        all_skills.update(job_data["skills"])
    
    for skill in all_skills:
        if skill in profile_lower:
            found_skills.append(skill)
    
    # Find matching jobs
    recommendations = []
    for role, data in JOBS.items():
        required_skills = set(data["skills"])
        matching_skills = required_skills.intersection(set(found_skills))
        
        if matching_skills:
            match_percentage = len(matching_skills) / len(required_skills) * 100
            recommendations.append({
                "role": role,
                "titles": data["titles"],
                "match_percentage": round(match_percentage, 2),
                "matching_skills": list(matching_skills),
                "missing_skills": list(required_skills - set(found_skills))
            })
    
    # Format results
    if not recommendations:
        return "No matching jobs found."
    
    result = "Job Recommendations:\n\n"
    for rec in recommendations:
        result += f"Role: {rec['role']}\n"
        result += f"Suggested Titles: {', '.join(rec['titles'])}\n"
        result += f"Match: {rec['match_percentage']}%\n"
        result += f"Matching Skills: {', '.join(rec['matching_skills'])}\n"
        result += f"Missing Skills: {', '.join(rec['missing_skills'])}\n\n"
    
    return result

def get_recommendations(profile: str) -> str:
    """Get job recommendations with LLM analysis."""
    # First get the basic recommendations
    recommendations = analyze_profile(profile)
    
    # Then use the LLM to analyze and explain the recommendations
    prompt = f"""Given this profile and job recommendations, provide a brief analysis:

Profile: {profile}

Recommendations:
{recommendations}

Please provide a brief analysis of the fit and suggestions for improvement."""
    
    try:
        analysis = llm.invoke(prompt)
        return f"{recommendations}\n\nAnalysis:\n{analysis}"
    except Exception as e:
        print(f"Error getting LLM analysis: {e}")
        return recommendations

# Example profile
profile_summary = "I am a software engineer with 3 years of experience in Python and JavaScript. I also know SQL and Git."

# Get recommendations
try:
    if not profile_summary.strip():
        print("Error: Profile summary cannot be empty.")
    else:
        result = get_recommendations(profile_summary)
        print("\nResults:")
        print("=" * 50)
        print(result)
        print("=" * 50)
except Exception as e:
    print(f"Error: {e}")