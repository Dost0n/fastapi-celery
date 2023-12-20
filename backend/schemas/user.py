from pydantic import BaseModel
from typing import Optional



class SignUpModel(BaseModel):
    id         :Optional[str]
    username   :Optional[str]
    password   :Optional[str]
    email      :Optional[str]
    first_name :Optional[str]
    is_staff   :Optional[bool]
    gender     :Optional[str]
    
    class Config:
        orm_mode = True
        schema_extra = {
            'example' :{
                'username'   :'Doston',
                'password'   :'123',
                'email'      :'example@gmail.com',
                'first_name' :'Doston',
                'is_staff'   :True,
                'gender'     :'M',
            }
        }