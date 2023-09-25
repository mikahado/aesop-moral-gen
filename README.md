**Aesop's Moral Generator** 

Read the famous children stories, reflect on the morals, and see if the AI gets it, too. 

*For ages 5 to 500.*

This application uses the ChatGPT API and [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework.

## Installation and Setup

1. Make sure you have Python installed. If not, download it [here](https://www.python.org/downloads/).

2. Clone the repository for this project.

```bash
$ git clone <repository-url>
```
3. Navigate to the project directory:

```bash
$ cd aesop-moral-generator
```
4. Create a new virtual environment for this project:

```bash
$ python -m venv venv
$ . venv/bin/activate
```
5. Install the required dependencies:

```bash
$ pip install -r requirements.txt
```
6. Make a copy of the example environment variables file:

```bash
$ cp .env.example .env
```
7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

```bash
$ flask run
```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!  --> Enjoy using Aesop's Moral Generator!


<!-- # Quickstart 

This is Aesop's Moral Generator app, an simplified version built off the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) 

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)!  -->
