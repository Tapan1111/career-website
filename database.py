from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://upkwmpqrrkcolnu0:myNoz7MsaMnnAHIUh82G@bfvcdyjv9kinltyhh9co-mysql.services.clever-cloud.com/bfvcdyjv9kinltyhh9co"
)

def get_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs_list = []
    for job in result.all():
      jobs_list.append(job._asdict())
    return jobs_list

def get_job_by_id(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT * FROM jobs 
                WHERE id = :job_id
            """),
            {"job_id": id}
        )
        job = result.fetchone()
        return job._asdict() if job else None
    
def add_application_to_db(job_id, application):
    with engine.connect() as conn:
        # SQL query with parameter binding
        query = text("""
            INSERT INTO applications (
                job_id,
                full_name,
                email, 
                linkedin_url,
                resume_url
            ) VALUES (
                :job_id,
                :full_name,
                :email,
                :linkedin_url,
                :resume_url
            )
        """)
        
        # Execute with parameters
        conn.execute(query, {
            'job_id': job_id,
            'full_name': application['name'],
            'email': application['email'],
            'linkedin_url': application.get('linkedin', ''),
            'resume_url': application.get('resume', '')
        })
        
        # Commit transaction
        conn.commit()
      

      
