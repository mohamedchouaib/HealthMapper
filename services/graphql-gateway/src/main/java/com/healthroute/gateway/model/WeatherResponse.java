package com.healthroute.gateway.model;

import lombok.Data;
import lombok.Builder;
import java.util.List;

/**
 * Modèle de réponse du Weather Service
 * 
 * LOGIQUE:
 * - Désérialiser la décision météo
 * - Contenir les raisons et pénalités
 * - Fournir un résumé pour l'utilisateur
 */
@Data
@Builder
public class WeatherResponse {
    
    private String decision;  // "OK", "WARNING", "BLOCK"
    private List<String> reasons;
    private Penalties penalties;
    private WeatherSummary summary;
    
    @Data
    @Builder
    public static class Penalties {
        private Double walkPenalty;  // 0..1
        private Double bikePenalty;  // 0..1
    }
    
    @Data
    @Builder
    public static class WeatherSummary {
        private Integer rainProbability;
        private Double temperature;
        private Double windSpeedKmh;
        private String conditions;
        private List<String> alerts;
    }
}
