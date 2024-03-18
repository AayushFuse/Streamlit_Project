from pydantic import BaseModel


class EmployeeBase(BaseModel):
    ename: str
    job: str
    deptno: int


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    empno: int

    class Config:
        orm_mode = True


class DepartmentBase(BaseModel):
    dname: str
    loc: str


class DepartmentCreate(DepartmentBase):
    pass


class Department(DepartmentBase):
    deptno: int

    class Config:
        orm_mode = True


class DetailedResponse(BaseModel):
    empno: int
    ename: str
    deptno: int
    dname: str

    class Config:
        orm_mode = True
