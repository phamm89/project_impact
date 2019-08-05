// Shorthand function for calling document.querySelector
function q (selector) {
    return document.querySelector(selector)
}

// Shorthand function for calling document.querySelectorAll
function qAll (selector) {
    return document.querySelectorAll(selector)
}

// Navigation Variables
const hamburger = q('.hamburger');
const navLinks = q('.nav-links');
const links = qAll('.nav-links li');
const newGoal = q('.new_goal')
const newStep = qAll('.new_step')

// Main execution
document.addEventListener('DOMContentLoaded', function() {

    // Hamburger Style Navigation
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle("open");
        links.forEach(link => {
            link.classList.toggle('fade');
        });
    });

});

newGoal.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log(newGoal)
    $.ajax({
        type: 'POST',
        url: $("#new_goal").attr('action'),
        data: {
            'description': $('.newGoal').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json',
        success: function (data) {
            console.log('Success')
            // $(".answers").load(" .answers")
        }
    });
});


newStep.forEach(item => {
    item.addEventListener('submit', function (e) {
    e.preventDefault();
    console.log(item.action)
    console.log(item.dataset.goal)
    $.ajax({
        type: 'POST',
        url: item.action,
        data: {
            'goal': item.dataset.goal,
            'step': $(item).find('.newStep').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        // dataType: 'json',
        success: function (data) {
            console.log('Success')
            // $(".answers").load(" .answers")
        }
    });
});
})