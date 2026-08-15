document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();
    getInput();
});

document.getElementById("type").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        getInput();
    }
});

let selectedCard = null;

const popup = document.getElementById("confirmation");
const confirmBtn = document.getElementById("confirm");
const denyBtn = document.getElementById("deny");

confirmBtn.addEventListener("click", confirmButton);
denyBtn.addEventListener("click", denyButton);

async function getInput(){
    var input = document.getElementById("input");
    var dropdown = document.getElementById("type");

    const mediaToFind = input.value;
    const mediaType = dropdown.value;

    const response = await fetch(
        "http://127.0.0.1:8000/search?media_to_find=" 
        + encodeURIComponent(mediaToFind) 
        + "&media_type="
        + encodeURIComponent(mediaType)
    );
    
    const data = await response.json();

    const container = document.getElementById("results");

    data.forEach(media => {
        const card = document.createElement("div");

        const data = {
            id: media.id,
            title: media.title,
            description: media.description,
            releaseDate: media.release_date,
            rating: media.rating,
            image: media.image,
            type: media.type,
            dateAdded: ""
        };
        
        Object.entries(data).forEach(([key, value]) => {
            card.dataset[key] = value;
        });

        card.innerHTML = `
            <h1>${media.title}</h1>
            <img src="${media.image}">
            <h2>Release Date: ${media.release_date}</h2>
            <p>${media.description}</p>
            <h2>Rating: ${media.rating}</h2>
        `;

        card.addEventListener("click", () => {
            selectedCard = card;
            popup.showModal();
        });

        container.appendChild(card);
    });      
}

async function confirmButton(){
    const currentDateTime = new Date().toLocaleString();
    selectedCard.dataset.dateAdded = currentDateTime
    const response = await fetch("http://127.0.0.1:8000/save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(selectedCard.dataset)
    });

    popup.close();

    const result = await response.json();
}

function denyButton(){
    popup.close();
}