async function getData(){
    const params = new URLSearchParams(window.location.search);
    const type = params.get("type");
    console.log(type);
    const response = await fetch(
        "http://127.0.0.1:8000/media?media_type="
        + encodeURIComponent(type)
    );

    if (response.status === 200){
        return response.json();
    }
}

const popup = document.getElementById("confirmation");

export async function displayData(){
    const data = await getData();

    const container = document.getElementById("results");

    data.forEach(media => {
        const card = document.createElement("div");

        const cardData = {
            id: media.id,
            title: media.title,
            description: media.description,
            releaseDate: media.release_date,
            rating: media.rating,
            image: media.image,
            type: media.type
        };
        
        Object.entries(cardData).forEach(([key, value]) => {
            card.dataset[key] = value;
        });

        card.innerHTML = `
            <button class="favoriteBtn">☆</button>
            <h1>${media.title}</h1>
            <img src="${media.image}">
            <h2>Release Date: ${media.release_date}</h2>
            <p>${media.description}</p>
            <h2>Rating: ${media.rating}</h2>
        `;

        const favoriteButton = card.querySelector(".favoriteBtn");

        favoriteButton.addEventListener("click", () => {
            if (favoriteButton.textContent === "☆") {
                favoriteButton.textContent = "★";
            }
            else favoriteButton.textContent = "☆";
        });

        container.appendChild(card);
    });     
}