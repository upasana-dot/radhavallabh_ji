function openEvent(title, image, date, desc) {
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalImage").src = image;
    document.getElementById("modalDate").innerText = date;
    document.getElementById("modalDesc").innerText = desc;

    document.getElementById("eventModal").style.display = "flex";
}

function closeEvent() {
    document.getElementById("eventModal").style.display = "none";
}
