import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import User
from students.models import Student
from tasks.models import Task
from datetime import date, timedelta

def seed():
    # Create Admin
    admin, created = User.objects.get_or_create(
        username='admin',
        defaults={'email': 'admin@example.com', 'role': 'admin', 'is_staff': True, 'is_superuser': True}
    )
    if created:
        admin.set_password('admin123')
        admin.save()
        print("Admin created: admin/admin123")

    # Create Student User
    student_user, created = User.objects.get_or_create(
        username='john_doe',
        defaults={'email': 'john@example.com', 'role': 'student'}
    )
    if created:
        student_user.set_password('student123')
        student_user.save()
        print("Student User created: john_doe/student123")

        # Create Student Profile
        Student.objects.create(
            user=student_user,
            student_id='STU001',
            name='John Doe',
            email='john@example.com',
            department='Computer Science',
            phone='1234567890',
            address='123 Main St, City'
        )
        print("Student Profile created for John Doe")

    # Create Sample Tasks
    Task.objects.create(user=student_user, title='Submit Assignment', description='Finish Django project', due_date=date.today() + timedelta(days=2))
    Task.objects.create(user=student_user, title='Buy Groceries', description='Milk, Eggs, Bread', is_completed=True)
    print("Sample tasks created")

if __name__ == '__main__':
    seed()
