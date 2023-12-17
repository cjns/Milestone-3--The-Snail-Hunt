# Testing
## Links
- Nav
    - Home
    - Surveys
    - Add Survey

- Home page
    - Snail hunt logo.
    - How to hunt banded snails link.

## Buttons
Surveys.html
- Add Survey

add_survey.html
- Add Survey

## add_survey.html
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

## registration.html
- All fields required to make a submission.
- 

## login.html

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