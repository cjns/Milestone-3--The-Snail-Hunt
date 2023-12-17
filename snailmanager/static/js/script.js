// Materializecss sidenav initialisation
document.addEventListener('DOMContentLoaded', function () {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Date Picker
    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: { done: "Ok" }
    });

    // Time Picker
    var timepicker = document.querySelectorAll('.timepicker');
    M.Timepicker.init(timepicker, {
        twelveHour: false, // Use 24-hour format
        i18n: { done: "Ok" }
    });

    // Collapsibles
    var collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);

    // Delete confirmation
    /**
     * Adds a click event listener to all elements with the class 'delete-btn'.
     * When a delete button is clicked, a confirmation dialog will appear.
     * If the user clicks "Cancel", the default action of the event (following the link) is cancelled.
     */
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const confirmation = confirm('Are you sure you want to delete this survey?');
            if (!confirmation) {
                event.preventDefault();
            }
        });
    });

    // Edit confirmation
    /**
     * Adds a click event listener to all elements with the class 'edit-btn'.
     * When an edit button is clicked, a confirmation dialog will appear.
     * If the user clicks "Cancel", the default action of the event (following the link) is cancelled.
     */
    const editButtons = document.querySelectorAll('.edit-btn');
    editButtons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const confirmation = confirm('Are you sure you want to edit this survey?');
            if (!confirmation) {
                event.preventDefault();
            }
        });
    });

    // Logout confirmation
    /**
     * Adds a click event listener to the logout link with the class 'logout'.
     * When the logout link is clicked, a confirmation dialog will appear.
     * If the user clicks "Cancel", the default action of the event (logging out) is cancelled.
     */
    const logoutLink = document.querySelector('.logout');
    logoutLink.addEventListener('click', (event) => {
        const confirmation = confirm('Are you sure you want to logout?');
        if (!confirmation) {
            event.preventDefault();
        }
    });

    // Check if there are any flash messages
    var flashMessage = document.getElementById('flash-message');
    if (flashMessage) {
        // Get the class name from the data-class attribute
        var className = flashMessage.getAttribute('data-class');
        // Display the toast
        M.toast({ html: flashMessage.textContent, classes: className });
    }

});