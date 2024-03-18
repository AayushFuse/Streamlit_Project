from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Department(Base):
    __tablename__ = "departments"

    deptno = Column(Integer, primary_key=True, index=True)
    dname = Column(String)
    loc = Column(String)

    employee = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"

    empno = Column(Integer, primary_key=True, index=True)
    ename = Column(String)
    job = Column(String)
    deptno = Column(Integer, ForeignKey("departments.deptno"))

    department = relationship("Department", back_populates="employee")
