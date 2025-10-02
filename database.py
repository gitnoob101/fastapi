import sqlalchemy
from sqlalchemy import create_engine, text,MetaData,Table,insert
from sqlalchemy.orm import sessionmaker


# Database URL
DATABASE_URL = "mysql+pymysql://root:bill123%40A@localhost:3306/fastapi_db"
engine = create_engine(DATABASE_URL)
session_local=sessionmaker(bind=engine,autoflush=False)
metadata=MetaData()
students=Table("students",metadata,autoload_with=engine)#reflection of the actual table in the db

def search(name:str):
    session=session_local()
    try:
        result=session.query(students).filter(students.c.name==name).all()
        return result
    finally:
        session.close()
def add(candidata):
    # session=session_local()
    # try:
    #     session.add(candidata)
    #     session.commit()
    #     session.refresh(candidata)
    #     return [f"candidate is added:{candidata.id}"]
    # finally:
    #     session.close() will not work beause using reflected table
    with engine.begin() as conn:
        conn.execute(insert(students).values(**candidata.dict()))
    return {"process is completed"}



# def search(name: str):
#     with engine.connect() as conn:
#         result = conn.execute(
#             text("SELECT * FROM students WHERE students.name = :name"),
#             {"name": name}
#         ).fetchall()

#         if not result:
#             return [{"result":"not found bro"}]
#         else:
#             student=[]
#             for row in result:
#                 student.append({
#                     "student_id":row.id,
#                     "student_name":row.name,
#                     "stundent_class":row.clas,

#                 })
#         return student


# def add(candidate):
#     with engine.begin() as conn:  
#         conn.execute(
#             text("INSERT INTO students ( name, roll,clas, pos) VALUES ( :name,:roll, :clas, :pos)"),
#             {
                
#                 "name": candidate.name,
#                 "roll":candidate.roll,
#                 "clas": candidate.clas,
#                 "pos": candidate.pos
#             }
#         )
#         print("New student added to the database")
# with engine.begin() as conn:  
#     result=conn.execute(text('desc students')).fetchall()
#     print(result)
l=search('Renu')
print(l)