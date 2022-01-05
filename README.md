# Word Counter App

Welcome to Word Counter, an app developed for the Voxy Challenge.

- The application was developed according to the [accept criteria below](#acceptance-criteria).
- To start the application, follow the [instructions](#initial-setup).

## Initial setup

### Download Python

First of all you need to have Python 3.8^ installed in your machine. You can download it in the [official Python website](https://www.python.org/downloads/). Follow up [official docs](https://wiki.python.org/moin/BeginnersGuide/Download) for installation.

### Clone this repository

Go to any folder in your computer where you want to install this project. Next, clone this repository using:

``` shell
git clone https://github.com/dversoza/voxy-challenge.git
```

### Create a virtual environment for your app

Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects.

In order to achieve that, access the recently created folder, using:

``` shell
cd voxy-challenge
```

Then run the following script to create a virtual environment:

``` shell
python -m venv venv
```

Activate the virtual environment using:

#### For Linux / MacOS users

``` shell
source ./venv/bin/activate
```

#### For windows users

``` shell
/venv/scripts/activate
```

### Install project requirements

With your active virtual environment, run:

``` shell
pip install -r requirements.txt
```

Wait for the project dependencies to install.

## Running the app

To run the app, access your project folder and run:

``` shell
python manage.py runserver
```

This project does not use any database to persist data (only has a default sqlite to make sure the app works), but if you want to get rid of CLI errors when running the app, stop the app by closing the terminal and run: `python manage.py migrate`, then run the app again.

## Acceptance Criteria

As a user when I view the application then I see a form containing a text box to enter a body of text and when I submit the form with some text then I see a result containing the number of words in the text box and when I submit the form with an empty text then I see a form error telling me that some text input is required.

As an engineer when I look at your project then I should understand how to install and run it.
