# 🍽️ What's Cooking Now?

> **A time-based recipe web app** that suggests the perfect recipe based on your current time of day — built with Flask, HTML, CSS & JS, containerized with Docker, and deployed on **Amazon Lightsail** via **GitHub Actions CI/CD**.

<img width="1360" height="633" alt="image" src="https://github.com/user-attachments/assets/1cbd7c31-f58f-4733-b351-ef34a1e360d4" />
<img width="1363" height="618" alt="image" src="https://github.com/user-attachments/assets/d2b898b7-79a2-4a45-9488-35c156d934f1" />
<img width="1366" height="640" alt="image" src="https://github.com/user-attachments/assets/c34f3d54-cf9e-4164-9662-40bf3e265fe8" />
<img width="1365" height="640" alt="image" src="https://github.com/user-attachments/assets/53cfe6f3-2796-40f6-a655-dc12e562aa5d" />
<img width="1366" height="639" alt="image" src="https://github.com/user-attachments/assets/47e646f3-d894-4a2d-a571-9010a2befb96" />
<img width="1353" height="630" alt="image" src="https://github.com/user-attachments/assets/45b71259-2ea6-4011-97c6-cafb0d9325e3" />

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![AWS Lightsail](https://img.shields.io/badge/AWS-Lightsail-FF9900?logo=amazonaws)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions)

---

## 📸 Preview

| Time of Day | Recipe Suggested |
|---|---|
| 🌅 6AM – 11AM | Avocado Toast with Poached Eggs |
| ☀️ 11AM – 1PM | Fluffy Banana Pancakes |
| 🌞 1PM – 4PM | Grilled Chicken Caesar Wrap |
| 🌆 4PM – 7PM | Honey Garlic Popcorn |
| 🌙 7PM – 10PM | Creamy Tuscan Garlic Pasta |
| 🌃 10PM – 6AM | Midnight Nutella Mug Cake |

---

## 📁 Project Structure

```
whats-cooking-now/
├── app.py                     # Flask backend — API routes & recipe logic
├── Dockerfile                 # Docker container configuration
├── requirements.txt           # Python dependencies
├── static/
│   ├── index.html             # Frontend HTML
│   ├── style.css              # Styling & animations
│   └── script.js              # Frontend logic & API calls
└── .github/
    └── workflows/
        └── deploy.yml          # GitHub Actions CI/CD pipeline
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.11** | Backend language |
| **Flask 3.0.3** | Web framework & REST API |
| **HTML5** | Frontend structure |
| **CSS3** | Styling, animations, responsive design |
| **JavaScript (Vanilla)** | Live clock, API calls, countdown timer |
| **Docker** | Containerization |
| **Amazon Lightsail** | Cloud hosting (container service) |
| **GitHub Actions** | CI/CD pipeline — auto deploy on push |
| **AWS IAM** | Secure access management for deployment |

---

## 🚀 Quick Start — Run Locally

### Prerequisites
- Python 3.11+
- pip
- Docker (optional, for container testing)
- Git

### Option 1 — Run with Python directly

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/whats-cooking-now.git
cd whats-cooking-now

# 2. Install dependencies
pip install flask

# 3. Start Flask
python app.py

# 4. Open in browser
# → http://localhost:5000
```

### Option 2 — Run with Docker

```bash
# 1. Build the Docker image
docker build -t whats-cooking-now .

# 2. Run the container
docker run -p 5000:5000 whats-cooking-now

# 3. Open in browser
# → http://localhost:5000
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serves the frontend app |
| GET | `/api/recipe` | Returns recipe based on current time |
| GET | `/api/recipe/breakfast` | Returns breakfast recipe |
| GET | `/api/recipe/brunch` | Returns brunch recipe |
| GET | `/api/recipe/lunch` | Returns lunch recipe |
| GET | `/api/recipe/snack` | Returns snack recipe |
| GET | `/api/recipe/dinner` | Returns dinner recipe |
| GET | `/api/recipe/midnight` | Returns midnight recipe |

### Sample Response

```json
{
  "meal_time": "dinner",
  "current_hour": 20,
  "recipe": {
    "emoji": "🌙",
    "meal": "Creamy Tuscan Garlic Pasta 🍝🧄",
    "time_range": "7 PM – 10 PM",
    "ingredients": [
      "300g fettuccine pasta",
      "3 cloves garlic",
      "1 cup heavy cream",
      "½ cup sun-dried tomatoes",
      "2 cups spinach",
      "Parmesan cheese",
      "Olive oil, salt, pepper"
    ],
    "steps": [
      "Cook pasta according to package instructions.",
      "Sauté garlic in olive oil for 2 minutes.",
      "..."
    ],
    "fun_fact": "Italy has over 350 different pasta shapes! 🇮🇹"
  }
}
```

---

## ☁️ AWS Services Used

### 1. 🟠 Amazon Lightsail — Container Service

**What it is:** Amazon Lightsail is AWS's simplified cloud platform designed for developers who need to deploy apps quickly without managing complex infrastructure. It bundles compute, networking, and storage into simple, predictable monthly pricing.

**What we used:**
- Lightsail Container Service — a fully managed environment to run Docker containers
- Power: `nano` (512MB RAM, 0.25 vCPU) — perfect for small apps
- Scale: 1 node
- Auto-generated HTTPS public endpoint URL

**How it works in this project:**

```
GitHub push → GitHub Actions builds Docker image
           → Pushes image to Lightsail
           → Creates deployment
           → App is live at HTTPS URL
```

**Lightsail Container Service URL format:**

```
https://<service-name>.<random-id>.<region>.cs.amazonlightsail.com
```

**Pricing:**
- Nano plan: ~$7/month
- Billed hourly — delete when not in use to avoid charges
- Console: https://lightsail.aws.amazon.com/ls/webapp/home/containers

---

### 2. 🔐 AWS IAM — Identity and Access Management

**What it is:** AWS IAM lets you securely control who can access your AWS resources and what actions they can perform. It follows the principle of least privilege — give only the permissions needed, nothing more.

**What we used:**
- Created a dedicated IAM user specifically for GitHub Actions
- Attached the `AmazonLightsailFullAccess` policy
- Generated Access Key ID and Secret Access Key for programmatic access

**Why not use root account keys?**

❌ Root account has unlimited access to everything in your AWS account. If leaked, an attacker can delete all your resources, rack up huge bills, or steal data. Always use IAM users with limited permissions.

**IAM User Setup Steps:**
1. Go to IAM Console → Users → Create User
2. Username: `github-actions-lightsail`
3. Select: "Attach policies directly"
4. Attach: `AmazonLightsailFullAccess`
5. Go to user → Security credentials → Create access key
6. Select: "Application running outside AWS"
7. Save the Access Key ID and Secret Access Key — shown only once!

Console: https://console.aws.amazon.com/iam/home#/users

---

### 3. 🐙 GitHub Actions — CI/CD Pipeline

**What it is:** GitHub Actions is a CI/CD (Continuous Integration / Continuous Deployment) platform built into GitHub. It automatically runs workflows when you push code — in our case, it builds and deploys the app to Lightsail on every push to `main`.

**What we used:**
- Workflow file: `.github/workflows/deploy.yml`
- Trigger: Push to `main` branch
- Jobs: Build Docker image → Push to Lightsail → Deploy → Print URL

**Workflow Steps Explained:**

| Step | What it does |
|---|---|
| `actions/checkout@v4` | Pulls your code into the runner |
| `aws-actions/configure-aws-credentials@v4` | Authenticates with AWS using your secrets |
| Install `lightsailctl` | Installs the Lightsail CLI plugin for pushing images |
| `docker build` | Builds your Docker image locally on the runner |
| `create-container-service` | Creates Lightsail service if it doesn't exist yet |
| Wait loop | Polls until service state is READY or RUNNING |
| `push-container-image` | Uploads Docker image to Lightsail |
| `create-container-service-deployment` | Deploys the new image live |
| Print URL | Outputs the live app URL in the logs |

**GitHub Secrets Required:**

| Secret Name | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key |
| `AWS_REGION` | AWS region e.g. `us-east-1` |
| `LIGHTSAIL_SERVICE_NAME` | Your service name e.g. `whats-cooking-now` |

**How to add secrets:**
GitHub Repo → Settings → Secrets and variables → Actions → New repository secret

---

### 4. 🐳 Docker — Containerization

**What it is:** Docker packages your application and all its dependencies into a container — a lightweight, portable unit that runs the same way everywhere: your laptop, a teammate's machine, or AWS.

**Our Dockerfile explained:**

```dockerfile
FROM python:3.11-slim        # Use lightweight Python 3.11 base image

WORKDIR /app                 # Set working directory inside container

COPY requirements.txt .      # Copy dependencies file first (layer caching)
RUN pip install --no-cache-dir -r requirements.txt  # Install dependencies

COPY . .                     # Copy all project files

EXPOSE 5000                  # Tell Docker the app runs on port 5000

CMD ["python", "app.py"]     # Command to start the Flask app
```

**Useful Docker commands:**

```bash
# Build image
docker build -t whats-cooking-now .

# Run container
docker run -p 5000:5000 whats-cooking-now

# Run in background
docker run -d -p 5000:5000 whats-cooking-now

# List running containers
docker ps

# Stop container
docker stop <container-id>

# Remove image
docker rmi whats-cooking-now
```

---

## 🔧 Full Deployment Setup Guide

**Step 1 — Create IAM User**
1. Open IAM Console
2. Create user: `github-actions-lightsail`
3. Attach policy: `AmazonLightsailFullAccess`
4. Create access key → save both keys

**Step 2 — Add GitHub Secrets**
1. Go to your GitHub repo → Settings → Secrets and variables → Actions
2. Add these 4 secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION` (e.g. `us-east-1`)
   - `LIGHTSAIL_SERVICE_NAME` (e.g. `whats-cooking-now`)

**Step 3 — Push to GitHub**

```bash
git init
git add .
git commit -m "Initial commit — What's Cooking Now"
git branch -M main
git remote add origin https://github.com/Santhosh-p653/aws-lightsail.git
git push -u origin main
```

**Step 4 — Watch GitHub Actions Deploy**
1. Go to your repo → Actions tab
2. Watch the workflow run in real time
3. When complete, click the last step "Get App URL"
4. Copy your live HTTPS URL 🎉

**Step 5 — Open Your Live App**

```
https://whats-cooking-now.xxxxxxxx.<region>.cs.amazonlightsail.com
```

---

## 🧪 Testing the API Locally

```bash
# Current time recipe
curl http://localhost:5000/api/recipe

# Specific meal
curl http://localhost:5000/api/recipe/dinner

# Pretty print
curl http://localhost:5000/api/recipe | python -m json.tool

# Test invalid (should return 404)
curl -i http://localhost:5000/api/recipe/pizza
```

---

## 🧹 Cleanup Guide

**Disable (Pause — keeps data, stops compute charges)**

```bash
aws lightsail update-container-service \
  --service-name whats-cooking-now \
  --is-disabled
```

**Full Delete (Permanent — cannot be undone)**

```bash
aws lightsail delete-container-service \
  --service-name whats-cooking-now
```

Or via Console: Lightsail Console → Click service → Three dots menu → Delete

**Full Cleanup Checklist**
- ✅ Delete Lightsail container service
- ✅ Delete IAM user (`github-actions-lightsail`)
- ✅ Remove GitHub repository secrets
- ✅ Delete any unused Lightsail Static IPs
- ✅ Delete any Lightsail snapshots

⚠️ Static IPs are billed even when unattached — always check Lightsail Networking.

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| CSS/JS not loading | Make sure paths are `/static/style.css` and `/static/script.js` |
| 404 on `/api/recipe` | Flask is not running — check `python app.py` |
| Docker build fails | Check `requirements.txt` exists in root folder |
| GitHub Actions fails at AWS step | Verify all 4 GitHub Secrets are set correctly |
| Lightsail service stuck in PENDING | Wait 2–3 minutes, it's provisioning for the first time |
| App URL returns 503 | Service is disabled — re-enable from Lightsail console |

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Built With

- [Flask](https://flask.palletsprojects.com/) — Python web framework
- [Docker](https://www.docker.com/) — Containerization
- [Amazon Lightsail](https://aws.amazon.com/lightsail/) — Cloud hosting
- [GitHub Actions](https://github.com/features/actions) — CI/CD automation
- AWS IAM — Secure access management

---

💡 **Tip:** Star ⭐ this repo if you found it helpful!
