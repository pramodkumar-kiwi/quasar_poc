# Gondola Web and API


### Prerequisite:

    * Python 3.10
    * Django 4.2
    

### System Setup:

1. Environment setup:

    * Install pip and virtualenv:
        - sudo apt-get install python3-pip
        - pip install --upgrade pip
        - sudo pip3 install virtualenv or sudo pip install virtualenv

          * Create virtual environment:
              - virtualenv venv

              OPTIONAL:- In case finding difficulty in creating virtual environment by
                        above command , you can use the following commands too.

                *  Create virtualenv using Python3:-
                 - virtualenv -p python3.10 venv
    * Activate environment:
      - source venv/bin/activate

    * Clone project:
          ```
            git clone https://github.com/KiwiTechLLC/GondolaLife-Backend.git
          ```

    * Checkout to branch
        - git checkout "branch_name"

    * Install the requirements(according to server) by using command:
        - cd GondolaLife-Backend/
        * for local system follow below command
        ```
          pip3 install -r requirements.txt
        ```

4.Run servers:
    ```
     $ python manage.py runserver
    ```
# quasar_poc
