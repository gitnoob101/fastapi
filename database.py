import sqlalchemy
from sqlalchemy import create_engine, text

# Database URL
DATABASE_URL = "mysql+pymysql://root:bill123%40A@localhost:3306/fastapi_db"
engine = create_engine(DATABASE_URL)

def search(name: str):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM students WHERE students.name = :name"),
            {"name": name}
        ).fetchall()

        if not result:
            print("not present in the database")
        else:
            student=[]
            for row in result:
                student.append({
                    "student_id":row.id,
                    "student_name":row.name,
                    "stundent_class":row.clas,

                })
        return student


def add(candidate):
    with engine.begin() as conn:  
        conn.execute(
            text("INSERT INTO students (id, name, clas, pos) VALUES (:id, :name, :clas, :pos)"),
            {
                "id": candidate.id,
                "name": candidate.name,
                "clas": candidate.clas,
                "pos": candidate.pos
            }
        )
        print("New student added to the database")
