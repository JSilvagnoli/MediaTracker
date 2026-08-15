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
        const cardImg = media.image || "./No_Image_Available.jpg";
        const userRating = media.personal_rating || 0;

        card.innerHTML = `
            <button type="button" class="favoriteBtn">${favoriteIcon}</button>
            <h1>${media.title}</h1>
            <img src="${cardImg}">
            <h2>Release Date: ${media.release_date}</h2>
            <p>${media.description}</p>
            <h2>Rating: ${media.rating}</h2>
            <label for="rating">Your Rating (0-10):</label>
            <input class="personalRating" type="number" id="rating" name="rating" min="0" max="10" value="${userRating}" step="1">
            <label for="completionStatus">Completion Status:</label>
            <select class="completionStatus" name="completionStatus">
                <option value="not started">Not Started</option>
                <option value="in progress">In Progress</option>
                <option value="completed">Completed</option>
            </select>
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

        const completionStatus = card.querySelector(".completionStatus");
        completionStatus.value = media.completion_status;

        completionStatus.addEventListener("change", function(event) {
            media.completion_status = completionStatus.value;

            updateCompletionStatus(media);
        });

        const rating = card.querySelector(".personalRating");

        rating.addEventListener("change", function(event) {
            media.personal_rating = rating.value;

            updatePersonalRating(media);
        });

        container.appendChild(card);
    });     
}

async function updateFavoriteStatus(media){
    const response = await fetch(
        "http://127.0.0.1:8000/updateFavoriteStatus", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(media)
    });
}

async function updateCompletionStatus(media){
    const response = await fetch(
        "http://127.0.0.1:8000/updateCompletionStatus", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(media)
    });
}

async function updatePersonalRating(media){
    console.log(media);
    const response = await fetch(
        "http://127.0.0.1:8000/updatePersonalRating", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(media)
    });
}