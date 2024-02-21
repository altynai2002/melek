function handleKeyPress(event, nextInputId) {
    if (event.keyCode === 13) {
        const nextInput = document.getElementById(nextInputId);
        if (nextInput) {
            nextInput.focus();
        }
    }
}