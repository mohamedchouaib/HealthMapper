"""
ÉTAPE 1: Naolib Mobility Service - Données de mobilité Nantes

LOGIQUE GLOBALE:
- Service REST pour accéder aux données Naolib (API mobilité Nantes)
- Fournit les parkings vélos, leur capacité, disponibilité
- Normalise les données vers un format interne
- Cache les données pour réduire les appels API

PORT: 8003
"""

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
import logging
import os
from typing import Optional, List
from datetime import datetime, timedelta

# ÉTAPE: Importer les modules locaux
# from .models import BikeParking, BikeParkingList
# from .services.naolib_adapter import NaolibAdapter
# from .cache import NaolibCache

# ÉTAPE: Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ÉTAPE: Initialiser l'application FastAPI
app = FastAPI(
    title="Naolib Mobility Service",
    description="Service de données de mobilité Nantes (parkings vélos)",
    version="1.0.0"
)

# ÉTAPE: Configuration
NAOLIB_API_KEY = os.getenv("NAOLIB_API_KEY", "")
CACHE_TTL_SECONDS = 60  # Cache de 60 secondes


# ÉTAPE: Middleware pour requestId
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    """
    LOGIQUE:
    - Extraire ou générer X-Request-Id
    - Logger chaque requête
    """
    # TODO: Implémenter
    pass


# ÉTAPE: Endpoint de santé
@app.get("/health")
async def health_check():
    """
    LOGIQUE:
    - Vérifier que le service est opérationnel
    - Optionnel: Tester l'API Naolib
    """
    return {"status": "healthy", "service": "naolib-mobility"}


# ÉTAPE: Endpoint principal - GET /bike-parkings/nearby
@app.get("/bike-parkings/nearby")
async def get_nearby_bike_parkings(
    lat: float = Query(..., description="Latitude du point de recherche"),
    lon: float = Query(..., description="Longitude du point de recherche"),
    radius: int = Query(1000, ge=100, le=5000, description="Rayon de recherche en mètres"),
    min_available: int = Query(0, ge=0, description="Nombre minimum de places disponibles"),
    request: Request = None
):
    """
    ÉTAPE PRINCIPALE: Obtenir les parkings vélos à proximité
    
    LOGIQUE:
    1. Vérifier le cache
    2. Si cache valide, retourner depuis cache
    3. Sinon, appeler l'API Naolib
    4. Filtrer par distance (rayon)
    5. Filtrer par disponibilité
    6. Trier par distance
    7. Mettre en cache
    8. Retourner la liste
    
    INPUT:
    - lat, lon: Point de recherche
    - radius: Rayon en mètres
    - min_available: Places disponibles minimales
    
    OUTPUT:
    - Liste de parkings vélos avec:
      * id, name, lat, lon
      * capacity, available
      * distance (depuis le point de recherche)
      * status (open/closed)
      * updated_at
    """
    
    # ÉTAPE 1.1: Extraire requestId
    # - request_id = request.headers.get('X-Request-Id')
    # - Logger: "Searching bike parkings: lat={}, lon={}, radius={}"
    
    # ÉTAPE 1.2: Vérifier le cache
    # - cache_key = f"parkings_{lat}_{lon}_{radius}"
    # - cached = cache.get(cache_key)
    # - Si valide (timestamp < 60s), retourner cached
    
    # ÉTAPE 1.3: Appeler l'API Naolib
    # - _fetch_naolib_parkings()
    # - Obtenir tous les parkings vélos de Nantes
    
    # ÉTAPE 1.4: Calculer les distances
    # - Pour chaque parking:
    #   * Calculer distance avec formule haversine
    #   * Ajouter champ 'distance_meters'
    
    # ÉTAPE 1.5: Filtrer par rayon
    # - Garder seulement ceux avec distance <= radius
    
    # ÉTAPE 1.6: Filtrer par disponibilité
    # - Si min_available > 0:
    #   * Garder seulement ceux avec available >= min_available
    
    # ÉTAPE 1.7: Trier par distance
    # - parkings.sort(key=lambda x: x['distance_meters'])
    
    # ÉTAPE 1.8: Mettre en cache
    # - cache.set(cache_key, parkings, ttl=CACHE_TTL_SECONDS)
    
    # ÉTAPE 1.9: Logger et retourner
    # - Logger: "Found {} bike parkings within {}m"
    # - Retourner la liste
    
    # TODO: Implémenter
    pass


