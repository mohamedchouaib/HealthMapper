"""
ÉTAPE 1: Point d'entrée du Health Planner Service

LOGIQUE GLOBALE:
- Service REST (FastAPI) qui génère des plans d'itinéraires santé
- Orchestration entre Routing et Naolib
- Scoring et ranking des candidats
- Production d'un fallback normal

PORT: 8001
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import logging
import uuid
from typing import Optional
import os

# ÉTAPE: Importer les modules locaux
# from .models import PlanRequest, PlanResponse
# from .services.planner_service import PlannerService
# from .services.candidate_generator import CandidateGenerator
# from .services.scoring_service import ScoringService

# ÉTAPE: Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ÉTAPE: Initialiser l'application FastAPI
app = FastAPI(
    title="Health Planner Service",
    description="Service de planification d'itinéraires santé",
    version="1.0.0"
)

# ÉTAPE: Middleware pour logging et requestId
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    """
    LOGIQUE:
    - Extraire X-Request-Id du header ou générer un nouveau
    - Logger chaque requête avec requestId
    - Propager requestId aux services appelés
    - Logger le temps de réponse
    """
    # TODO: Implémenter
    pass


# ÉTAPE: Endpoint de santé
@app.get("/health")
async def health_check():
    """
    LOGIQUE:
    - Vérifier que le service est opérationnel
    - Vérifier la connexion aux services externes (Routing, Naolib)
    - Retourner le statut
    """
    # TODO: Implémenter
    return {"status": "healthy", "service": "health-planner"}


# ÉTAPE: Endpoint principal - POST /plan
@app.post("/plan")
async def create_health_plan(request: Request):
    """
    ÉTAPE PRINCIPALE: Génération du plan de santé
    
    LOGIQUE MÉTIER:
    1. Recevoir et valider la requête
    2. Générer les candidats (A, B, C types)
    3. Scorer chaque candidat
    4. Sélectionner le meilleur
    5. Générer le fallback normal
    6. Construire la réponse
    
    INPUT:
    - origin, destination, departureTime
    - goals (walkMinutes, bikeMinutes)
    - constraints (maxTime, maxDetour)
    - preferences
    
    OUTPUT:
    - recommendedPlan
    - alternatives (2-3 plans)
    - fallbackPlan
    - explanation
    - evaluationMetrics
    """
    
    # ÉTAPE 1.1: Extraire requestId
    # - Depuis header X-Request-Id
    # - Logger: "Received plan request with requestId={}"
    
    # ÉTAPE 1.2: Parser et valider le body
    # - Utiliser Pydantic pour validation
    # - Vérifier origin/destination présents
    # - Vérifier walkMinutes > 0
    # - Si invalide, raise HTTPException(400)
    
    # ÉTAPE 1.3: Appeler le service de génération de candidats
    # - Passer à CandidateGenerator
    # - Obtenir liste de candidats (plans possibles)
    
    # ÉTAPE 1.4: Scorer les candidats
    # - Passer à ScoringService
    # - Trier par score décroissant
    # - Conserver Top 3-4
    
    # ÉTAPE 1.5: Sélectionner le meilleur
    # - candidats[0] = recommendedPlan
    # - candidats[1:3] = alternatives
    
    # ÉTAPE 1.6: Générer le fallback normal
    # - Appeler Routing pour itinéraire standard
    # - Sans marche additionnelle
    
    # ÉTAPE 1.7: Construire explanation
    # - Texte explicatif du choix
    # - Ex: "Plan avec waypoint au parking X, ajoute 12min de marche"
    
    # ÉTAPE 1.8: Calculer evaluationMetrics
    # - walkGoalAchieved
    # - totalDetourMinutes
    # - score
    
    # ÉTAPE 1.9: Logger et retourner
    # - Logger: "Generated plan with {} alternatives"
    # - Retourner PlanResponse
    
    # TODO: Implémenter
    pass


# ÉTAPE: Endpoint de test - GET /plans/history (optionnel)
@app.get("/plans/history")
async def get_plans_history():
    """
    LOGIQUE:
    - Lire les plans générés depuis data/plans_cache.json
    - Retourner les N derniers plans
    - Utile pour debug/monitoring
    """
    # TODO: Implémenter
    pass


if __name__ == "__main__":
    import uvicorn
    # ÉTAPE: Lancer le serveur
    # - Port 8001
    # - Host 0.0.0.0
    # - Reload en dev
    uvicorn.run(app, host="0.0.0.0", port=8001)
