from transformers import pipeline

# ===== Step 1: Set up the local language model =====
model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=100
)

# ===== Step 2: Define our job database =====
# In ideal world this will be a DB
SKILLS = {
    "Python": ["software engineer", "data scientist"],
    "SQL": ["database engineer", "data scientist"],
    "Maths": ["data scientist"],
    "JavaScript": ["software engineer"],
    "Statistics": ["data scientist"],
    "Communication": ["project manager"],
    "Leadership": ["project manager"],
    "Agile": ["project manager"]
}

# ===== Step 3: Create skill extraction tool that uses llm =====
def extract_skills(profile: str) -> list:
    print("🤖 Tool: skill extraction")
    prompt = f"""Extract technical and soft skills from this profile. Return only a comma-separated list of skills, no other text.

Profile: {profile}

Skills:"""
    
    response = model(prompt)[0]['generated_text']
    skills = [skill.strip() for skill in response.split(',')]
    return skills

# ===== Step 4: Create a simple python function as tool =====
def find_job_matches(profile: str) -> str:
    print("🤖 Tool: job matching")
    # First extract skills using LLM
    skills = extract_skills(profile)
    
    # Find jobs that match the extracted skills
    matching_jobs = {}
    for skill in skills:
        for req_skill, jobs in SKILLS.items():
            if req_skill.lower() in skill.lower():
                for job in jobs:
                    if job not in matching_jobs:
                        matching_jobs[job] = []
                    matching_jobs[job].append(req_skill)
    
    if not matching_jobs:
        return "No matching jobs found."
    
    # Return all matching jobs
    result = []
    for job, matching_skills in matching_jobs.items():
        result.append(f"Job: {job} (Matching Skills: {', '.join(matching_skills)})")
    return "\n".join(result)

# ===== Step 5: Create career advice agent =====
def get_career_advice(profile: str) -> str:
    print("🤖 Tool: career advice")
    matches = find_job_matches(profile)
    prompt = f"""Based on the profile and job matches, recommend the most suitable job. Consider:
1. Number of matching skills
2. Relevance of skills to the job
3. Career growth potential

Profile: {profile}

Available Matches:
{matches}

Which job is the best match for this profile? """
    
    advice = model(prompt)[0]['generated_text']
    return f"{matches}\nCareer Advice:: {advice}"

# ===== Main program =====
def main():
    print("Starting Career Advisor")
    print("="*50)
    
    profile = "I know Python and love maths"
    print(f"Profile: {profile}")
    print("="*50)

    try:
        result = get_career_advice(profile)
        print("\nResults:")
        print("="*50)
        print(result)
        print("="*50)
    except Exception as e:
        print(f"Error: {e}")

# ===== Run the program =====
if __name__ == "__main__":
    main()