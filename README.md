# CodeTable
A web application to compile and run code online on browser. 

## About this project

Compile and run code. You just need to host the project on your machine and you are good to go. 

This project uses the HackerEarth Compile and run API for code compilation. For more details about the API, visit the link  https://www.hackerearth.com/docs/api/developers/code/v3/

## Instructions to setup the project on local machine

Setting up the project on your local machine is very easy. Just three step installation after cloning the repository. 

1. Create virtual environment by using following command: 
    
        virtualenv env

2. If you dont have virtualenv the install using the command 
    
        pip install virtualenv
    
3. Run the virtaulenv by 

        source env/bin/activate
    
4. Install the dependencies using the command: 

        pip install -r requirements.txt
    
5. Run migrations using the command: 

        python manage.py migrate
    
6. Enter the HackerEarth API Key( HE_CLIENT_SECRET) in settings.py file.

7. Run the development server: 

        python manage.py runserver

Finally open http://127.0.0.1:8000 to see the magic into action. 

If you want to contribute to this project, then simply:

    * Fork the repository
    * Clone on your machine 
    * Make changes
    * Send Pull requests
