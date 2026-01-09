"""
ÉTAPE 1: Routing Service - Calcul d'itinéraires

LOGIQUE GLOBALE:
- Service REST pour calculer des itinéraires entre 2 points
- Supporte 3 modes: walk, bike, transit
- Normalise les réponses de l'API de routing externe
- Fournit distance, durée, géométrie

PORT: 8002
"""

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from enum import Enum
import logging
import os
from typing import Optional

# ÉTAPE: Importer les modules locaux
# from .models import RouteRequest, RouteResponse
# from .services.routing_adapter import RoutingAdapter

# ÉTAPE: Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ÉTAPE: Initialiser l'application FastAPI
app = FastAPI(
    title="Routing Service",
    description="Service de calcul d'itinéraires multi-modal",
    version="1.0.0"
)


class TravelMode(str, Enum):
    """Modes de transport supportés"""
    WALK = "walk"
    BIKE = "bike"
    TRANSIT = "transit"


# ÉTAPE: Middleware pour requestId
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    """
    LOGIQUE:
    - Extraire ou générer X-Request-Id
    - Logger chaque requête
    - Mesurer le temps de réponse
    """
    # TODO: Implémenter
    pass


# ÉTAPE: Endpoint de santé
@app.get("/health")
async def health_check():
    """
    LOGIQUE:
    - Vérifier que le service est opérationnel
    - Optionnel: Ping l'API externe de routing
    """
    return {"status": "healthy", "service": "routing"}


# ÉTAPE: Endpoint principal - GET /route
@app.get("/route")
async def get_route(
    mode: TravelMode = Query(..., description="Mode de transport"),
    from_lat: float = Query(..., alias="from_lat", description="Latitude origine"),
    from_lon: float = Query(..., alias="from_lon", description="Longitude origine"),
    to_lat: float = Query(..., description="Latitude destination"),
    to_lon: float = Query(..., description="Longitude destination"),
    time: Optional[str] = Query("now", description="Heure de départ (ISO 8601 ou 'now')"),
    request: Request = None
):
    """
    ÉTAPE PRINCIPALE: Calculer un itinéraire
    
    LOGIQUE:
    1. Valider les paramètres
    2. Extraire requestId
    3. Appeler l'API externe de routing selon le mode
    4. Normaliser la réponse
    5. Calculer les métriques (distance, durée)
    6. Retourner la réponse standardisée
    
    INPUT:
    - mode: walk / bike / transit
    - from_lat, from_lon: Coordonnées origine
    - to_lat, to_lon: Coordonnées destination
    - time: Heure de départ
    
    OUTPUT:
    - distance_km: Distance totale
    - duration_minutes: Durée totale
    - segments: Liste de segments
    - geometry: Polyline (optionnel)
    """
    
    # ÉTAPE 1.1: Extraire requestId
    # - request_id = request.headers.get('X-Request-Id')
    # - Logger: "Routing request: mode={}, from=({},{}), to=({},{})"
    
    # ÉTAPE 1.2: Valider les coordonnées
    # - Vérifier -90 <= lat <= 90
    # - Vérifier -180 <= lon <= 180
    # - Si invalide, raise HTTPException(400)
    
    # ÉTAPE 1.3: Sélectionner l'adaptateur selon le mode
    # - Si mode == WALK: appeler _calculate_walk_route()
    # - Si mode == BIKE: appeler _calculate_bike_route()
    # - Si mode == TRANSIT: appeler _calculate_transit_route()
    
    # ÉTAPE 1.4: Normaliser la réponse
    # - Transformer en format standard
    # - Calculer distance_km et duration_minutes
    # - Construire segments[]
    
    # ÉTAPE 1.5: Logger et retourner
    # - Logger: "Route calculated: {} km, {} minutes"
    # - Retourner JSON
    
    # TODO: Implémenter
    pass


