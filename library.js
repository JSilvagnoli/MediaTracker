async function getData(){
    const params = new URLSearchParams(window.location.search);
    const type = params.get("type");
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

        const favoriteIcon = media.favorite_status ? "★" : "☆";
        card.innerHTML = `
            <button type="button" class="favoriteBtn">${favoriteIcon}</button>
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
                media.favorite_status = true;
            }
            else {
                favoriteButton.textContent = "☆";
                media.favorite_status = false;
            }

            updateFavoriteStatus(media);
        });

        container.appendChild(card);
    });     
}

async function updateFavoriteStatus(media){
    console.log(media);
    const response = await fetch(
        "http://127.0.0.1:8000/updateFavoriteStatus", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(media)
    });
}