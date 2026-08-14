// ===== STATE =====
let currentMealTime = null;

// ===== MEAL TIME BOUNDARIES (24h) =====
const MEAL_HOURS = {
    breakfast: 6,
    brunch: 11,
    lunch: 13,
    snack: 16,
    dinner: 19,
    midnight: 22
};

// ===== INIT =====
document.addEventListener("DOMContentLoaded", () => {
    startClock();
    fetchRecipe();
    setupMealButtons();
    startCountdown();
});

// ===== LIVE CLOCK =====
function startClock() {
    function updateClock() {
        const now = new Date();
        let hours = now.getHours();
        const minutes = String(now.getMinutes()).padStart(2, "0");
        const seconds = String(now.getSeconds()).padStart(2, "0");
        const ampm = hours >= 12 ? "PM" : "AM";
        hours = hours % 12 || 12;
        document.getElementById("liveTime").textContent =
            `${String(hours).padStart(2, "0")}:${minutes}:${seconds} ${ampm}`;
    }
    updateClock();
    setInterval(updateClock, 1000);
}

// ===== FETCH RECIPE FROM FLASK =====
async function fetchRecipe(mealTime = null) {
    showLoading();

    try {
        const url = mealTime ? `/api/recipe/${mealTime}` : "/api/recipe";
        const response = await fetch(url);
        const data = await response.json();

        currentMealTime = data.meal_time;
        updateMealBadge(data.meal_time);
        renderRecipe(data.recipe);
        setActiveButton(data.meal_time);
    } catch (error) {
        showError();
    }
}

// ===== RENDER RECIPE =====
function renderRecipe(recipe) {
    document.getElementById("recipeEmoji").textContent = recipe.emoji;
    document.getElementById("recipeName").textContent = recipe.meal;
    document.getElementById("timeRange").textContent = `⏰ ${recipe.time_range}`;

    // Ingredients
    const ingredientsList = document.getElementById("ingredientsList");
    ingredientsList.innerHTML = recipe.ingredients
        .map(item => `<li>${item}</li>`)
        .join("");

    // Steps
    const stepsList = document.getElementById("stepsList");
    stepsList.innerHTML = recipe.steps
        .map(step => `<li>${step}</li>`)
        .join("");

    // Fun Fact
    document.getElementById("funFact").textContent = `💡 Fun Fact: ${recipe.fun_fact}`;

    hideLoading();

    // Animate in
    const content = document.getElementById("recipeContent");
    content.classList.remove("fade-in");
    void content.offsetWidth; // reflow trick to restart animation
    content.classList.add("fade-in");
}

// ===== MEAL BADGE =====
function updateMealBadge(mealTime) {
    const labels = {
        breakfast: "🌅 Breakfast Time",
        brunch: "☀️ Brunch Time",
        lunch: "🌞 Lunch Time",
        snack: "🌆 Snack Time",
        dinner: "🌙 Dinner Time",
        midnight: "🌃 Midnight Munchies"
    };
    document.getElementById("mealBadge").textContent = labels[mealTime] || mealTime;
}

// ===== MEAL BUTTONS =====
function setupMealButtons() {
    document.querySelectorAll(".meal-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            const meal = btn.dataset.meal;
            fetchRecipe(meal);
        });
    });

    document.getElementById("refreshBtn").addEventListener("click", () => {
        fetchRecipe(currentMealTime);
    });
}

function setActiveButton(mealTime) {
    document.querySelectorAll(".meal-btn").forEach(btn => {
        btn.classList.toggle("active", btn.dataset.meal === mealTime);
    });
}

// ===== LOADING STATES =====
function showLoading() {
    document.getElementById("loadingSpinner").style.display = "flex";
    document.getElementById("recipeContent").style.display = "none";
}

function hideLoading() {
    document.getElementById("loadingSpinner").style.display = "none";
    document.getElementById("recipeContent").style.display = "block";
}

function showError() {
    document.getElementById("loadingSpinner").innerHTML =
        `<p style="color:#ff6b6b; font-size:1.1rem;">😕 Oops! Couldn't load recipe.<br>Make sure Flask is running!</p>`;
    document.getElementById("loadingSpinner").style.display = "flex";
}

// ===== COUNTDOWN TO NEXT MEAL =====
function startCountdown() {
    function updateCountdown() {
        const now = new Date();
        const currentHour = now.getHours();

        // Find next meal hour
        const mealHours = Object.values(MEAL_HOURS).sort((a, b) => a - b);
        let nextHour = mealHours.find(h => h > currentHour);
        if (!nextHour) nextHour = mealHours[0] + 24; // wrap to next day

        const nextMealTime = new Date(now);
        nextMealTime.setHours(nextHour, 0, 0, 0);
        if (nextHour > 23) {
            nextMealTime.setDate(nextMealTime.getDate() + 1);
            nextMealTime.setHours(nextHour - 24, 0, 0, 0);
        }

        const diff = nextMealTime - now;
        const h = String(Math.floor(diff / 3600000)).padStart(2, "0");
        const m = String(Math.floor((diff % 3600000) / 60000)).padStart(2, "0");
        const s = String(Math.floor((diff % 60000) / 1000)).padStart(2, "0");

        document.getElementById("countdown").textContent = `${h}:${m}:${s}`;
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
}
