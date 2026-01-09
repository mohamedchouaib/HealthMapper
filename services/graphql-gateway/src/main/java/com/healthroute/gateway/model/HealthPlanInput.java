package com.healthroute.gateway.model;

import lombok.Data;
import lombok.Builder;

/**
 * Input GraphQL pour HealthPlan
 */
@Data
@Builder
public class HealthPlanInput {
    private LocationInput origin;
    private LocationInput destination;
    private String departureTime;
    private ActivityGoalsInput goals;
    private TripConstraintsInput constraints;
    private PreferencesInput preferences;
    
    @Data
    @Builder
    public static class LocationInput {
        private Double lat;
        private Double lon;
        private String address;
    }
    
    @Data
    @Builder
    public static class ActivityGoalsInput {
        private Integer walkMinutes;
        private Integer bikeMinutes;
    }
    
    @Data
    @Builder
    public static class TripConstraintsInput {
        private Integer maxTotalTimeMinutes;
        private Double maxDetourDistanceKm;
        private Integer maxDetourPercent;
    }
    
    @Data
    @Builder
    public static class PreferencesInput {
        private String avoidRain;
        private String windTolerance;
        private Boolean avoidStairs;
        private Boolean preferBikeParkings;
    }
}
