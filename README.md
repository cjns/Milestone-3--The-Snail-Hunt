# Milestone 3: The Snail Hunt
This is a platform that allows users to enter data they have gathered about the Brown lipped snail and White lipped snail for the Evolution MegaLab study.

You can read more about the Evolution MegaLab study here.

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
- Create, view, update, and delete my entries.
- Search all entries.

## Strategic Tradeoffs

I have assigned a score out of five (5) to the importance and viability / feasibility for each of the user goals to establish the immediate focus. Anything fallout outside of the immediate focus will be considered for a future implementation.

---
|Opportunity / Problem|Importance|Viability / Feasibility|Result|Possible Solution|
|-|-|-|-|-|
|Understand what the site is for.|1|1|Will be addressed.|Include an introduction on the main page.|
|Find out more information about the site's purpose.|1|1|Will be addressed.|Include a separate page that provides more information about the study.|
|Create, view, update, and delete my entries.|1|1|Will be addressed.|Use the Flask Framework and Postgresql to store and manipulate information.|
|Register for an account.|1||||
|Log in to my account.|1||||
|Search all entries.|1||||
|Export data to a spread sheet.|1||||

# Features
> 'What are we going to make?'

I am making a web application that will contain the following pages.

1. Home page with intro.
Problem it addresses: Understand what the site is for.

2. A page with additional information about the study.
Problem it addresses: Find out more information about the site's purpose.

3. A page to add/modify a record.
Problem it addresses: Create, view, update, and delete my entries.


## Database
### ERD Components
A 'Student' can have multiple 'SnailObservation' records. This is a one-to-many relationship.

1. Entity: Student
   - Attributes:
   - student_id (Primary Key)
   - student_name (string)
   - other student-related information.

2. Entity: SnailObservation
   - Attributes:
   - observation_id (Primary Key)
   - observation_date (date)
   - snail_color (string)
   - banding_count (integer)
   - location (string)
   - habitat (string)
   - student_id (Foreign Key referencing Student).

## Future Implementations

4. A registration page.
Problem it addresses: Register for an account.

5. A login page.
Problem it addresses: Log in to my account.

6. A page with search functionality.
Problem it addresses: Search all entries.

7. The ability to export the data.
Problem it addresses: Export data to a spread sheet.

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
- Materialize
- JavaScript
- Jest
- Node
- Babel

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
