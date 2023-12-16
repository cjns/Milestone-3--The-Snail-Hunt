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
});