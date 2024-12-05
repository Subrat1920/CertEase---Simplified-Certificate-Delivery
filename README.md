# CertEase---Simplified-Certificate-Delivery
CertEase is a web application designed to streamline the process of certificate distribution. With CertEase, administrators can upload a CSV file containing student details, and the system will generate and deliver certificates to the students' email addresses effortlessly.

## Key Features
    1. Bulk Certificate Generation: Generate personalized certificates for all students listed in a CSV file.
    2. Automated Email Delivery: Send certificates directly to students' email addresses.
    3. Easy File Upload: Upload CSV files to the platform with student details for processing.
    4. Database Integration: Efficiently manage student data using SQLite.
    5. Responsive Design: Ensures seamless use on various devices with Bootstrap-based UI.

## Technologies Used
    1. Backend: Python, Django, SQLite.
    2. Frontend: HTML, CSS, JavaScript, Bootstrap.
    3. Email Integration: Django's email framework for automated certificate delivery.


## How to Use
    1. Clone the repository to your local machine.
        git clone git@github.com:Subrat1920/CertEase-Simplified-Certificate-Delivery.git
    2. Activate Virtual Environemnt :
            venv\Scripts\activate
    3. Install the required packages : 
            pip install -r requirements.txt
    4. Check for the migrations : 
            python manage.py showmigrations
    5.  Migrate the dependencies : 
            python manage.py migrate
    6. Make migrations : 
        python manage.py makemigrations
    7. Make a super-user for admin panel controll : 
        python manage.py createsuperuser
    8. Give the required option to the terminal
    9. Run the server : 
        python manage.py runserver
    10. Upload CSV and Send Certificates

### CertEase makes the task of distributing certificates efficient and hassle-free for educational institutions, training centers, and event organizers.