async def _calculate_walk_route(
    from_lat: float,
    from_lon: float,
    to_lat: float,
    to_lon: float,
    time: str,
    request_id: str
) -> dict:
    """
    ÉTAPE 2.1: Calcul d'itinéraire à pied
    
    LOGIQUE:
    - Appeler l'API externe (ex: OSRM, GraphHopper, Google Directions)
    - Mode: foot/walking
    - Parser la réponse
    - Extraire: distance, durée, steps, geometry
    
    API EXTERNE SUGGÉRÉE:
    - OSRM (gratuit, self-hosted possible)
    - GraphHopper (gratuit avec limites)
    - OpenRouteService
    """
    
    # ÉTAPE 2.1.1: Construire la requête API
    # - URL de l'API externe
    # - Paramètres: coordinates, profile=foot
    
    # ÉTAPE 2.1.2: Envoyer la requête
    # - httpx.AsyncClient()
    # - timeout: 2 secondes
    
    # ÉTAPE 2.1.3: Parser la réponse
    # - Extraire routes[0]
    # - distance (m -> km)
    # - duration (s -> minutes)
    # - geometry (polyline)
    
    # ÉTAPE 2.1.4: Construire les segments
    # - Pour marche, typiquement 1 segment
    # - Mais peut avoir plusieurs steps si l'API le fournit
    
    # ÉTAPE 2.1.5: Retourner dict normalisé
    # TODO: Implémenter
    pass


async def _calculate_bike_route(
    from_lat: float,
    from_lon: float,
    to_lat: float,
    to_lon: float,
    time: str,
    request_id: str
) -> dict:
    """
    ÉTAPE 2.2: Calcul d'itinéraire à vélo
    
    LOGIQUE:
    - Similaire à walk, mais profile=bike
    - Peut privilégier les pistes cyclables
    - Vitesse moyenne différente (~15-20 km/h)
    """
    
    # ÉTAPE: Appeler API externe avec profile=bike
    # - Même structure que _calculate_walk_route
    # - Adapter les paramètres pour vélo
    
    # TODO: Implémenter
    pass


async def _calculate_transit_route(
    from_lat: float,
    from_lon: float,
    to_lat: float,
    to_lon: float,
    time: str,
    request_id: str
) -> dict:
    """
    ÉTAPE 2.3: Calcul d'itinéraire en transports en commun
    
    LOGIQUE:
    - Utiliser une API de transit (ex: OpenTripPlanner, Google Transit)
    - Obtenir un itinéraire avec bus/tram/métro
    - Parser les legs (segments) du trajet
    - Identifier les attentes (waiting time)
    
    SPÉCIFICITÉ:
    - Dépend fortement de l'heure de départ
    - Peut retourner plusieurs options
    - On prend la première/meilleure
    """
    
    # ÉTAPE 2.3.1: Appeler l'API de transit
    # - URL de l'API (ex: OpenTripPlanner /plan endpoint)
    # - Paramètres: from, to, time, mode=TRANSIT
    
    # ÉTAPE 2.3.2: Parser la réponse
    # - Extraire itineraries[0] (meilleur itinéraire)
    # - Pour chaque leg:
    #   * mode (WALK, BUS, TRAM, etc.)
    #   * from/to
    #   * duration
    #   * distance
    
    # ÉTAPE 2.3.3: Identifier les attentes
    # - Si gap temporel entre legs, c'est une attente
    # - Ajouter un segment virtuel "WAIT"
    
    # ÉTAPE 2.3.4: Construire segments[]
    # - Transformer chaque leg en segment
    # - Normaliser le mode (BUS -> TRANSIT)
    
    # ÉTAPE 2.3.5: Retourner dict
    # TODO: Implémenter
    pass


@app.get("/route/circular")
async def get_circular_route(
    center_lat: float = Query(..., description="Latitude du centre"),
    center_lon: float = Query(..., description="Longitude du centre"),
    radius_km: float = Query(..., gt=0, description="Rayon de la boucle en km"),
    mode: TravelMode = Query(TravelMode.WALK, description="Mode de transport"),
    request: Request = None
):
    """
    ÉTAPE BONUS: Générer un itinéraire circulaire
    
    LOGIQUE:
    - Pour les boucles Type C du Health Planner
    - Générer un itinéraire qui revient au point de départ
    - Distance approximative = radius_km * 2 * pi
    
    STRATÉGIE:
    - Calculer 4 points cardinaux autour du centre
    - Demander itinéraire: centre -> N -> E -> S -> W -> centre
    - Simplifier si l'API supporte les waypoints
    """
    
    # ÉTAPE 1: Calculer les waypoints
    # - Points à ~radius_km dans 4 directions
    # - Utiliser formule géographique pour décalage lat/lon
    
    # ÉTAPE 2: Appeler l'API avec waypoints
    # - Certaines APIs supportent waypoints[]
    # - Sinon, chaîner plusieurs appels
    
    # ÉTAPE 3: Assembler les segments
    # - Combiner tous les segments en un itinéraire
    
    # ÉTAPE 4: Retourner
    # TODO: Implémenter
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
