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
|Page|HTML|Lighthouse Mobile|Lighthouse Desktop|Notes|
|-|-|-|-|-|
|Home|[Valid*](https://validator.w3.org/#validate_by_uri)|[Mobile](assets/images/lighthouse-home-mobile.webp)|[Desktop](assets/images/lighthouse-home-desktop.webp)|Errors/warnings relate to Jinja templates only.|
|Register|[Valid*](https://validator.w3.org/#validate_by_uri)|[Mobile](assets/images/lighthouse-register-mobile.webp)|[Desktop](assets/images/lighthouse-register-desktop.webp)|Errors/warnings relate to Jinja templates only.|
|Log in|[Valid*](https://validator.w3.org/#validate_by_uri)|[Mobile](assets/images/lighthouse-login-mobile.webp)|[Desktop](assets/images/lighthouse-login-desktop.webp)|Errors/warnings relate to Jinja templates only.|
|Surveys|[Valid*](https://validator.w3.org/#validate_by_uri)|[Mobile](assets/images/lighthouse-surveys-mobile.webp)|[Desktop](assets/images/lighthouse-surveys-desktop.webp)|Errors/warnings relate to Jinja templates only.|
|Add Survey|[Valid*](https://validator.w3.org/#validate_by_uri)|[Mobile](assets/images/lighthouse-add_survey-mobile.webp)|[Desktop](assets/images/lighthouse-add_survey-desktop.webp)|Errors/warnings relate to Jinja templates only.|
|Edit Survey|[Valid*](https://validator.w3.org/#validate_by_uri)|[Mobile](assets/images/lighthouse-edit_survey-mobile.webp)|[Desktop](assets/images/lighthouse-edit_survey-desktop.webp)|Errors/warnings relate to Jinja templat only.|
|403|Valid|[Mobile](assets/images/lighthouse-403-mobile.webp)|[Desktop](assets/images/lighthouse-403-desktop.webp)|Pages with unsuccessful HTTP status codes may not be indexed properly|
|404|Valid|[Mobile](assets/images/lighthouse-404-mobile.webp)|[Desktop](assets/images/lighthouse-404-desktop.webp)|Pages with unsuccessful HTTP status codes may not be indexed properly|
|405|Valid|Unable to test|Unable to test|
|500|Valid|Unable to test|Unable to test|
|Base|Valid|n/a|n/a|

## Accessibility
|Page|Wave Validation|Notes|
|-|-|-|
|Home|[Pass](assets/images/wave-home.webp)||
|Register|[Pass](assets/images/wave-register.webp)||
|Login|[Pass](assets/images/wave-login.webp)||
|Surveys|[Pass](assets/images/wave-surveys.webp)||
|Add Survey|[Pass*](assets/images/wave-add_survey.webp)|Alerts are due to Materialize CSS including tab indexes after the [Time Picker Buttons](assets/images/wave-time_picker_buttons.webp)|
|Edit Survey|[Pass*](assets/images/wave-edit_survey.webp)|Alerts are due to Materialize CSS including tab indexes after the [Time Picker Buttons](assets/images/wave-time_picker_buttons.webp)||
|403|[Pass](assets/images/wave-403.webp)||
|404|[Pass](assets/images/wave-404.webp)||
|405|Unable to test|Unable to test|
|500|Unable to test|Unable to test|


## CSS
|File|Validation|
|-|-|
|style.css|[Valid, no error found](assets/images/css-valid.webp)|

## JavaScript
|File|Validation|Notes|
|-|-|-|
|script.js|[Valid*](assets/images/js-valid.webp)||

## Python
|File|Valid|Notes|
|-|-|-|
|forms.py|[Valid](assets/images/forms.webp)||
|models.py|[Valid](assets/images/models.webp)||
|routes.py|[Valid](assets/images/routes.webp)||
|run.py|[Valid](assets/images/run.webp)||
|__init__.py|[Valid](assets/images/init.webp)||

## Nav & Footer Links
|Link|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|Home|Go to home page|Click link|Goes to expected page|Pass|
|Login|Go to login page|Click link|Goes to expected page|Pass|
|Register|Go to register page|Click link|Goes to expected page|Pass|
|Surveys|Go to surveys page|Click link|Goes to expected page|Pass|
|Add Survey|Go to add survey page|Click link|Goes to expected page|Pass|
|Email for support|Opens email client|Click link|Opens email client|Pass|

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