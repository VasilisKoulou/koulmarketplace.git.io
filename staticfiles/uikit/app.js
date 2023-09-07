const closeButtons = document.querySelectorAll('.alert__close');

closeButtons.forEach(button => {
    button.addEventListener('click', () => {
        const alertContainer = button.parentElement;
        alertContainer.style.display = 'none';
    });
});