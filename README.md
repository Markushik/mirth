<div align="center">
# Mirth
🌸 An elegant order processing system based on **event-driven architecture (EDA) with modular microservices**
</div>

## ✨ Features

## 📦 Installation
<div>
### 🦭 Podman
This Podman image published on Docker Hub.

### ❄️ Nix

### Default
`1` Clone the repository
</div>


## 🏛️ Architecture
```mermaid
  graph TD;
    User --> Bot;
    User --> WebApp;
    Bot --> NATS;
    WebApp --> NATS;
    NATS --> Database;
```
