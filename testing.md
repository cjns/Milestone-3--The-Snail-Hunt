# Testing
## Tools
The following tools were used for testing:

- HTML: [W3C Markup Validator](https://validator.w3.org/)
- CSS: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- Accessibility: [WAVE (Web Accessibility Evaluation Tool)](https://wave.webaim.org/)
- Performance: [Lighthouse (Within Chrome Developer Tools)](https://developer.chrome.com/docs/lighthouse/overview/)
- Python Syntax: [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
- JS Syntax: [ESLint](https://eslint.org/)

## Testing Client Stories
|Opportunity/Problem|Evidence of meeting user story|
|-|-|
|Understand what the site is for|[Home page]()|
|Find out more information about the site's purpose|[Link to external resources]()|
|Create surveys|[Add a survey]()|
|View surveys|[View surveys]()|
|Update surveys||
|Delete your surveys||
|Register for an account||
|Log in to your account||
|Log out of your account||
|Contact someone for support||

## HTML, Accessibility, & Performance
|Page|HTML|Lighthouse Mobile|Lighthouse Desktop|
|-|-|-|-|
|Home|[Valid*](https://validator.w3.org/#validate_by_uri)|||
|Log in|[Valid*](https://validator.w3.org/#validate_by_uri)|||
|Register|[Valid*](https://validator.w3.org/#validate_by_uri)|||
|Surveys|[Valid*](https://validator.w3.org/#validate_by_uri)|||
|Add Survey|[Valid*](https://validator.w3.org/#validate_by_uri)|||
|Edit Survey|[Valid*](https://validator.w3.org/#validate_by_uri)|||
|403|[Valid]()|||
|404|[Valid]()|||
|405|[Valid]()|||
|500|[Valid]()|||
|Base|[Valid]()|||
* Errors/warnings relate to Jinja templates only.

## Accessibility
|Page|Wave Validation|
|-|-|
|Home||
|Login||
|Register||
|Surveys||
|Add Survey||
|Edit Survey||
403
404
405
500

## CSS
|File|Validation|
|-|-|
|style.css|[Valid, no error found](https://jigsaw.w3.org/css-validator/#validate_by_uri)|

## JavaScript
|File|Validation|
|-|-|
|script.js|[Valid*](assets/images/js-valid.webp)|
*'M' refers to the global object for Materialize.

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

### 4
#### Description
Console error: Returning null because logout is not visible unless logged in.
#### Error:
'script.js:63 Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')
    at HTMLDocument.<anonymous> (script.js:63:16)
(anonymous) @ script.js:63'
### Fix:
Check that the logoutLink exists before activating the event listener.

### 5
#### Description
Console error.
#### Error:
A preload for '<URL>' is found, but is not used because the request credentials mode does not match. Consider taking a look at crossorigin attribute.
#### Fix:
Unknown.

### 6
#### Description
Console error.
#### Error:
The resource <URL> was preloaded using link preload but not used within a few seconds from the window's load event. Please make sure it has an appropriate `as` value and it is preloaded intentionally.
#### Fix:
Unknown.