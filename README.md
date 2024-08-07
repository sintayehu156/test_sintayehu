### Solar Cell Company Calculation

Solar Cell Company Calculation


## Introduction
The test_sintayehu app is a custom Frappe application designed to manage power consumption data and calculate tariffs for solar cell companies. This guide will walk you through the setup of Frappe using Bench, site configuration, and the installation of the test_sintayehu app.

## Prerequisites

Frappe Bench installed and running.
A working Frappe site (e.g., test_sintayehu.com).

### Installation

1. Access Your Bench Directory
Navigate to the directory where your Frappe Bench is initialized. Replace <project-directory> with your project directory name.

cd <project-directory>

2. Get the test_sintayehu App
Fetch the test_sintayehu app from the repository. Use the appropriate repository URL.

bench get-app https://github.com/sintayehu156/test_sintayehu.git

3. Install the App on Your Site
Install the test_sintayehu app on your Frappe site. Replace <site-name> with the name of your site (e.g., test_sintayehu.com).

bench --site <site-name> install-app test_sintayehu

4. Run Migrations
Update the site’s database with the app’s schema changes.

bench --site <site-name> migrate

5. Start Bench
To see the changes and use the app, start the Bench server.

bench start

6. Access the Application
Open your browser and navigate to your Frappe site to access the test_sintayehu app. Replace <site-name> with your actual site name.

http://<site-name>:8000

Example:
http://test_sintayehu.com:8000

### Conclusion
By following these steps, you will have the test_sintayehu app installed and configured on your Frappe Bench setup.


### License

mit
