This application is written in Django framework

Installing Instructions:

1 Make sure you have installed Python
2 In CMD navigate to the path in this folder ./customerservice/customerservice/ (make sure that you are in folder where is the manage.py file)
3 Run following commands:   1 pipenv install django
                            2 pipenv shell
                            3 python manage.py runserver
4 This will start a development server probably at: http://127.0.0.1:8000/, you willl get info about ip address.
5 Open browser and type in address bar: http://127.0.0.1:8000/callbackform/ 

For backend/administration page is used standard Django admin functionlity.
Path for administration page is: http://127.0.0.1:8000/admin/callbackform/supportrequest/ 
(user: admin pass: admin). Password is changeable.
In administration page, administrators can see non-archived tickets by default, but they can change to see and archived.
Tickets are sortable by DateTime fields by clicking on these columns captions.


