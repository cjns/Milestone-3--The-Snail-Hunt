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
|Understand what the site is for|Home Page|
|Find out more information about the site's purpose|Link to external resources|
|Create surveys|Add a survey|
|View surveys|View surveys|
|Update surveys|Edit survey|
|Delete your surveys|Delete survey|
|Register for an account|Register page|
|Log in to your account|Login page|
|Log out of your account|Logout functionality|
|Contact someone for support|Contact page|
|User authorisation|Only the original user can edit/delete their surveys|

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

## Home Page (index.html)
|Feature|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|Introduction|User should see an introduction and understand the site's purpose|View the home page|Introduction is displayed and clear|Pass|
|Link to external resource|User should be able to click the link and be redirected to an external resource for more information|Click the link|User is redirected to the external resource|Pass|
|Navigation|User should be able to navigate to other pages (e.g., register, login, surveys)|Click on navigation links|User is redirected to the clicked page|Pass|

## Register (register.html)
|Feature|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|Registration form|User should be able to fill out form and submit|Fill out form and click submit|User is registered and redirected|Pass|
|Validation|Form should validate input and show errors if invalid|Submit form with invalid input|Form shows error messages|Pass|

## Login (login.html)
|Feature|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|Login form|User should be able to fill out form and submit|Fill out form and click submit|User is logged in and redirected|Pass|
|Validation|Form should validate input and show errors if invalid|Submit form with invalid input|Form shows error messages|Pass|

## Surveys (surveys.html)
|Feature|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|View surveys|User should see a list of surveys|Navigate to page|Surveys are displayed|Pass|
|Link to add survey|User should be able to navigate to add survey page|Click link|User is redirected to add survey page|Pass|

## Add Survey (add_survey.html)
|Feature|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|Add survey form|User should be able to fill out form and submit|Fill out form and click submit|New survey is created and user is redirected|Pass|
|Validation|Form should validate input and show errors if invalid|Submit form with invalid input|Form shows error messages|Pass|

## Edit Survey (edit_survey.html)
|Feature|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|Edit survey form|User should be able to modify existing survey and submit|Modify fields in form and click submit|Survey is updated and user is redirected|Pass|
|Validation|Form should validate input and show errors if invalid|Submit form with invalid input|Form shows error messages|Pass|

## Delete and Edit Buttons
|Feature|Expected Outcome|Testing|Result|Pass/Fail|
|-|-|-|-|-|
|Delete button|User should be able to delete their own surveys|Click delete button on a survey created by the user|Survey is deleted from the list|Pass|
|Delete button|User should not be able to delete surveys created by others|Click delete button on a survey not created by the user|Error message is displayed|Pass|
|Edit button|User should be redirected to the edit survey page for their own surveys|Click edit button on a survey created by the user|User is redirected to the edit survey page with the survey's current information populated|Pass|
|Edit button|User should not be able to edit surveys created by others|Click edit button on a survey not created by the user|Error message is displayed|Pass|

## Bugs
### Bug 1: Login Part 1
**Error**: Exception: Install 'email_validator' for email validation support  
**Fix**: Run `pip install email_validator` or `pip install --user email_validator`

### Bug 2: Login Part 2
**Error**: NoForeignKeysError  
**Fix**: Set up a foreign key relationship between the User and Survey

### Bug 3: Login After Registering a User
**Error**: NotImplementedError: No `id` attribute - override `get_id`  
**Fix**: Flask cannot find the id attribute. Update 'user_id' to 'id' in models.py.

### Bug 4: Console Error When Logout is Not Visible
**Error**: 'script.js:63 Uncaught TypeError: Cannot read properties of null (reading 'addEventListener') at HTMLDocument.<anonymous> (script.js:63:16) (anonymous) @ script.js:63'  
**Fix**: Check that the logoutLink exists before activating the event listener.

### Bug 5: Console Error Regarding Preload
**Error**: A preload for '<URL>' is found, but is not used because the request credentials mode does not match. Consider taking a look at crossorigin attribute.  
**Fix**: Unknown.

### Bug 6: Console Error Regarding Unused Preload
**Error**: The resource <URL> was preloaded using link preload but not used within a few seconds from the window's load event. Please make sure it has an appropriate `as` value and it is preloaded intentionally.  
**Fix**: Unknown.