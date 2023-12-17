// Materializecss sidenav initialisation
document.addEventListener('DOMContentLoaded', function () {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Date Picker
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: { done: "Ok" }
    });

    // Time Picker
    let timepicker = document.querySelectorAll('.timepicker');
    M.Timepicker.init(timepicker, {
        twelveHour: false, // Use 24-hour format
        i18n: { done: "Ok" }
    });

    // Collapsibles
    let collapsibles = document.querySelectorAll('.collapsible');
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
    if (logoutLink) {
        logoutLink.addEventListener('click', (event) => {
            const confirmation = confirm('Are you sure you want to logout?');
            if (!confirmation) {
                event.preventDefault();
            }
        });
    }

    // Display flash messages as toasts
    /**
     * This function selects all hidden input elements with the class 'flash-message'.
     * For each element, it extracts the data-message and data-class attributes
     * and uses them to display a toast via Materialize's toast mechanism.
     */
    let flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach((flashMessage) => {
        let message = flashMessage.dataset.message;
        let className = flashMessage.dataset.class; // Use the data attributes set in the HTML
        M.toast({ html: message, classes: className, displayLength: 5000 });
    });

});