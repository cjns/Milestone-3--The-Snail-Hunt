# Testing

The following tools were used for testing:

- HTML: [W3C Markup Validator](https://validator.w3.org/)
- CSS: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- Accessibility: [WAVE (Web Accessibility Evaluation Tool)](https://wave.webaim.org/)
- Performance: [Lighthouse (Within Chrome Developer Tools)](https://developer.chrome.com/docs/lighthouse/overview/)
- Python Syntax: [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
- JS Syntax: [ESLint](https://eslint.org/)

## HTML, Accessibility, & Performance
|Page|HTML|Lighthouse Mobile|Lighthouse Desktop|
|-|-|-|-|
|Home||||
|Log in||||
|Register||||
|Surveys||||
|Add Survey||||
|Edit Survey||||

## Accessibility
|Page|Wave Validation|
|-|-|
|Home||
|Login||
|Register||
|Surveys||
|Add Survey||
|Edit Survey||

## CSS
|File|Validation|
|-|-|
|style.css|-|

## JavaScript
|File|Validation|
|-|-|
|script.js|-|

## Python
|File|Valid|
|-|-|
|forms.py|-|
|models.py|-|
|routes.py|-|
|run.py|-|
|__init__.py|-|

## Nav & Footer Links
|Link|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|Home|-|-|-|-|
|Login|-|-|-|-|
|Register|-|-|-|-|
|Surveys|-|-|-|-|
|Add Survey|-|-|-|-|
|Email for support|-|-|-|-|

## Home page
|Feature|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|-|
|Link: How to hunt banded snails|-|-|-|-|-|

## Log in (login.html)
## Register (register.html)
## Surveys (surveys.html)
## Add Survey (add_survey.html)
- Date
- Time
- Location
- Habitat
- Name of recorder
- Brown lipped snail, 0 bands
- Brown lipped snail, 1 band
- Brown lipped snail, many bands
- White lipped snail, 0 bands
- White lipped snail, 1 band
- White lipped snail, many bands

## Bugs
### 1
#### Description:
Logging in part 1
#### Error:
Exception: Install 'email_validator' for email validation support
#### Fix
pip install email_validator
or
pip install --user email_validator

### 2
#### Description
Logging in part 2
#### Error:
NoForeignKeysError
#### Fix:
Set up a foreign key relationship between the User and Survey

### 3
#### Description
Logging in after registering a user.
#### Error:
NotImplementedError
NotImplementedError: No `id` attribute - override `get_id`
#### Fix:
Flask cannot find the id attribute. Update 'user_id' to 'id' in models.py.