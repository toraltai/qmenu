from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from .users import User



class Company(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(50)
    user = fields.ForeignKeyField(User)


GetCompany = pydantic_model_creator(Company, name='Company')
CreateCompany = pydantic_model_creator(Company, name='CompanyIn', exclude_readonly=True)