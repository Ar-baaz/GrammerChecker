
# Spell Checker

Spell Checker is a simple web application that checks the spelling of a given text and suggests corrections for any spelling mistakes found.

## Installation

To run this application, you must have Python 3.6 or later installed on your machine. You can install Python from the official website: https://www.python.org/downloads/

After installing Python, you can clone this repository to your local machine using Git:

```bash
git clone https://github.com/Ar-baaz/GrammerChecker
```

Next, navigate to the project directory:

```bash
cd GrammerChecker
```

Create a virtual environment for the project and activate it:

```bash
python3 -m venv venv
source venv/bin/activate   # on Linux/MacOS
venv\Scripts\activate     # on Windows
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, simply execute the following command in your terminal or command prompt:

```bash
streamlit run GrammerChecker.py
```

This will start the application on a local web server. You can access the application by opening a web browser and navigating to http://localhost:8501/

Enter some text in the input box and click the "Check Spelling" button to check for spelling mistakes. Any spelling mistakes found will be highlighted in bold and their suggested corrections will be displayed next to them.

## Contributing

If you find any issues or have any suggestions for improving this application, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
