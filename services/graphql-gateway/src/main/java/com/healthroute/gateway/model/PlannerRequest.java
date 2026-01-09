package com.healthroute.gateway.model;

import lombok.Data;
import lombok.Builder;

/**
 * Modèle de données pour la requête au Health Planner Service
 * 
 * LOGIQUE:
 * - Transformer les inputs GraphQL en format REST
 * - Valider les données avant l'envoi
 * - Sérialiser en JSON
 */
@Data
@Builder
public class PlannerRequest {
    
    // ÉTAPE: Définir les champs nécessaires
    // - origin (Location)
    // - destination (Location)
    // - departureTime (String ISO 8601)
    // - goals (ActivityGoals)
    // - constraints (TripConstraints)
    // - preferences (Preferences - sans les paramètres météo)
    
    @Data
    @Builder
    public static class Location {
        private Double lat;
        private Double lon;
        private String address;
    }
    
    @Data
    @Builder
    public static class ActivityGoals {
        private Integer walkMinutes;
        private Integer bikeMinutes;
    }
    
    @Data
    @Builder
    public static class TripConstraints {
        private Integer maxTotalTimeMinutes;
        private Double maxDetourDistanceKm;
        private Integer maxDetourPercent;
    }
    
    @Data
    @Builder
    public static class Preferences {
        private Boolean avoidStairs;
        private Boolean preferBikeParkings;
    }
}
