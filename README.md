# Mirth  
🌸 An elegant order processing system based on **event-driven architecture (EDA) with modular microservices**

## ✨ Features

## 📦 Installation

### 🦭 Podman
This Podman image is published on Docker Hub.

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

### Tree Structure
