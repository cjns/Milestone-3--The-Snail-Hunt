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
A 'Student' can have multiple 'SnailObservation' records. This is a one-to-many relationship.

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

## Wireframes

## Colours
Pros:
Cons:

## Typography / Fonts
Headings & Titles:
Subheadings:
Body:
Pros:
Cons:

## Icons

## Styling

# Technologies
- HTML
- CSS
- JavaScript
- Materialize CSS
- Python
- Flash
- Jinja

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
- [Google Fonts](https://fonts.google.com/): Fonts.
- [Google Variable Fonts](https://fonts.google.com/variablefonts): Variable Fonts.
- [Google Fonts Knowledge](https://fonts.google.com/knowledge/): Typography Knowledge. 
- [Jest](https://jestjs.io/): JavaScript testing.
- [JSHint](https://jshint.com): JavaScript testing.
- [mycolor.space](https://mycolor.space/?hex=%23A9D6BB&sub=1): For colours.
- [Web accessibility evaluation tool (WAVE)](https://wave.webaim.org/): For testing site accessibility quality.
- [WebP Converter](https://developers.google.com/speed/webp): Converting images to the WebP format.
- [VSCode](https://code.visualstudio.com/): Coding text editor.

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