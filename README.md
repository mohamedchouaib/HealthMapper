# Health Route - Système d'itinéraire santé

## Architecture

Ce projet est composé de 5 microservices :

1. **GraphQL Gateway** (Spring Boot) - Port 8080
   - Point d'entrée unique pour le client
   - Orchestration et décision finale (fallback météo)

2. **Health Planner Service** (FastAPI) - Port 8001
   - Cerveau de la planification d'itinéraires santé
   - Génération et scoring des candidats

3. **Routing Service** (FastAPI) - Port 8002
   - Calcul d'itinéraires (marche/vélo/transit)

4. **Naolib Mobility Service** (FastAPI) - Port 8003
   - Données de mobilité Nantes (parkings vélos)

5. **Weather Service** (FastAPI) - Port 8004
   - Décision météo et alertes

## Prérequis

- Docker et Docker Compose installés
- Clés API pour les services externes (optionnel pour le développement)

## Démarrage rapide

### 1. Configuration de l'environnement

```bash
# Se placer dans le répertoire du projet
cd /home/medchab/Documents/3A_IMT/hackthon

# Copier le fichier d'environnement
cp .env.example .env

# Éditer .env avec vos clés API (optionnel pour dev)
nano .env
```

**Clés API nécessaires** (dans `.env`) :
- `ROUTING_API_KEY` - Pour l'API de routing externe (ex: GraphHopper, OSRM)
- `NAOLIB_API_KEY` - Pour l'API Naolib (données Nantes)
- `WEATHER_API_KEY` - Pour l'API météo (ex: OpenWeatherMap)

### 2. Lancement avec Docker Compose

```bash
# Construire et lancer tous les services
docker-compose up --build

# Ou en mode détaché (background)
docker-compose up -d --build

# Voir les logs
docker-compose logs -f

# Voir les logs d'un seul service
docker-compose logs -f health-planner
```

### 3. Vérification

```bash
# Vérifier que tous les conteneurs sont démarrés
docker-compose ps

# Tester les endpoints de santé
curl http://localhost:8080/health  # GraphQL Gateway (si implémenté)
curl http://localhost:8001/health  # Health Planner
curl http://localhost:8002/health  # Routing Service
curl http://localhost:8003/health  # Naolib Service
curl http://localhost:8004/health  # Weather Service
```

### 4. Arrêt des services

```bash
# Arrêter les services
docker-compose down

# Arrêter et supprimer les volumes
docker-compose down -v
```

## Endpoints

### Interface GraphQL
- **GraphQL Gateway**: http://localhost:8080/graphql
- **GraphiQL** (interface de test): http://localhost:8080/graphiql

### Documentation API (Swagger/OpenAPI)
- **Health Planner**: http://localhost:8001/docs
- **Routing Service**: http://localhost:8002/docs
- **Naolib Service**: http://localhost:8003/docs
- **Weather Service**: http://localhost:8004/docs

### Exemple de requête GraphQL

```graphql
query {
  healthPlan(input: {
    origin: { lat: 47.2184, lon: -1.5536 }
    destination: { lat: 47.2173, lon: -1.5534 }
    goals: { walkMinutes: 20 }
    constraints: { maxTotalTimeMinutes: 60 }
    preferences: { avoidRain: "strict" }
  }) {
    selectedPlan {
      planType
      totalDurationMinutes
      activity {
        walkMinutes
        bikeMinutes
      }
    }
    weatherSummary {
      decision
      temperature
    }
    alerts {
      level
      message
    }
  }
}
```

## Développement

### Structure des fichiers

```
hackthon/
├── docker-compose.yml          # Orchestration des services
├── .env.example                # Template de configuration
├── README.md                   # Ce fichier
└── services/
    ├── graphql-gateway/        # Spring Boot (Java)
    │   ├── Dockerfile
    │   ├── pom.xml
    │   └── src/
    ├── health-planner/         # FastAPI (Python)
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   ├── app/
    │   └── data/               # Persistance JSON
    ├── routing-service/        # FastAPI (Python)
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── app/
    ├── naolib-service/         # FastAPI (Python)
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   ├── app/
    │   └── data/               # Cache JSON
    └── weather-service/        # FastAPI (Python)
        ├── Dockerfile
        ├── requirements.txt
        ├── app/
        └── data/               # Cache JSON
```

### Développement local (sans Docker)

#### GraphQL Gateway (Java)
```bash
cd services/graphql-gateway
mvn clean install
mvn spring-boot:run
```

#### Services Python (exemple: Health Planner)
```bash
cd services/health-planner
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

## Données persistées

Les services utilisent des fichiers JSON pour la persistance :
- `/services/health-planner/data/` - Cache des plans générés
- `/services/naolib-service/data/` - Cache des données mobilité
- `/services/weather-service/data/` - Cache des données météo

## Dépannage

### Problème: Port déjà utilisé
```bash
# Vérifier quels ports sont utilisés
netstat -tuln | grep -E '8080|8001|8002|8003|8004'

# Arrêter un service spécifique
docker-compose stop health-planner
```

### Problème: Erreur de build
```bash
# Nettoyer et rebuild
docker-compose down -v
docker system prune -a
docker-compose up --build
```

### Problème: Logs d'erreur
```bash
# Voir les logs détaillés d'un service
docker-compose logs -f --tail=100 health-planner

# Voir les logs de tous les services
docker-compose logs -f
```

### Problème: Conteneur qui redémarre en boucle
```bash
# Vérifier l'état
docker-compose ps

# Inspecter le conteneur
docker inspect <container_id>

# Voir pourquoi il crash
docker-compose logs <service_name>
```

## État d'implémentation

⚠️ **Note**: Les fichiers contiennent la **structure et la logique en commentaires**. 
L'implémentation du code doit être réalisée selon les étapes définies.

### Fichiers avec étapes détaillées (TODO: implémenter)
- ✅ Architecture complète définie
- ✅ Docker & docker-compose configurés
- ✅ Schémas GraphQL et modèles de données
- ⏳ Code Java (GraphQL Gateway) - Étapes en commentaires
- ⏳ Code Python (4 services FastAPI) - Étapes en commentaires

### Prochaines étapes
1. Implémenter le code selon les étapes commentées
2. Configurer les clés API dans `.env`
3. Tester chaque service individuellement
4. Tester l'orchestration complète
5. Ajuster les timeouts et paramètres

## Contributeurs

Projet hackathon IMT 3A - Janvier 2026
