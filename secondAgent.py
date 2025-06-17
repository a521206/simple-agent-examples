"""
A simple career advisor agent that matches skills to jobs and provides career advice.
This is a beginner-friendly example that shows how to:
1. Use a language model
2. Create a simple matching system
3. Combine AI with basic programming
"""

from transformers import pipeline

# ===== Step 1: Set up the local language model =====
model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=100
)

# ===== Step 2: Define our job database =====
# In ideal world this will either be a DB or web search
JOBS = {
    "software engineer": [
        "Python",
        "JavaScript",
        "SQL"
    ],
    "data scientist": [
        "Python",
        "SQL",
        "Statistics"
    ],
    "project manager": [
        "Communication",
        "Leadership",
        "Agile"
    ]
}

# ===== Step 2: Create a function =====
# In ideal world this could be an llm
def find_job_matches(profile: str) -> str:
    print("🤖 Tool: job matching")
    profile = profile.lower()
    
    for job, skills in JOBS.items():
        matching_skills = [
            skill for skill in skills 
            if skill.lower() in profile
        ]
        if matching_skills:
            return f"Job: {job} (Matching Skills: {', '.join(matching_skills)})"
    
    return "No matching jobs found."

# ===== Step 3: Create second function =====
def get_career_advice(profile: str) -> str:
    print("🤖 Tool: career advice")
    matches = find_job_matches(profile)
    prompt = f"""Given this profile and job matches, provide brief career advice:
    Profile: {profile}
    Matches: {matches}
    What career advice would you give this person?"""
    
    advice = model(prompt)[0]['generated_text']
    return f"{matches}\nCareer Advice:: {advice}"

# ===== Main program =====
def main():
    print("Starting Career Advisor")
    print("="*50)
    
    profile = "I know Python and SQL, and I'm good at maths."
    print(f"Profile: {profile}")
    
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