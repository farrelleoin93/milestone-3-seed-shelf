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

## <a name="bugs">Bugs</a>

---

### Bugs fixed while building the website:

1. cards displaying 3 times, change location of for loop
2. deleting session user then logging out crashed the site.
3. change created by part of submit in edit so original creater remains creater
4. fix splitlines bug
4. fix registration but by changing from render template to redirect
6. vegetables bug - remove unnecessary variable
