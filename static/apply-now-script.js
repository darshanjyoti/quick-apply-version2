function openApplicationForm(contactEmail, jobTitle) {
  console.log("apply now clicked")
    // Compose the mailto link with pre-filled subject and body
  var subject = encodeURIComponent('Job Application for ' + jobTitle);
  var body = encodeURIComponent('Dear Hiring Team,\n\nI am interested in applying for the position of ' + jobTitle + '.\n\nPlease find my details below:\n\nName:\nEmail:\n\nPlease Find attached resume.\n\nThank you,\n[Your Name]');
  var mailtoLink = 'mailto:' + contactEmail + '?subject=' + subject + '&body=' + body;

    // Open the default email client with the pre-filled email
    window.location.href = mailtoLink;
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