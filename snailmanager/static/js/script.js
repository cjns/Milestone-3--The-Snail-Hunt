// Materializecss sidenav initialisation
document.addEventListener('DOMContentLoaded', function () {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Date Picker
    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Ok"}
    });

    // Time Picker
    var timepicker = document.querySelectorAll('.timepicker');
    M.Timepicker.init(timepicker, {
        i18n: {done: "Ok"}
    });
});

