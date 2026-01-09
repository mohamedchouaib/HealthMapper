package com.healthroute.gateway.model;

import lombok.Data;
import lombok.Builder;
import java.util.List;

/**
 * Response GraphQL pour HealthPlan
 */
@Data
@Builder
public class HealthPlanResponse {
    private Plan selectedPlan;
    private Plan recommendedPlan;
    private Plan fallbackPlan;
    private List<Plan> alternatives;
    private WeatherSummary weatherSummary;
    private List<Alert> alerts;
    private EvaluationMetrics metrics;
    private String explanation;
    
    @Data
    @Builder
    public static class Plan {
        private String planType;
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
        private String mode;
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
    public static class WeatherSummary {
        private String decision;
        private Integer rainProbability;
        private Double temperature;
        private Double windSpeedKmh;
        private String conditions;
    }
    
    @Data
    @Builder
    public static class Alert {
        private String level;
        private String message;
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
