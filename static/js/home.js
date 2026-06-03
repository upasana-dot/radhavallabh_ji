const music = document.getElementById("bgMusic");
const button = document.getElementById("musicBtn");
const volumeControl = document.getElementById("volumeControl");

// Set default volume
music.volume = 0.5;

function toggleMusic() {
    if (music.paused) {
        music.play();
        button.innerText = "🔇 Pause Bhajan";
    } else {
        music.pause();
        button.innerText = "🔊 Play Bhajan";
    }
}

// Volume Control
volumeControl.addEventListener("input", function() {
    music.volume = this.value;
});
