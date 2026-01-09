"""
ÉTAPE 1: Weather Service - Décision météo

LOGIQUE GLOBALE:
- Service REST pour évaluer les conditions météo
- Appelle une API météo externe
- Produit une décision: OK / WARNING / BLOCK
- Fournit un résumé et des alertes

PORT: 8004
"""

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from enum import Enum
import logging
import os
from typing import Optional, List
from datetime import datetime, timedelta

# ÉTAPE: Importer les modules locaux
# from .models import WeatherDecision, WeatherResponse
# from .services.weather_adapter import WeatherAdapter
# from .services.decision_engine import WeatherDecisionEngine
# from .cache import WeatherCache

# ÉTAPE: Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ÉTAPE: Initialiser l'application FastAPI
app = FastAPI(
    title="Weather Service",
    description="Service de décision météo pour itinéraires santé",
    version="1.0.0"
)

# ÉTAPE: Configuration
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
CACHE_TTL_SECONDS = 300  # Cache de 5 minutes


class WeatherDecision(str, Enum):
    """Décision météo"""
    OK = "OK"
    WARNING = "WARNING"
    BLOCK = "BLOCK"


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
    - Optionnel: Tester l'API météo
    """
    return {"status": "healthy", "service": "weather"}


# ÉTAPE: Endpoint principal - GET /weather/decision
@app.get("/weather/decision")
async def get_weather_decision(
    origin_lat: float = Query(..., description="Latitude origine"),
    origin_lon: float = Query(..., description="Longitude origine"),
    dest_lat: float = Query(..., description="Latitude destination"),
    dest_lon: float = Query(..., description="Longitude destination"),
    departure_time: str = Query("now", description="Heure de départ"),
    duration_minutes: int = Query(..., gt=0, description="Durée estimée du trajet"),
    request: Request = None
):
    """
    ÉTAPE PRINCIPALE: Décision météo pour un trajet
    
    LOGIQUE MÉTIER:
    1. Calculer la fenêtre temporelle (départ + durée)
    2. Obtenir les prévisions météo pour cette fenêtre
    3. Analyser les conditions (pluie, vent, température)
    4. Appliquer les règles de décision
    5. Calculer les pénalités (walk_penalty, bike_penalty)
    6. Générer le résumé et les alertes
    7. Retourner la décision
    
    INPUT:
    - origin_lat, origin_lon: Point de départ
    - dest_lat, dest_lon: Point d'arrivée
    - departure_time: Heure de départ (ISO 8601 ou "now")
    - duration_minutes: Durée du trajet
    
    OUTPUT:
    - decision: OK / WARNING / BLOCK
    - reasons: Liste des raisons
    - penalties: walk_penalty (0-1), bike_penalty (0-1)
    - summary: Résumé météo avec détails
    
    RÈGLES DE DÉCISION:
    - BLOCK si:
      * Pluie forte (> 10mm/h) sur majorité du trajet
      * Alerte météo officielle sévère (orange/rouge)
      * Vent très fort (> 70 km/h)
    
    - WARNING si:
      * Pluie modérée (5-10mm/h) ou probabilité > 60%
      * Froid intense (< 0°C)
      * Vent modéré (40-70 km/h)
      * Canicule (> 35°C)
    
    - OK sinon
    """
    
    # ÉTAPE 1.1: Extraire requestId
    # - request_id = request.headers.get('X-Request-Id')
    # - Logger: "Weather decision request: from ({},{}) to ({},{}) at {}"
    
    # ÉTAPE 1.2: Parser departure_time
    # - Si "now": datetime.now()
    # - Sinon: parser ISO 8601
    # - Calculer arrival_time = departure_time + duration_minutes
    
    # ÉTAPE 1.3: Vérifier le cache
    # - cache_key = f"weather_{origin_lat}_{origin_lon}_{dest_lat}_{dest_lon}_{departure_time}"
    # - cached = cache.get(cache_key)
    # - Si valide (< 5min), retourner cached
    
    # ÉTAPE 1.4: Obtenir les données météo
    # - Appeler _fetch_weather_data() pour origine et destination
    # - Moyenner ou prendre le pire des deux
    
    # ÉTAPE 1.5: Appliquer les règles de décision
    # - Appeler _apply_decision_rules()
    # - Obtenir decision, reasons, penalties
    
    # ÉTAPE 1.6: Construire le résumé
    # - _build_weather_summary()
    # - Inclure: rain_probability, temperature, wind_speed, conditions
    
    # ÉTAPE 1.7: Mettre en cache
    # - cache.set(cache_key, response, ttl=CACHE_TTL_SECONDS)
    
    # ÉTAPE 1.8: Logger et retourner
    # - Logger: "Weather decision: {}, reasons: {}"
    # - Retourner WeatherResponse JSON
    
    # TODO: Implémenter
    pass


async def _fetch_weather_data(
    lat: float,
    lon: float,
    start_time: datetime,
    end_time: datetime,
    request_id: str
) -> dict:
    """
    ÉTAPE 2.1: Obtenir les données météo depuis l'API externe
    
    LOGIQUE:
    - Appeler l'API météo (ex: OpenWeatherMap, Weather API)
    - Obtenir prévisions pour la fenêtre temporelle
    - Parser et extraire:
      * Probabilité de pluie
      * Intensité de pluie (mm/h)
      * Température
      * Vitesse du vent
      * Conditions générales
      * Alertes officielles
    
    API SUGGÉRÉES:
    - OpenWeatherMap (gratuit avec limites)
    - WeatherAPI.com
    - Météo France API
    """
    
    # ÉTAPE 2.1.1: Construire la requête API
    # - URL: ex. "https://api.openweathermap.org/data/2.5/forecast"
    # - Params:
    #   * lat, lon
    #   * appid: WEATHER_API_KEY
    #   * units: metric
    
    # ÉTAPE 2.1.2: Envoyer la requête
    # - async with httpx.AsyncClient() as client:
    # - response = await client.get(url, params=params, timeout=3.0)
    
    # ÉTAPE 2.1.3: Parser la réponse
    # - data = response.json()
    # - Extraire les prévisions pour la fenêtre temporelle
    # - Pour chaque période (ex: 3h):
    #   * Vérifier si overlap avec [start_time, end_time]
    #   * Extraire météo
    
    # ÉTAPE 2.1.4: Agréger les données
    # - Calculer moyennes/max pour la fenêtre
    # - rain_probability: moyenne des probabilités
    # - rain_intensity: max des intensités
    # - temperature: moyenne
    # - wind_speed: max
    # - conditions: condition la plus fréquente
    
    # ÉTAPE 2.1.5: Vérifier les alertes
    # - Si l'API fournit des alertes (alerts[])
    # - Extraire event, severity, description
    
    # ÉTAPE 2.1.6: Retourner dict normalisé
    # - {
    #     'rain_probability': 0.45,  # 0-1
    #     'rain_intensity_mmh': 5.2,
    #     'temperature_c': 12.5,
    #     'wind_speed_kmh': 25.0,
    #     'conditions': 'light rain',
    #     'alerts': [...]
    #   }
    
    # TODO: Implémenter
    pass


def _apply_decision_rules(
    weather_data: dict,
    user_preferences: Optional[dict] = None
) -> tuple:
    """
    ÉTAPE 2.2: Appliquer les règles de décision
    
    LOGIQUE:
    - Analyser weather_data
    - Appliquer les seuils définis
    - Prendre en compte user_preferences (avoid_rain: strict/flexible)
    - Retourner (decision, reasons, penalties)
    
    RÈGLES:
    1. Alertes officielles
       - Si alert.severity == "severe": BLOCK
       - Si alert.severity == "moderate": WARNING
    
    2. Pluie
       - Si rain_intensity > 10 mm/h: BLOCK, reason="Pluie forte"
       - Si rain_intensity > 5 mm/h: WARNING, reason="Pluie modérée"
       - Si rain_probability > 70%: WARNING, reason="Risque élevé de pluie"
    
    3. Vent
       - Si wind_speed > 70 km/h: BLOCK, reason="Vent très fort"
       - Si wind_speed > 40 km/h: WARNING, reason="Vent fort"
    
    4. Température
       - Si temp < 0°C: WARNING, reason="Températures glaciales"
       - Si temp > 35°C: WARNING, reason="Canicule"
    
    5. Pénalités
       - walk_penalty = (rain_intensity / 20) * 0.5 + (wind_speed / 100) * 0.3
       - bike_penalty = walk_penalty * 1.5 (vélo plus sensible)
       - Clamp entre 0 et 1
    """
    
    # ÉTAPE 2.2.1: Initialiser
    decision = WeatherDecision.OK
    reasons = []
    walk_penalty = 0.0
    bike_penalty = 0.0
    
    # ÉTAPE 2.2.2: Vérifier alertes officielles
    # - Si alerts et severity == "severe":
    #   * decision = BLOCK
    #   * reasons.append("Alerte météo sévère")
    
    # ÉTAPE 2.2.3: Vérifier pluie
    # - Appliquer les règles ci-dessus
    # - Mettre à jour decision et reasons
    
    # ÉTAPE 2.2.4: Vérifier vent
    # - Appliquer les règles
    
    # ÉTAPE 2.2.5: Vérifier température
    # - Appliquer les règles
    
    # ÉTAPE 2.2.6: Calculer pénalités
    # - Formules ci-dessus
    # - Clamp à [0, 1]
    
    # ÉTAPE 2.2.7: Retourner
    # - return (decision, reasons, {'walk_penalty': walk_penalty, 'bike_penalty': bike_penalty})
    
    # TODO: Implémenter
    pass


def _build_weather_summary(weather_data: dict) -> dict:
    """
    ÉTAPE 2.3: Construire un résumé météo pour l'utilisateur
    
    LOGIQUE:
    - Transformer les données brutes en résumé lisible
    - Arrondir les valeurs
    - Générer une description textuelle
    
    RETURN: dict pour WeatherSummary
    """
    
    # ÉTAPE: Construire le dict
    # - rain_probability: int (%)
    # - temperature: float (°C)
    # - wind_speed_kmh: float
    # - conditions: string (ex: "Nuageux avec pluie légère")
    # - alerts: liste de strings
    
    # TODO: Implémenter
    pass


@app.get("/weather/current")
async def get_current_weather(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    request: Request = None
):
    """
    ÉTAPE BONUS: Obtenir la météo actuelle (pour debug)
    
    LOGIQUE:
    - Appeler l'API météo pour conditions actuelles
    - Retourner les données brutes
    - Utile pour tests
    """
    
    # TODO: Implémenter
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
