// PRAYER FORM

const form =
document.getElementById("prayerForm");

form.addEventListener("submit",
function(event) {

    // STOP PAGE RELOAD
    event.preventDefault();

    // SUCCESS MESSAGE
    document.getElementById("successMessage")
    .innerHTML =
    "🙏 Your prayer has been received 🌸";

    // CLEAR FORM
    form.reset();
});