"""
Cache pour les données Naolib (persistance JSON)

LOGIQUE:
- Cache court (60s) pour réduire les appels API
- Sauvegarder les données sur disque pour redémarrage
- Gestion TTL (Time To Live)
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, Optional

DATA_DIR = "/app/data"
CACHE_FILE = os.path.join(DATA_DIR, "naolib_cache.json")


class NaolibCache:
    """
    Gestionnaire de cache pour les données Naolib
    """
    
    def __init__(self, ttl_seconds: int = 60):
        """
        ÉTAPE: Initialiser le cache
        
        LOGIQUE:
        - Créer le dossier data s'il n'existe pas
        - Définir TTL
        - Charger le cache existant
        """
        self.ttl_seconds = ttl_seconds
        # TODO: Implémenter
        pass
    
    
    def get(self, key: str) -> Optional[dict]:
        """
        ÉTAPE: Récupérer une valeur depuis le cache
        
        LOGIQUE:
        - Vérifier si la clé existe
        - Vérifier si le TTL n'est pas expiré
        - Si valide, retourner la valeur
        - Sinon, retourner None
        """
        # TODO: Implémenter
        pass
    
    
    def set(self, key: str, value: dict, ttl: Optional[int] = None):
        """
        ÉTAPE: Mettre une valeur en cache
        
        LOGIQUE:
        - Stocker avec timestamp actuel
        - Utiliser ttl fourni ou ttl par défaut
        - Sauvegarder sur disque
        """
        # TODO: Implémenter
        pass
    
    
    def clear_expired(self):
        """
        ÉTAPE: Nettoyer les entrées expirées
        
        LOGIQUE:
        - Parcourir toutes les clés
        - Supprimer celles dont le timestamp + TTL < now
        - Sauvegarder le cache nettoyé
        """
        # TODO: Implémenter
        pass
