document.addEventListener("DOMContentLoaded", () => {
    const jokeDiv = document.getElementById("joke");
    let state = 0; // 0 - ожидание, 1 - setup, 2 - punchline
    let currentSetup = "";
    let currentPunchline = "";

    async function loadJoke() {
        jokeDiv.textContent = "Loading the joke, vro..";
        try {
            const response = await fetch("/joke");
            if (!response.ok) throw new Error("Error loading joke, vro..");
            const data = await response.json();
            currentSetup = data.setup;
            currentPunchline = data.punchline;
            state = 1;
            jokeDiv.textContent = currentSetup;
        } catch (e) {
            jokeDiv.textContent = "Cannot reach the joke, vro..";
            state = 0;
        }
    }

    jokeDiv.addEventListener("click", () => {
        if (state === 0) {
            loadJoke();
        } else if (state === 1) {
            jokeDiv.textContent = currentPunchline;
            state = 2;
        } else if (state === 2) {
            loadJoke();
        }
    });

    // начальное состояние
    jokeDiv.textContent = "Start the joke, vro..";
    state = 0;
});
