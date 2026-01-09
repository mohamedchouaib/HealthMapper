package com.healthroute.gateway.model;

import lombok.Data;
import lombok.Builder;
import java.util.List;

/**
 * Modèle de réponse du Health Planner Service
 * 
 * LOGIQUE:
 * - Désérialiser la réponse JSON du Planner
 * - Contenir tous les plans (recommandé, alternatives, fallback)
 * - Fournir les métriques d'évaluation
 */
@Data
@Builder
public class PlannerResponse {
    
    private Plan recommendedPlan;
    private List<Plan> alternatives;
    private Plan fallbackPlan;
    private String explanation;
    private EvaluationMetrics evaluationMetrics;
    
    @Data
    @Builder
    public static class Plan {
        private String planType;  // "HEALTH" ou "NORMAL"
        private Integer totalDurationMinutes;
        private Double totalDistanceKm;
        private ActivityMetrics activity;
        private List<Segment> segments;
        private String why;
    }
    
    @Data
    @Builder
    public static class ActivityMetrics {
        private Integer walkMinutes;
        private Integer bikeMinutes;
    }
    
    @Data
    @Builder
    public static class Segment {
        private String mode;  // "WALK", "BIKE", "TRANSIT"
        private Location from;
        private Location to;
        private Integer durationMinutes;
        private Double distanceKm;
        private String geometry;
    }
    
    @Data
    @Builder
    public static class Location {
        private Double lat;
        private Double lon;
        private String name;
    }
    
    @Data
    @Builder
    public static class EvaluationMetrics {
        private Boolean walkGoalAchieved;
        private Boolean bikeGoalAchieved;
        private Integer totalDetourMinutes;
        private Double totalDetourKm;
        private Double score;
    }
}
