<div align="center">

# Mirth
🌸 An elegant order processing system based on **event-driven architecture (EDA) with modular microservices**

</div>

## ✨ Features

## 📦 Installation

## 🏛️ Architecture
```mermaid
  graph TD;
    User --> Bot;
    User --> WebApp;
    Bot --> NATS;
    WebApp --> NATS;
    NATS --> Database;
```
