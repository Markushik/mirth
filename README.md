<div style="text-align: center;">
# Mirth
🌸 An elegant order processing system based on **event-driven architecture (EDA) with modular microservices**
</div>

## ✨ Features

## 📦 Installation
### 🦭 Podman
<div>
This Podman image published on Docker Hub.
</div>
### ❄️ Nix
### Default
`1` Clone the repository


## 🏛️ Architecture
```mermaid
  graph TD;
    User --> Bot;
    User --> WebApp;
    Bot --> NATS;
    WebApp --> NATS;
    NATS --> Database;
```
