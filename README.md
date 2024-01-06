# Albanero_assignment
1. Clone: git@gitlab.com:hornet4054609/ml-engine.git from main branch
    2. Install Python3:
        ### make sure the system's repositories are updated, 
            if not use : sudo apt update

        sudo apt install python3.8

    3. After installing we can check the version using 'python3.8 --version'
    4. Create a virtual environment:
        i. Create the Venv:  python3 -m venv albanerovenv
        ii. Activate the Venv: source albanerovenv/bin/activate

    5. After activating the venv go to 'Albanero_assignment' folder and run 
        pip install -r requirements.txt
    6. Setup environment variables:
        export FLASK_APP=app.py
        export FLASK_ENV=development
    7. Run the query_to_run.sql file inside in DB folder