# ÉTAPE: Endpoint détail - GET /bike-parkings/{parking_id}
@app.get("/bike-parkings/{parking_id}")
async def get_bike_parking_detail(
    parking_id: str,
    request: Request = None
):
    """
    ÉTAPE: Obtenir les détails d'un parking spécifique
    
    LOGIQUE:
    - Appeler l'API Naolib pour ce parking
    - Retourner les infos détaillées
    - Utile pour vérifier avant de recommander
    """
    
    # ÉTAPE 1: Extraire requestId
    # ÉTAPE 2: Appeler _fetch_naolib_parking_detail(parking_id)
    # ÉTAPE 3: Normaliser et retourner
    
    # TODO: Implémenter
    pass


async def _fetch_naolib_parkings() -> List[dict]:
    """
    ÉTAPE 2.1: Appeler l'API Naolib pour obtenir tous les parkings
    
    LOGIQUE:
    - URL de l'API Naolib (données open data Nantes)
    - Endpoint: /api/records/1.0/search/
    - Dataset: parkings vélos Nantes
    - Parser la réponse JSON
    - Normaliser vers notre format
    
    API NAOLIB:
    - Base URL: https://data.nantesmetropole.fr
    - Authentification: API key (si nécessaire)
    - Format: JSON avec records[]
    """
    
    # ÉTAPE 2.1.1: Construire l'URL de requête
    # - base_url = "https://data.nantesmetropole.fr/api/records/1.0/search/"
    # - params:
    #   * dataset: "244400404_parkings-velos-nantes-metropole"
    #   * rows: 100 (ou -1 pour tout)
    #   * apikey: NAOLIB_API_KEY (si requis)
    
    # ÉTAPE 2.1.2: Envoyer la requête
    # - async with httpx.AsyncClient() as client:
    # - response = await client.get(url, params=params, timeout=3.0)
    
    # ÉTAPE 2.1.3: Parser la réponse
    # - data = response.json()
    # - records = data['records']
    
    # ÉTAPE 2.1.4: Normaliser chaque record
    # - Pour chaque record:
    #   * Extraire fields
    #   * Normaliser vers notre format:
    #     {
    #       'id': record['recordid'],
    #       'name': fields['nom'] ou fields['libelle'],
    #       'lat': fields['geo_point_2d'][0],
    #       'lon': fields['geo_point_2d'][1],
    #       'capacity': fields['capacite'] ou 0,
    #       'available': fields['disponibilite'] ou capacity,
    #       'status': 'open' si disponible sinon 'closed',
    #       'updated_at': datetime.now().isoformat()
    #     }
    
    # ÉTAPE 2.1.5: Gestion des erreurs
    # - Si timeout ou erreur HTTP, logger et raise HTTPException
    # - Si format JSON invalide, logger et retourner []
    
    # ÉTAPE 2.1.6: Logger et retourner
    # - Logger: "Fetched {} parkings from Naolib"
    # - return parkings_list
    
    # TODO: Implémenter
    pass


def _calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    ÉTAPE HELPER: Calculer la distance entre 2 points (Haversine)
    
    LOGIQUE:
    - Formule Haversine pour distance géodésique
    - Retourner distance en mètres
    
    FORMULE:
    - a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
    - c = 2 * atan2(√a, √(1−a))
    - d = R * c  (R = 6371 km)
    """
    
    # ÉTAPE: Implémenter Haversine
    # - Convertir degrés en radians
    # - Appliquer la formule
    # - Retourner distance_meters
    
    # TODO: Implémenter
    pass


@app.get("/bike-parkings/all")
async def get_all_bike_parkings(request: Request = None):
    """
    ÉTAPE BONUS: Obtenir tous les parkings (pour debug/monitoring)
    
    LOGIQUE:
    - Appeler _fetch_naolib_parkings()
    - Retourner la liste complète
    - Pas de filtre
    """
    
    # TODO: Implémenter
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
