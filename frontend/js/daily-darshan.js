const darshanImages = [
    "/Users/upasanaporwal/Desktop/Radhavallabh ji/frontend/Images/WhatsApp Image 2025-12-25 at 23.15.35.jpeg",
    "/Users/upasanaporwal/Desktop/Radhavallabh ji/frontend/Images/WhatsApp Image 2026-01-15 at 21.41.11.jpeg",
    "/Users/upasanaporwal/Desktop/Radhavallabh ji/frontend/Images/WhatsApp Image 2026-01-15 at 21.41.26.jpeg",
    "/Users/upasanaporwal/Desktop/Radhavallabh ji/frontend/Images/WhatsApp Image 2025-12-25 at 23.15.41.jpeg"
];

// Get today's date number
const today = new Date();
const day = today.getDate();

// Select image based on day
const imageIndex = day % darshanImages.length;

// Set image
document.getElementById("darshanImage").src = darshanImages[imageIndex];

document.getElementById("darshanDate").innerText =
    today.toDateString();
