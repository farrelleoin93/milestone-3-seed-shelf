## Index
- [User Stories](#userstories)
- [Features](#features)
- [Technologies](#technologies)
- [Testing](#testing)
- [Bugs](#bugs)

### <a name="#userstories">Testing User Stories</a> 
### All Users
1. "As a user I want to be able to understand what the site is for immedietly from the home page."
   - The home page has a large hero image of potting equipment and also a short couple of lines that briefly explains what the website does.
   - The home page also has an images carousel of some of the plants that people have added. These images are also links to the page where the user can learn to grow the plant.
   - The is also a "Recently Added" section at the bottom of the homepage displaying the three most recently added seeds.
2. "As a user I want to be able to easily navigate through the site."
   - The navbar has clear and descriptive words so that the user will be able to easily navigate through the website.
   - All images on the "Home" page and "Seeds" page are also links that will direct the user to the page where they can learn to grow a seed.
3. "As a user I want to be able to search for seeds that I would like to grow."
   - On the "Seeds" page there is a search bar so users can easily seatch for a plant that they would like to grow.
4. "As a user I want to be able to filter the seeds by categories so that I can easily find the types of seeds that I want."
   - The is also a dropdown menu on the "Seeds" page which allows the user to filer the seeds by category for example "Herbs" or "Vegetables"
5. "As a user I would like to be able to recieve emails containing information about gardening."
   - In the footer there is a section where the user can add their email address. If the user avails of this they will recieve a weekly newsletter about gardening.

### Unregistered Users
1. "As an unregistered user I would like to be able to easily register for this website.
   - If an unregistered user is on the website a "Register" option will appear in the navbar which will direct the user to a page so that they can register.
2. "As an unregistered user I would like to be able to view all the seeds even when I am not registered."
   - The "Seeds" page is available for all users not just those who have registered. Th user can navigate to this page by clicking on the "Seeds" option in the navbar.

### Registered Users 
1. "As a registered user I would like to be able to add my own seed to the collection of seeds displayed on the website so that I can share the knowledge I have with like minded people."
   - An "Add Seed" page is available to all registered users. Users can reach this page by clicking on the "Add Seed" option in the navbar or by clicking on the floating button on their "Profile" page.
2. "As a registered user I would like to be able to view any seeds that I have added easily and locate them in the same place."
   - The users "Profile" page displays all the seeds that they have added to the website.
3. "As a registered user I would like to be able to edit any seed that I have added in case I made a mistake or would like to change something." 
   - There is an edit button under each of the users seeds on their "Profile" page. This button will direct them to the a page where they can edit the information for their seed. This edit page has the same layout as the page that they used to add the seed so the user will be familar with how to use it.
4. "As a registered user I would like to be able to delete any seeds that I have added."
   - There is a delete button under each of the users seeds on their "Profile" page. If the user clicks this button they are met with a box where they must confirm that they would like to delete the seed.

#### Testing Site Owner Goals

1.  "As the owner I want to inspire people to grow there own plants and discover the joys of gardening."
   - I feel that this is achieved by supplying the users with a website that is clear, concise and easy to navigate. 
2. "As the owner I want to provide people with a visually appealing website."
   - This is achieved by the use of appealing imagery and and consistent styling thoughout the website. The minimal use of text also aids the visual appeal of the website.
3. "As the owner I want to provide people with clear instructions on how to grow different types of plants."
   - Although the instructions for growing the seeds on this website are provided by the users the layout of the grow seed page is clear and instructive. As admin the site owner has the ability to delete any seeds that they feel are not clear or in keeping with the style of the website.
4. "As the owner I want to increase the volume of people that visit this website over time."
   - Although this has not been widely tested yet most users that I got to try out the website said that they would use the website again and recommend it to friends. They said that the fact that new seeds will be consistantly added would encourage them to return to the website.
5. "As the owner I want to be able to delete the content that users have added."
   - The "admin" has the ablity to delete any seed that they wish. This ability is reserved for the admin and the creater of the seed only.

### Manual testing

The following tests have been carried out without any issues:

**Navigation bar**

Mobile:
- Tapping/clicking the logo takes users to the Home page.
- When the hamburger menu icon is clicked/tapped all the menu options that are available to the user are displayed in the Sidenav.
- The correct menu options appear depending on the user's session status:
- Only the correct menu options are displayed depending on whether the user is logged in or not:
  - **Not logged in**: Home, Seeds, Log In, Register
  - **Logged in**: Home, Seeds, Add Seed, Profile, Log Out
- The active page is indicated.
- Tapping/clicked each link directs the user to the relevant page.

On screen widths greater than 992px:
- A standard navigation bar replaces the hamburger menu.
- When the mouse hovers over an navigation option a shadow appears.

**Footer**

- The footer remains stuck to the bottom of the page even when all content is removed.
- The newsletter sends to users email to the site owners email so that they can be added to a list recieve a weekly newsletter.
- A success message is displayed to the user when the sign up, and an error message is displayed when the signup failed.
- Each social media link opens the relevant external page in a new window.

**Seed Cards**
1. **Home page and Seeds page**
    - The seed image is displayed with on overlay displaying the seed name in the center of the image appearing when the mouse is hovering over the image.
    - If the user that uploaded the seed did not provide an image a default image appears in its place.
    - The overlay and seed name are always visable on tablets and phones as hover effect does not work on these devices.
    - Clicking/tapping the image will direct the user to the relevent seed view page. 
2. **Profile page**
    - The seed image is displayed, when this image is clicked/tapped the user is redirected to the seed view page for the specific seed.
    - The seed name, plant type and who created the seed is displayed beneath the image.
    - An edit and delete button are located at the bottom of the card.
    - If the edit button is clicked/tapped the user is redirected to the edit seed page.
    - If the user clicks/taps the delete button a modal appears asking if they really want to delete the seed. If cancel is clicked/tapped the modal disappears and the user remains on the seed view page. If confirm is clicked/tapped by the user the seed is deleted from the database, the user is redirected to the seeds page and a toast message appears stating that the seed was deleted successfully.

**Home page**

- "Find Seeds" button on hero image directs user to the Seeds page.
- The carousel displays five seeds and automatically skips through them.
- Clicking/tapping on a an image in the carousel directs the user to the relevent seed view page.
- The three most recently added seeds are displayed in the "Recently added section"
- The seed cards in the "Recently Added" section function as described in the Seed Cards testing section (see above).
- Three cards appear in a row on tablet devices and bigger but appear one on top of another on mobile devices.

**Seeds page**
- All seeds in the database are displayed in the form of cards.
- The seed cards function as described in the Seed Cards testing section (see above).

Search and Filter:
- If the user enters a word in the search field and hits enter or clicks/taps "Search" all the seeds that contain word in the database will be displayed.
- If the user picks a specific category in the dropdown filter the seeds that are in that category are displayed immedietly.
- Clicking/tapping the cancel icon reloads the page with no query or filter applied.
- If no results are found a heading is displayed stating that no results were found.

**Add Seed Page**

- If a user is not logged in and tries to reach the Add Seed page with brute force using the url they are redirected to the log in page and a toast message appears stating that they need to be logged in to do that.
- If the user leaves the "Seed name" or "Category" field empty they are indicated that the field must be filled out by a red line appearing under the relevant field.
- The seed category dropdown contains the different seed categories from the MongoDB database for the user to choose from.
- The user is instructed that they must enter each new instruction on a new line.
- The 'Submit' button does the following:
  - Adds the seed to the seeds collection.
  - Redirects to the user to the seeds page, showing the new seed as the first seed.
  - A toast message is displayed stating that the seed was successfully added.

**Edit Seed Page**
- If a user is not logged in and tries to reach the Add Seed page with brute force using the url they are redirected to the log in page and a toast message appears stating that they need to be logged in to do that.
- If a user is logged in and tries to use brute force to edit another users seed they are redirected to the seeds page and a toast message is displayed stating that the seed does not belong to them.
- When the edit seed page opens the input fields already contain the seeds existing values.
- If the user leaves the "Seed name" or "Category" field empty it is indicated to them that the field must be filled out by a red line appearing under the relevant field.
- The seed category dropdown contains the different seed categories from the MongoDB database for the user to choose from.
- The user is instructed that they must enter each new instruction on a new line.
- The 'Edit' button does the following:
  - Edits the seed in the seeds collection.
  - Redirects the user to the seeds page.
  - A toast message is displayed stating that the seed was successfully updated.
- The admin can edit or delete any seed.

**Seed View Page**
- If a user is logged in and they have added the seed edit and delete buttons appear at the top of the page.
- If admin is logged in edit and delete buttons appear at the top of all seed pages.
- If the edit button is clicked/tapped the user is redirected to the edit seed page.
- If the user clicks/taps the delete button a modal appears asking if they really want to delete the seed. If cancel is clicked/tapped the modal disappears and the user remains on the seed view page. If confirm is clicked/tapped by the user the seed is deleted from the database, the user is redirected to the seeds page and a toast message appears stating that the seed was deleted successfully.
- If a user is not logged in and tries to delete a seed with brute force using the url they are redirected to the log in page and a toast message appears stating that they need to be logged in to do that.
- If a user is logged in and tries to use brute force to delete another users seed they are redirected to the seeds page and a toast message is displayed stating that the seed does not belong to them.
- The description moves to underneath the image on mobile devices.
- If there are no harvesting instructions for a seed in the database the "Harvesting Instructions" section of the page does not appear.

**Profile Page**
- A floating action button to add a seed is located at the page.
- When the floating action button is clicked/tapped the user is relocated to the add seed page.
- All seeds that the user has created appear in the form of cards
- The seed cards function as described in the Seed Cards testing section (see above).
- If the user has not added any seeds a message is displayed stating that they have not added any seeds and they are provided with a link to the add seed page.

**Register page**

- If the user is already registered the 'Log In' link takes the user to the Log In page.
- If the user enters a username or password that does match the form validation it highlights the issue to the user by displaying a red line.
- If the user enters correctly formatted username and password fields the form displays a green line indicating that the fields are acceptable.
- If the user submits a username (uppercase or lowercase) that is already registered the page reloads and a toast is displayed stating that the username is taken.
- If all the fields are valid the user is redirected to their new Profile page upon clicking/tapping the "Register" button and a toast message is displayed stating that their registration was successfull.
- The newly registered user's username and password are added to the users collection in the database.
- If the user is already registered the 'Log In' link takes the user to the Log In page.

**Log In page**

- Entering a username or password not matching the form validation highlights the issue to the user.
- If the user enters a username or password that does match the form validation it highlights the issue to the user by displaying a red line.
- If the user enters correctly formatted username and password fields the form displays a green line indicating that the fields are acceptable.
- If all the fields are valid the user is redirected to their Profile page upon clicking/tapping the "Log In" button and a toast message is displayed stating that their log in was successfull.
- If the user has not already registered the 'Register' link takes the user to the Register page.

### Automated testing
[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Lighthouse was used to audit all pages:

**Home page**

- Performance: **95%**
- Accessibility: **97%**
- Best Practices: **87%**
- SEO: **100%**

**Seeds page**

- Performance: **92-98%**
- Accessibility: **89%**
- Best Practices: **87%**
- SEO: **100%**

**Add Seed page**

- Performance: **98-99%**
- Accessibility: **88%**
- Best Practices: **87%**
- SEO: **100%**

**Profile page**

- Performance: **99%**
- Accessibility: **94%**
- Best Practices: **87%**
- SEO: **90%**

**Log In page**

- Performance: **97-99%**
- Accessibility: **97%**
- Best Practices: **87%**
- SEO: **100%**

**Register page**

- Performance: **96-97%**
- Accessibility: **97%**
- Best Practices: **87%**
- SEO: **100%**

- Lighthouse reported a warning on each page that "Background and foreground colors do not have a sufficient contrast ratio." in regards to the navbar, however I have tested this website on people and all report that they had no trouble in reading the navbar elements so I decided to ignore this warning.

## <a name="bugs">Bugs</a>

---

### Bugs fixed while building the website:

1. **Seed cards displaying three times.** 
    - To fix this bug I simply changed the location of the for loop.
2. **Deleting session user then logging out crashes the site.**
    - To fix this I added an if statement to the logout function checking if the user was in session. If the user is not in session they are redirected to the home page and a toast message is displayed stating that they are already logged out.
3. **When the admin edited another users seed the admin then appeared as the creater of the seed.**
    - To solve this issue I changed the "created by" part of the edit function so that the original creater remained the seed creater.
4. **All seed instructions were being added to the database in an array containing one string, this caused issues when displaying the instructions on the seed view page**
    - To fix this issue the instructions information needed to be sent to the database as a string not an array. I then added the splitlines() to the instructions part of the seed view page. I recieved help and advice on this issue from Stephen, one of the Code Institute's tutors.
6. **When the vegetable option of the dropdown filter was selected twice it crashed the site** 
    - To fix this bug I removed the seeds=seeds that I was passing into the filter url_for as the filter view did not take a parameter. I was helped with this issue by Michael, one of the Code Institute's tutors.
7. **When all option in dropdown select on the seeds page was picked I got the error: "object of type 'Cursor' has no len() convert it to list"**
    - This issue was fixed by adding the list() constructor to "All" in the filter function. I recieved help on how to rectify this issue by browsing through slack and reading about how other people solved similar issues.
