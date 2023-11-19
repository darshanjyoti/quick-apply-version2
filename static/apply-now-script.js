function openApplicationForm(jobId) {
  // Redirect to the job details page with the specific job ID
  if (1) {
    window.location.href = '/application/' + jobId;
  }
  else{
    // Redirect to the login page if the user is not logged in
    window.location.href = '/login';
  }
}
function openContactEmail(contactEmail) {
    // Compose the mailto link with pre-filled subject and body
    var subject = encodeURIComponent('Inquiry from Quick Apply Website');
    var body = encodeURIComponent('Dear Quick Apply Team,\n\nI have an inquiry:\n\n');

    // Open the default email client with the pre-filled email
    window.location.href = 'mailto:' + contactEmail + '?subject=' + subject + '&body=' + body;
}