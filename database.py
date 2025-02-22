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
