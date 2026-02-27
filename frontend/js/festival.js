// FESTIVAL DATE CONFIGURATION
// Example: Radhashtami (change dates anytime)
const festival = {
    name: "Radhashtami",
    start: { day: 15, month: 8 }, // 15 September
    end: { day: 16, month: 8 }
};

const today = new Date();
const day = today.getDate();
const month = today.getMonth(); // 0 = Jan

if (
    month === festival.start.month &&
    day >= festival.start.day &&
    day <= festival.end.day
) {
    activateFestivalMode();
}

function activateFestivalMode() {
    // Show banner
    document.getElementById("festivalBanner").style.display = "block";

    // Change background
    document.body.classList.add("festival-bg");

    // Start flowers
    startFlowerAnimation();
}

function startFlowerAnimation() {
    const container = document.getElementById("flowerContainer");

    for (let i = 0; i < 20; i++) {
        const flower = document.createElement("img");
        flower.src = "/Users/upasanaporwal/Desktop/Radhavallabh ji/frontend/Images/lotus.jpeg";
        flower.className = "flower";

        flower.style.left = Math.random() * 100 + "vw";
        flower.style.animationDuration = (5 + Math.random() * 5) + "s";

        container.appendChild(flower);
    }
}
