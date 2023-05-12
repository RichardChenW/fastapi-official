from typing import Optional
from sqlmodel import create_engine, Field, SQLModel,Session,select
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from sqlalchemy import Column
import pandas as pd

# table=True 表示这个类是一个数据库表
class Customer_info(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(default=None, max_length=255)
    age: Optional[int] = Field(default=None)

# 数据库连接 用户名、密码、主机、端口、库名
MYSQL_URL = r'mysql://root:882525@localhost:3306/competition'
# echo=True 打印日志
engine = create_engine(MYSQL_URL, echo=True)
# 这行代码会创建所有继承了SQLModel的表
SQLModel.metadata.create_all(engine)

# 创建一行
# def create_test_record():
#     user_1 = Customer_info(name="jamesss", age=20)

#     # 创建会话
#     session = Session(engine)
#     # 添加更改
#     session.add(user_1)
#     # 提交更改
#     session.commit()
#     session.refresh(user_1)
#     # 关闭会话
#     session.close()

# def read_data():
#     with Session(engine) as session:
#         statement = select(Customer_info.name)
#         results = session.exec(statement)
#         print(results)

def query_data():
    with Session(engine) as session:
        res = session.exec(select(Customer_info.user_id,Customer_info.name,Customer_info.age))
        print(Customer_info.__annotations__.keys())
        print(pd.DataFrame(res.all(),columns=Customer_info.__annotations__.keys()))

if __name__ == '__main__':
    query_data()
