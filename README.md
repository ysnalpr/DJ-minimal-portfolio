# DJ-minimal-portfolio

A minimal porfolio with Django framework.

## How to run

To run in development mode; Just use steps below:

1. Install `python3`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/ysnalpr/DJ-minimal-portfolio.git`.
3. Make development environment ready using commands below;

  ```bash
  git clone https://github.com/ysnalpr/DJ-minimal-portfolio.git && cd DJ-minimal-portfolio
  virtualenv -p python3 env  # Create virtualenv named env
  source env/bin/activate
  pip install -r requirements.txt
  python3 manage.py migrate  # Create database tables
  ```

4. Run using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your local version.

## Run On Windows

If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python2`, `pip`, `virtualenv` 
2. Clone the project using:  `https://github.com/ysnalpr/DJ-minimal-portfolio.git`.
3. Make Environment Ready Like This:
  ``` Command Prompt
  cd DJ-minimal-portfolio
  virutalenv env
  env\Scripts\activate # Activate The Virutal Environment
  pip install -r requirements.txt
  python manage.py migrate # Create Database Tables
  ```
4. Run using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your local version.