"""
Cache pour les données météo (persistance JSON)

LOGIQUE:
- Cache moyen (5min) pour équilibrer fraîcheur et performance
- Sauvegarder sur disque pour survie aux redémarrages
- TTL adaptatif selon l'heure (prévisions plus stables loin dans le futur)
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, Optional

DATA_DIR = "/app/data"
CACHE_FILE = os.path.join(DATA_DIR, "weather_cache.json")


class WeatherCache:
    """
    Gestionnaire de cache pour les données météo
    """
    
    def __init__(self, ttl_seconds: int = 300):
        """
        ÉTAPE: Initialiser le cache
        
        LOGIQUE:
        - Créer le dossier data s'il n'existe pas
        - Définir TTL par défaut
        - Charger le cache existant
        """
        self.ttl_seconds = ttl_seconds
        # TODO: Implémenter
        pass
    
    
    def get(self, key: str) -> Optional[dict]:
        """
        ÉTAPE: Récupérer une décision météo depuis le cache
        
        LOGIQUE:
        - Vérifier existence
        - Vérifier TTL
        - Retourner valeur ou None
        """
        # TODO: Implémenter
        pass
    
    
    def set(self, key: str, value: dict, ttl: Optional[int] = None):
        """
        ÉTAPE: Mettre une décision en cache
        
        LOGIQUE:
        - Stocker avec timestamp
        - Utiliser TTL adaptatif
        - Sauvegarder
        """
        # TODO: Implémenter
        pass
    
    
    def clear_expired(self):
        """
        ÉTAPE: Nettoyer les entrées expirées
        
        LOGIQUE:
        - Supprimer les entrées périmées
        - Optimiser la taille du cache
        """
        # TODO: Implémenter
        pass
