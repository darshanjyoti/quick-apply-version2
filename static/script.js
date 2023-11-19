var isLoggedIn = true;
document.getElementById('showAllButton').addEventListener('click', function() {
    // Redirect to the /all route
      window.location.href = '/all-jobs';
});

function onLoginButtonClick() {
   window.location.href = '/login';
}

function onLogOutButtonClick() {
   window.location.href = '/logout';
}
function redirectToJobDetails(jobId) {
    // Redirect to the job details page with the specific job ID
  if (1) {
    window.location.href = '/job/' + jobId;
  }
  else{
    // Redirect to the login page if the user is not logged in
    window.location.href = '/login';
  }
}
function openContactEmail() {
    // Replace 'contact@example.com' with the actual email address you want to use
    var contactEmail = 'contact@example.com';

    // Compose the mailto link with pre-filled subject and body
    var subject = encodeURIComponent('Inquiry from Quick Apply Website');
    var body = encodeURIComponent('Dear Quick Apply Team,\n\nI have an inquiry:\n\n');

    // Open the default email client with the pre-filled email
    window.location.href = 'mailto:' + contactEmail + '?subject=' + subject + '&body=' + body;
}
