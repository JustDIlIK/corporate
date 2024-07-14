from sqladmin import ModelView

from app.achievement.model import Achievement
from app.calculation.model import Calculation
from app.client.model import Client
from app.company.model import Company
from app.consideration.model import Consideration
from app.direction.model import Direction
from app.employee.model import Employee
from app.feature.model import Feature
from app.feedback.model import Feedback
from app.lang.model import Lang
from app.link.model import Link
from app.project.model import Project, ProjectImage
from app.service.model import Service
from app.statistic.model import Statistic
from app.technology.model import Technology
from app.user.models import User
from app.visitor.model import Visitor


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]
    column_details_exclude_list = [User.password]
    can_delete = False
    icon = "fa-solid fa-user"


class AchievementsAdmin(ModelView, model=Achievement):
    column_list = [c.name for c in Achievement.__table__.c]
    icon = "fa-solid fa-trophy"

class CalculationsAdmin(ModelView, model=Calculation):
    column_list = [c.name for c in Calculation.__table__.c]
    icon = "fa-solid fa-calculator"


class ClientsAdmin(ModelView, model=Client):
    column_list = [c.name for c in Client.__table__.c]
    icon = "fa-solid fa-users"


class CompaniesAdmin(ModelView, model=Company):
    column_list = [c.name for c in Company.__table__.c]
    icon = "fa-solid fa-building"
    name_plural = "Companies"


class DirectionsAdmin(ModelView, model=Direction):
    column_list = [c.name for c in Direction.__table__.c]
    icon = "fa-solid fa-compass"


class EmployeesAdmin(ModelView, model=Employee):
    column_list = [c.name for c in Employee.__table__.c]
    icon = "fa-solid fa-user-tie"


class FeaturesAdmin(ModelView, model=Feature):
    column_list = [c.name for c in Feature.__table__.c]
    icon = "fa-solid fa-star"


class FeedbacksAdmin(ModelView, model=Feedback):
    column_list = [c.name for c in Feedback.__table__.c]
    icon = "fa-solid fa-comment"


class LangsAdmin(ModelView, model=Lang):
    column_list = [c.name for c in Lang.__table__.c]
    icon = "fa-solid fa-language"


class LinksAdmin(ModelView, model=Link):
    column_list = [c.name for c in Link.__table__.c]
    icon = "fa-solid fa-link"


class ProjectsAdmin(ModelView, model=Project):
    column_list = [c.name for c in Project.__table__.c]
    icon = "fa-solid fa-diagram-project"


class ProjectImageAdmin(ModelView, model=ProjectImage):
    column_list = [c.name for c in ProjectImage.__table__.c]
    icon = "fa-solid fa-diagram-project"


class ServicesAdmin(ModelView, model=Service):
    column_list = [c.name for c in Service.__table__.c]
    icon = "fa-solid fa-person-chalkboard"


class TechnologiesAdmin(ModelView, model=Technology):
    column_list = [c.name for c in Technology.__table__.c]
    icon = "fa-solid fa-code"
    name_plural = "Technologies"


class VisitorAdmin(ModelView, model=Visitor):
    column_list = [c.name for c in Visitor.__table__.c]
    icon = "fa-solid fa-user-group"


class StatisticAdmin(ModelView, model=Statistic):
    column_list = [c.name for c in Statistic.__table__.c]
    icon = "fa-solid fa-users-rectangle"


class ConsiderationAdmin(ModelView, model=Consideration):
    column_list = [c.name for c in Consideration.__table__.c]
    icon = "fa-solid fa-file-signature"

