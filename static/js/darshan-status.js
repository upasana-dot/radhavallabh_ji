// ================= TEMPLE STATUS + COUNTDOWN =================

// TEMPLE OPEN/CLOSE TIME
const openHour = 5;
const closeHour = 21;

// AARTI TIMES
const aartiTimes = [
    { name: "Mangla Aarti", hour: 5, minute: 0 },

    { name: "Shringar Darshan", hour: 8, minute: 0 },

    { name: "Rajbhog Darshan", hour: 12, minute: 0 },

    { name: "Sandhya Aarti", hour: 19, minute: 0 },

    { name: "Shayan Darshan", hour: 21, minute: 0 }
];

function updateTempleStatus() {

    const now = new Date();

    const currentHour = now.getHours();

    // TEMPLE STATUS
    const statusElement =
        document.getElementById("templeStatus");

    if (statusElement) {

        if (currentHour >= openHour &&
            currentHour < closeHour) {

            statusElement.innerHTML =
                "🟢 Temple Open";

            statusElement.style.color = "green";

        } else {

            statusElement.innerHTML =
                "🔴 Temple Closed";

            statusElement.style.color = "red";
        }
    }

    // FIND NEXT AARTI
    let nextAarti = null;

    for (let aarti of aartiTimes) {

        const aartiDate = new Date();

        aartiDate.setHours(aarti.hour);
        aartiDate.setMinutes(aarti.minute);
        aartiDate.setSeconds(0);

        if (aartiDate > now) {

            nextAarti = {
                name: aarti.name,
                time: aartiDate
            };

            break;
        }
    }

    // NEXT DAY FIRST AARTI
    if (!nextAarti) {

        nextAarti = {
            name: aartiTimes[0].name,
            time: new Date(
                now.getFullYear(),
                now.getMonth(),
                now.getDate() + 1,
                aartiTimes[0].hour,
                aartiTimes[0].minute
            )
        };
    }

    // COUNTDOWN
    const diff = nextAarti.time - now;

    const hours =
        Math.floor(diff / (1000 * 60 * 60));

    const minutes =
        Math.floor(
            (diff % (1000 * 60 * 60))
            / (1000 * 60)
        );

    const seconds = 
        Math.floor(
            (diff % (1000 * 60))
            / 1000
        );

    const countdownElement =
        document.getElementById("aartiCountdown");

    if (countdownElement) {

        countdownElement.innerHTML =
            nextAarti.name +
            " in " +
            hours +
            "h " +
            minutes +
            "m";
            seconds + 
            "s";
    }
}

// RUN FUNCTION
setInterval(updateTempleStatus, 1000);

updateTempleStatus();

// LIVE DIGITAL CLOCK

function updateClock() {

    const now = new Date();

    let hours = now.getHours();

    let minutes = now.getMinutes();

    let seconds = now.getSeconds();

    let ampm = hours >= 12 ? "PM" : "AM";

    hours = hours % 12;

    hours = hours ? hours : 12;

    hours = hours.toString().padStart(2, "0");

    minutes = minutes.toString().padStart(2, "0");

    seconds = seconds.toString().padStart(2, "0");

    const time =
        `${hours}:${minutes}:${seconds} ${ampm}`;

    document.getElementById("clock").innerHTML =
        time;
}

setInterval(updateClock, 1000);

updateClock();

