"""
Modèles de données pour le Health Planner Service

LOGIQUE:
- Définir les structures Pydantic pour validation
- Assurer la cohérence avec les contrats REST
- Faciliter la sérialisation JSON
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum


# ==================== ENUMS ====================

class PlanType(str, Enum):
    """Type de plan"""
    HEALTH = "HEALTH"
    NORMAL = "NORMAL"


class TravelMode(str, Enum):
    """Mode de transport"""
    WALK = "WALK"
    BIKE = "BIKE"
    TRANSIT = "TRANSIT"


# ==================== REQUEST ====================

class Location(BaseModel):
    """Localisation (coordonnées ou adresse)"""
    lat: Optional[float] = None
    lon: Optional[float] = None
    address: Optional[str] = None
    
    # ÉTAPE: Validator
    # - Au moins lat/lon OU address doit être fourni
    # - Si lat fourni, lon doit l'être aussi (et vice-versa)


class ActivityGoals(BaseModel):
    """Objectifs d'activité physique"""
    walk_minutes: int = Field(..., gt=0, description="Minutes de marche souhaitées")
    bike_minutes: Optional[int] = Field(None, ge=0, description="Minutes de vélo (optionnel)")


class TripConstraints(BaseModel):
    """Contraintes de trajet"""
    max_total_time_minutes: Optional[int] = Field(None, gt=0)
    max_detour_distance_km: Optional[float] = Field(None, gt=0)
    max_detour_percent: Optional[int] = Field(None, gt=0, le=100)
    
    # ÉTAPE: Validator
    # - Au moins une contrainte doit être définie


class Preferences(BaseModel):
    """Préférences utilisateur"""
    avoid_stairs: Optional[bool] = False
    prefer_bike_parkings: Optional[bool] = False


class PlanRequest(BaseModel):
    """Requête complète pour générer un plan"""
    origin: Location
    destination: Location
    departure_time: Optional[str] = "now"  # ISO 8601 ou "now"
    goals: ActivityGoals
    constraints: TripConstraints
    preferences: Optional[Preferences] = Preferences()


# ==================== RESPONSE ====================

class LocationOutput(BaseModel):
    """Localisation en sortie"""
    lat: float
    lon: float
    name: Optional[str] = None


class Segment(BaseModel):
    """Segment d'un itinéraire"""
    mode: TravelMode
    from_location: LocationOutput = Field(..., alias="from")
    to_location: LocationOutput = Field(..., alias="to")
    duration_minutes: int
    distance_km: float
    geometry: Optional[str] = None  # Polyline
    
    class Config:
        populate_by_name = True


class ActivityMetrics(BaseModel):
    """Métriques d'activité"""
    walk_minutes: int
    bike_minutes: int


class Plan(BaseModel):
    """Structure d'un plan complet"""
    plan_type: PlanType
    total_duration_minutes: int
    total_distance_km: float
    activity: ActivityMetrics
    segments: List[Segment]
    why: str  # Explication courte


class EvaluationMetrics(BaseModel):
    """Métriques d'évaluation du plan"""
    walk_goal_achieved: bool
    bike_goal_achieved: bool
    total_detour_minutes: int
    total_detour_km: float
    score: float


class PlanResponse(BaseModel):
    """Réponse complète du Planner"""
    recommended_plan: Plan
    alternatives: List[Plan]
    fallback_plan: Plan
    explanation: str
    evaluation_metrics: EvaluationMetrics
