window.onload = function () {

    const quotes = [
        "🌸 राधा नाम ही परम सुख है।",
        "🪔 प्रेम ही भक्ति का वास्तविक स्वरूप है।",
        "🌺 श्री राधावल्लभ जी की कृपा से जीवन प्रकाशित होता है।",
        "🙏 जहाँ भक्ति है, वहीं शांति है।",
        "✨ हरि स्मरण ही जीवन का सबसे बड़ा धन है।",
        "🌼 मन को राधा नाम में स्थिर करो।"
    ];

    const today = new Date().getDate();

    const quoteIndex = today % quotes.length;

    document.getElementById("quoteText").innerText =
        quotes[quoteIndex];

};