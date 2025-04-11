# Coffee Review Site

## How to set up website for access: 
1.	Download the files from GitHub
2.	Go to Linux command prompt terminal (use Ubuntu)
    -	Install Python 
      - Enter “sudo apt install python3”
    - Install Django 
      - Enter “pip install django”
    - Change directory to where the coffee site was downloaded 
      - “cd [directory]/coffee_site/”
    - Then enter, “source cs_env/bin/activate” 
        - Activates virtual environment 
    - Then enter “python manage.py runserver “
      - Starts the server 
3.	Go to browser and in the search bar, type “localhost:8000”
4.	Utilize website

## AI Use: ChatGPT 
Prompts: 
1.	I am unable to create a new account manually after adding in the Google OAuth2.0. What could be the possible error?
    - This changed the views.py in the user folder & fixed the error of people not being able to manually create an account
2.	How would I create a page for each user where you can see all of the reviews they have submitted? 
    - This changed the urls.py as well as the functionality of being able to click on a user and see all of their reviews. 
3.	How would I add a search bar to my coffee site so you can find the coffee bean to review that you want? 
    - This changed views.py
    - It added a search function to the main reviews page

