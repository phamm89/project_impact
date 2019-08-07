// Shorthand function for calling document.querySelector
function q (selector) {
    return document.querySelector(selector)
}

// Shorthand function for calling document.querySelectorAll
function qAll (selector) {
    return document.querySelectorAll(selector)
}

const hamburger = q('.burger');
const nav = q('.nav-links');
const navLinks = qAll('.nav-links li');


// Main execution
document.addEventListener('DOMContentLoaded', function() {

    // Hamburger Style Navigation
hamburger.addEventListener('click', () => {

    nav.classList.toggle("nav-active");
    
    // Animate
    navLinks.forEach((link, index) =>{
        if(link.style.animation){
            link.style.animation = ' ';
        
        } else{
            link.style.animation = `navLinkFade 0.5s ease forwards ${index/7 + .2}s`
        }
        
    });
        
});
    
});







// Goals variables
const newGoal = q('.new_goal')
const newStep = qAll('.new_step')
const checkBox = qAll('.step-done-checkbox')
console.log(checkBox)

// Main execution for goals

newGoal.addEventListener('submit', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: $("#new_goal").attr('action'),
        data: {
            'description': $('.newGoal').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        // dataType: 'json',
        success: function (data) {
            // $(".goals").load(" .goals")
            location.reload();
        }
    });
});




function handleTitleChange(e){
	const result = document.getElementById('result');

	result.innerHTML = 'The result is: ' + e.target.textContent;
}

//Trying to select item from goals

const getGoalItem = document.querySelectorAll('.goal-description')
// console.log(getGoalItem)


newStep.forEach(item => {
    item.addEventListener('submit', function (e) {
    e.preventDefault();

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
            // console.log('Success')
            // $(".goals").load(" .goals")
            location.reload();
        }
    });
});
})



checkBox.forEach(item => {
    item.addEventListener('change', function (e) {
        e.preventDefault();
        fetch(`goal/check_mark/${item.dataset.step}/`, {
            method: 'PATCH',
            body: JSON.stringify({ 'done': item.checked }),
        })
    })
})


const goals = document.querySelectorAll('.goal-div')
goals.forEach(item => {
    item.addEventListener('click', function (e) {
    const individualSteps = item.querySelectorAll('.individual-steps')
        individualSteps.forEach(step => { 
            step.innerHTML = `<div> ${step.dataset.step} </div>`
        });

        return individualSteps
    });

    });

