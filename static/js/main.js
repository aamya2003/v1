const rightNavImg = document.querySelector('.lis-it-small img');
const asideBa = document.querySelector('.ba');
const sec = document.querySelector('.bb');

rightNavImg.addEventListener('click', () => {
    if (asideBa.style.width == "") {

        asideBa.style.opacity = "100"
        asideBa.style.width = "25%"
        rightNavImg.src = "../static/imgs/close-list.png"

        console.log(asideBa.style.width)
    }
    else if (asideBa.style.width == "25%") {

        asideBa.style.width = ""
        asideBa.style.opacity = "0"
        rightNavImg.src = "../static/imgs/list-img.png"
        console.log(asideBa.style.width)
    }
});

document.addEventListener("click", function (event) {
    const isClickInsideBA = asideBa.contains(event.target);
    const isClickInsideImg = rightNavImg.contains(event.target)

    if (!isClickInsideBA & !isClickInsideImg) {
        asideBa.style.width = ""
        asideBa.style.opacity = "0"
        rightNavImg.src = "../static/imgs/list-img.png"
    }

    // if (asideBa.style.width == "25%") {

    //     if (!isClickInsideImg) {
    //         document.style.pointerEevents = "none"
    //     }
    // }
});

// sec.addEventListener("copy", () => {
//     console.log(true)
//     sec.style.color = "red"
// })

// rightNavImg.addEventListener('mouseleave', () => {
//     asideBa.style.width = "0%"
//     asideBa.style.opacity = "0"
// });



const sentences = [
    "My name is Ahmed Asaad",
    "I am a developer",
    "I'm an Engineer",
    "I am a programmer"
];

const textElement = document.getElementById("text");
let currentIndex = 0;
let currentSentence = "";
let currentLetterIndex = 0;
let delay = 100; // Initial delay is 500 milliseconds (0.5 seconds)

function writeLetters() {
    if (currentIndex === sentences.length) {

        currentIndex = 0; // Start again from the first sentence
        // delay += 100; // Increase the delay for each letter by 50 milliseconds
    }

    currentSentence = sentences[currentIndex];


    if (currentLetterIndex < currentSentence.length) {
        textElement.textContent += currentSentence.charAt(currentLetterIndex);
        currentLetterIndex++;
        setTimeout(writeLetters, delay); // Call writeLetters function recursively with the delay
    } else {
        setTimeout(eraseLetters, 2000); // Wait 1.5 seconds before erasing the sentence
    }
}

function eraseLetters() {
    if (currentLetterIndex > 0) {
        textElement.textContent = currentSentence.slice(0, currentLetterIndex - 1);
        currentLetterIndex--;
        setTimeout(eraseLetters, delay); // Call eraseLetters function recursively with the delay
    } else {
        currentIndex++; // Move to the next sentence
        setTimeout(writeLetters, 200); // Wait 1 second before writing the next sentence
    }
}

// Start the writer effect
setTimeout(writeLetters, 200); // Wait 1 second before starting the effect