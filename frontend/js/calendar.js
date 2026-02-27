const monthYear = document.getElementById("monthYear");
const calendarDates = document.getElementById("calendarDates");

let currentDate = new Date();

/* EVENTS DATA */
const events = {
    "2026-09-03": "🌸 Radhashtami",
    "2026-09-10": "🪔 Aarti Utsav",
    "2026-10-27": "🎉 Sharad Purnima",
    "2026-08-19": "🎊 Janmashtami",
    "2026-06-09": "🌼 It's my birthday"
};

function renderCalendar() {
    calendarDates.innerHTML = "";

    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();

    monthYear.innerText = currentDate.toLocaleString("default", {
        month: "long",
        year: "numeric"
    });

    const firstDay = new Date(year, month, 1).getDay();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    /* EMPTY CELLS */
    for (let i = 0; i < firstDay; i++) {
        calendarDates.innerHTML += `<div class="day empty"></div>`;
    }

    /* DAYS */
    for (let day = 1; day <= daysInMonth; day++) {
        const fullDate = `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;

        if (events[fullDate]) {
            calendarDates.innerHTML += `
                <div class="day event">
                    <strong>${day}</strong>
                    <span>${events[fullDate]}</span>
                </div>
            `;
        } else {
            calendarDates.innerHTML += `
                <div class="day">
                    <strong>${day}</strong>
                </div>
            `;
        }
    }
}

/* CONTROLS */
function prevMonth() {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();
}

function nextMonth() {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();
}

/* INIT */
renderCalendar();
