// Code to email the completed form was found at https://www.emailjs.com/docs/
// Code for the alert message was found at https://sweetalert2.github.io/

function sendMail(contactForm) {
    emailjs
        .send("gmail", "seed_shelf", {
            from_email: contactForm.emailaddress.value,
        })
        .then(
            function () {
                swal({
                    title: "Thanks for signing up!",
                    text: "You'll now start recieving our weekly newsletter",
                    icon: "success",
                    button: "Done",
                });
            },
            function (error) {
                swal({
                    title: "Oops, it looks like something went wrong.",
                    text: "Please try again",
                    icon: "error",
                    button: "Ok",
                });
            }
        );
    document.getElementById("contactForm").reset();
    return false;
}

