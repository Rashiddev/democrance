# Democrance
A test project to create customer and their policies.

## Project instructions
Please run following commands in the given order to execute and test this project:<br>
1. pip install -r requirements.txt (Please makesure you're inside the project and pip3 is installed in the system)
2. python manage.py test (Test the project)
3. python manage.py runserver 8000 (Please make sure that you already have PYTHON 3 installed on your system)

## Testing
Download POSTman and import sample APIs from the POSTman link given below:
Once the server is running, you can execute sample APIs in POSTman.

<b>Postman link:</b><br>
https://www.getpostman.com/collections/930e1a241530acb61736
<br><br>
In case if you don't have POSTman, you can use following samples to test APIs in the browser using Django's browsabe APIs.

<h5>Samples:</h5>
<hr>
<p><b>Customer Create API:</b></p>
URL: <a href="http://127.0.0.1:8000/api/v1/create_customer/">http://127.0.0.1:8000/api/v1/create_customer/</a>
<br>
Method: POST
<br>
Sample data:<br>
{
    "first_name": "Rashid",
    "last_name": "Mahmood",
    "dob": "1991-11-04"
}
<br>
<hr>
<p><b>Policy Create API:</b></p>
URL: <a href="http://127.0.0.1:8000/api/v1/create_policy/">http://127.0.0.1:8000/api/v1/create_policy/</a>
<br>
Method: POST<br>
Sample data:<br>
{
	"type": "personal-accident",
	"premium": 200,
	"cover": 200000,
	"customer": 1
}
<br><br>
<p>Note: Please make sure that atleast one customer is created before creating policy. Replace "customer" with existing customer's id.</p>
<hr>
<p><b>Customer List API:</b></p>
URL: <a href="http://127.0.0.1:8000/api/v1/customers/">http://127.0.0.1:8000/api/v1/customers/</a>
<br>Method: GET<br>

## Accessing Admin
<p>Using following details to login to admin panel:</p><br>
URL: <a href="http://127.0.0.1:8000/admin/login/?next=/admin/">http://127.0.0.1:8000/admin/login/?next=/admin/</a>
<br>Username: admin<br>
Password: test123#

## Other Notes
For testing purpose, I've kept all the APIs open, it's mean you don't need any authentication to access those APIs.

