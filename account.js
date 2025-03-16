const container = document.getElementById('container');
    const overlayBtn = document.getElementById('overlayBtn');
    const overlayCon = document.getElementById('overlayCon');

    overlayBtn.addEventListener('click', () => {
    container.classList.toggle('right-panel-active');

    overlayBtn.classList.remove('btnScaled');
    window.requestAnimationFrame( () => {
    overlayBtn.classList.add('btnScaled');
    })
});
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400,
    //reset: true

})
sr.reveal('.container', {delay: 90, interval: 100, origin: 'top'})
sr.reveal('.container p, .container span', {interval: 200})
sr.reveal('.container a, .container button', {delay: 120, interval: 100, origin: 'bottom'})
sr.reveal('.container h2', {delay: 100, interval: 100, origin: 'top'})  
sr.reveal('.container .infield', {delay: 150, interval: 100, origin: 'bottom'})

const signUpForm = document.getElementById("sign-up-form");
const signInForm = document.getElementById("sign-in-form");
const toSignUpLink = document.getElementById("to-sign-up");
const toSignInLink = document.getElementById("to-sign-in");

toSignUpLink.addEventListener("click", (e) => {
    e.preventDefault();
    signUpForm.style.display = "block";
    signInForm.style.display = "none";
});

toSignInLink.addEventListener("click", (e) => {
    e.preventDefault();
    signInForm.style.display = "block";
    signUpForm.style.display = "none";
});
