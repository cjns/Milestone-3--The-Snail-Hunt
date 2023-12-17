# Milestone 3: The Snail Hunt
This is a platform that allows users to enter data they have gathered about the Brown lipped snail and White lipped snail for the Evolution MegaLab study.

You can read more about the [Evolution MegaLab study here](https://www.stem.org.uk/resources/collection/4114/evolution-megalab).

# User Experience (UX)
## Project Goals
> 'Why are we making this product?'
> 'What is worth doing?'
> 'What are we creating?'
> 'What value does it provide?'

The Snail Hunt was created for a group of students at Eccles Sixth Form College to allow them to record and store data easily. The students are part of an extra curricular STEM group that are identifying and classifying snails from their observable features to study variation, evolution, and inheritance.

The web application's purpose is to make it easy for them to store, see, edit, and remove data for the study from a client device.

## Target Audience
Students or anyone interested in recording and categorising their local snail population.

## User Needs / Stories
### First Time Visitor Goals
As a first time user:

- Understand what the site is for.
- Find out more information about the site's purpose.
- Register for an account.

## Returning Visitor Goals
As a returning registered user:

- Log in to my account.
- Log out of my account.
- Create, view, update, and delete my entries.
- Search all entries.
- Export data to csv.
- See and edit my profile.
- Contact someone for support.
- Reset password

## Strategic Tradeoffs

I have assigned a score out of five (5) to the importance and viability / feasibility for each of the user goals to establish the immediate focus. Anything fallout outside of the immediate focus will be considered for a future implementation.

---
|Opportunity / Problem|Importance|Viability / Feasibility|Result|Possible Solution|
|-|-|-|-|-|
|Understand what the site is for|5|5|Will be addressed.|Include an introduction on the main page.|
|Find out more information about the site's purpose|5|5|Will be addressed.|Link to an external resource that describes the study.|
|Create, view, update, and delete my entries|5|5|Will be addressed.|Use the Flask Framework and Postgresql to store and manipulate information.|
|Register for an account|5|5|Will be addressed.|Include a registration page.|
|Log in to my account|5|5|Will be addressed.|Include a login page.|
|Log out of my account|5|5|Will be addressed.|Include a logout link.|
|Search all entries|5|1|Future implementation.|Currently out of scope.|
|Export data to a spread sheet|5|1|Future implementation.|Currently out of scope.|
|See and edit my profile|5|1|Future implementation.|Currently out of scope.|
|Contact someone for support|5|5|Will be addressed.|Add an email address in the footer.|
|Reset password|5|1|Future implementation.|Add the ability to reset a password via email.|

## Features
> 'What are we going to make?'

I am making a web application that will contain the following pages.

### Home page with introduction and a link to an external resource with more information.
Problem(s) it addresses:
- Understand what the site is for.
- Find out more information about the site's purpose.

## A page to view surveys (surveys.html)
Problem(s) it addresses:
- View surveys.

## A page to add surveys (add_surveys.html)
Problem(s) it addresses:
- Add surveys.

## A button to edit/delete surveys
Problem(s) it addresses:
- Update and delete surveys.

## A page to register an account (register.html)
Problem(s) it addresses:
- The ability to create your own account.

## A page to login (login.html)
Problem(s) it addresses:
- The ability to login to your account.

## A link to logout
Problem(s) it addresses:
- The ability to logout of your account.

## Confirmation alerts
- When submitting an edit to a survey.
- When confirming an edit.
- When deleting a survey.
- When adding a survey.
- When logging out.

## Materialize toasts
- After editing a survey.
- After adding a survey.
- After deleting a survey.

## Database
### ERD Components
A 'Student' can have multiple surveys. This is a one-to-many relationship.

1. Entity: User
   - Attributes:
   - id (Primary Key)
   - username (text)
   - password (text)

2. Entity: Survey
   - Attributes:
   - survey_id (Primary Key)
   - survey_date (date)
   - survey_time (time)
   - survey_location (text)
   - survey_habitat (text)
   - survey-recorder (text)
   - user_id (integer, foreign key referencing user id)
   - yellow_brown_lipped_snail_0_bands (integer)
   - pink_brown_lipped_snail_0_bands (integer)
   - brown_brown_lipped_snail_0_bands (integer)
   - yellow_brown_lipped_snail_1_band (integer)
   - pink_brown_lipped_snail_1_band (integer)
   - brown_brown_lipped_snail_1_band (integer)
   - yellow_brown_lipped_snail_many_bands (integer)
   - pink_brown_lipped_snail_many_bands (integer)
   - brown_brown_lipped_snail_many_bands (integer)
   - yellow_white_lipped_snail_0_bands (integer)
   - pink_white_lipped_snail_0_bands (integer)
   - brown_white_lipped_snail_0_bands (integer)
   - yellow_white_lipped_snail_1_band (integer)
   - pink_white_lipped_snail_1_band (integer)
   - brown_white_lipped_snail_1_band (integer)
   - yellow_white_lipped_snail_many_bands (integer)
   - pink_white_lipped_snail_many_bands (integer)
   - brown_white_lipped_snail_many_bands (integer)

## Future Implementations
### A page with search functionality.
Problem(s) it addresses:
- Search all entries.

### The ability to export the data.
Problem(s) it addresses:
- Export data to a spread sheet.

### The ability to reset a password via email
Problem(s) it addresses:
- Reset password.

## Success Metrics
The following metrics can be measured to track the website's success:
- Google Analytics.
- Search engine listings.

## Accessibility
- Use semantic HTML.
- Ensure sufficient colour contrast.
- Provide information for screen readers where appropriate (e.g. aria-labels).

# Design Choices
## Sitemap
- Home
- Register
- Login
- Logout
- Add Survey
- Surveys
   - Add Survey
   - Edit Survey
   - Delete Survey

## Wireframes
![home.html](assets/images/wireframe-home.webp)
![login.html](assets/images/wireframe-login.webp)
![register.html](assets/images/wireframe-register.webp)
![surveys.html](assets/images/wireframe-surveys.webp)
![add_surveys.html](assets/images/wireframe-add-surveys.webp)

## Colours
Pros:
Cons:

## Typography / Fonts
I decided to stick with the Materialize CSS theme to keep everything coherent.
Pros:
- Consistency: Ensure a consistent look and feel.
- Compatibility: Designed to be compatible with a wide range of devices.
- Performance: System fonts, which have faster loading times.
- Maintenance: Do not need to worry about hosting font files.
Cons:
- Lack of uniqueness: Will not stand out as much.
- Limited Control: Less control of the appearance.
- Potential Inconsistencies: System fonts can vary between different operating systems.

## Icons
Icons are taken from [fontawesome's](https://fontawesome.com/) free selection.

## Styling
- Minimal and clean with teal/green colours that are associate with nature.
- Error alerts will use a red palette since it is associate with danger/warnings.

# Technologies
- [HTML](https://html.spec.whatwg.org/multipage/)
- [CSS](https://www.w3.org/Style/CSS/)
- [Materialize CSS](https://materializecss.com/)
- [JavaScript](https://tc39.es/)
- [Python](https://www.python.org/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

# Other Resources
- [Am I Responsive](https://ui.dev/amiresponsive/): Images of responsive design.
- [Balsamiq](https://balsamiq.com/): Wire framing.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/): Testing and debugging.
- [ESLint](https://eslint.org/)
- [favicon.io](https://favicon.io/): For generating the favicon.
- [Font Awesome](https://fontawesome.com/): Icons.
- [Git](https://git-scm.com/): For version control and pushing to Github.
- [GitHub](https://github.com/): To store projects in a public repository.
- [GitHub Desktop](https://desktop.github.com/): Desktop software to simplify the Git/Github development workflow.
- [JSHint](https://jshint.com): JavaScript testing.
- [Web accessibility evaluation tool (WAVE)](https://wave.webaim.org/): For testing site accessibility quality.
- [WebP Converter](https://developers.google.com/speed/webp): Converting images to the WebP format.
- [VSCode](https://code.visualstudio.com/): Coding text editor.
- Real Python:
   - [User Management](https://realpython.com/using-flask-login-for-user-management-with-flask/)
   - [Setting up a static site](https://realpython.com/introduction-to-flask-part-1-setting-up-a-static-site/)
- Digital Ocean:
   - [How To Add Authentication to Your App with Flask-Login](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/utils/)

# Testing
Please visit the [testing](./testing.md) file.

# Deployment & Local Development
## GitHub
## Steps for Forking the Github Repository
## Steps for Making a Local Clone
## Heroku

# Credits
## Code
## Acknowledgements
- Graeme Taylor: Code Institute Mentor.
- Callum Jones: Course Facilitator at [Newcastle College University Centre](https://www.ncl-coll.ac.uk/)
- [Code Institute](https://codeinstitute.net/) for their learning resources.