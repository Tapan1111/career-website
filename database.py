from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://upkwmpqrrkcolnu0:myNoz7MsaMnnAHIUh82G@bfvcdyjv9kinltyhh9co-mysql.services.clever-cloud.com/bfvcdyjv9kinltyhh9co"
)

with engine.connect() as conn:
    result = conn.execute(text("select * from bfvcdyjv9kinltyhh9co.jobs"))
    print(result.all())
