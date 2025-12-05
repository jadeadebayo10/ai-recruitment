from app.rank import rank_resumes_for_job

job_desc = input("Paste the job description here:\n\n")

# 2. Get the top resume (full text)
df = rank_resumes_for_job(job_desc, top_k=1)  
best_resume = df.iloc[0]["resume_text"]

# 3. Show the result
print("\nBEST MATCHED RESUME:\n")
print(best_resume)