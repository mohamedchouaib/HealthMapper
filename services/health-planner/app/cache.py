"""
Cache pour stocker les plans générés (persistance JSON)

LOGIQUE:
- Sauvegarder les plans pour analyse/monitoring
- Éviter de recalculer des plans identiques
- Limiter la taille du cache (FIFO)
"""

import json
import os
from datetime import datetime
from typing import Dict, Optional, List
import hashlib

DATA_DIR = "/app/data"
CACHE_FILE = os.path.join(DATA_DIR, "plans_cache.json")
MAX_CACHE_SIZE = 100  # Nombre max de plans en cache


class PlanCache:
    """
    Gestionnaire de cache pour les plans
    """
    
    def __init__(self):
        """
        ÉTAPE: Initialiser le cache
        
        LOGIQUE:
        - Créer le dossier data s'il n'existe pas
        - Charger le cache existant ou créer un nouveau
        """
        # TODO: Implémenter
        pass
    
    
    def _load_cache(self) -> Dict:
        """
        ÉTAPE: Charger le cache depuis le fichier JSON
        
        LOGIQUE:
        - Lire plans_cache.json
        - Parser JSON
        - Si fichier n'existe pas ou corrompu, retourner {}
        """
        # TODO: Implémenter
        pass
    
    
    def _save_cache(self, cache: Dict):
        """
        ÉTAPE: Sauvegarder le cache dans le fichier JSON
        
        LOGIQUE:
        - Écrire le dict en JSON
        - Formater joliment (indent=2)
        - Gérer les erreurs d'écriture
        """
        # TODO: Implémenter
        pass
    
    
    def get_plan(self, request_hash: str) -> Optional[Dict]:
        """
        ÉTAPE: Récupérer un plan depuis le cache
        
        LOGIQUE:
        - Chercher par hash de la requête
        - Vérifier que le plan n'est pas trop ancien (ex: < 1 heure)
        - Retourner le plan ou None
        """
        # TODO: Implémenter
        pass
    
    
    def save_plan(self, request_hash: str, plan: Dict):
        """
        ÉTAPE: Sauvegarder un plan dans le cache
        
        LOGIQUE:
        - Ajouter timestamp
        - Limiter la taille du cache (FIFO)
        - Sauvegarder sur disque
        """
        # TODO: Implémenter
        pass
    
    
    def generate_request_hash(self, request: Dict) -> str:
        """
        ÉTAPE: Générer un hash unique pour une requête
        
        LOGIQUE:
        - Sérialiser les champs importants (origin, dest, goals)
        - Calculer MD5 ou SHA256
        - Retourner le hash en hex
        """
        # TODO: Implémenter
        pass
    
    
    def get_recent_plans(self, limit: int = 10) -> List[Dict]:
        """
        ÉTAPE: Récupérer les N plans les plus récents
        
        LOGIQUE:
        - Trier par timestamp décroissant
        - Retourner les N premiers
        - Utile pour monitoring/debug
        """
        # TODO: Implémenter
        pass
