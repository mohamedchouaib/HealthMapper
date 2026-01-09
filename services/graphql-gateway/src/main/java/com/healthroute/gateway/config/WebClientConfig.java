package com.healthroute.gateway.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.WebClient;

/**
 * ÉTAPE 2: Configuration des clients REST
 * 
 * LOGIQUE:
 * - Créer des WebClient configurés pour chaque service
 * - Configurer les timeouts appropriés
 * - Ajouter des headers communs
 * - Préparer pour circuit breaker
 */
@Configuration
public class WebClientConfig {

    @Value("${services.health-planner.url}")
    private String healthPlannerUrl;

    @Value("${services.health-planner.timeout}")
    private int healthPlannerTimeout;

    @Value("${services.weather.url}")
    private String weatherUrl;

    @Value("${services.weather.timeout}")
    private int weatherTimeout;

    /**
     * ÉTAPE 2.1: Client pour Health Planner Service
     * 
     * LOGIQUE:
     * - Configurer l'URL de base du service
     * - Définir un timeout de connexion et lecture (ex: 3s)
     * - Ajouter un header pour le requestId (traçabilité)
     * - Configurer la gestion des erreurs HTTP
     */
    @Bean(name = "healthPlannerClient")
    public WebClient healthPlannerClient() {
        // ÉTAPE: Créer HttpClient avec timeout
        // - Connection timeout: 2000ms
        // - Read timeout: healthPlannerTimeout ms
        // - Write timeout: 2000ms
        
        // ÉTAPE: Construire WebClient
        // - baseUrl = healthPlannerUrl
        // - defaultHeaders: Content-Type: application/json
        // - Interceptor pour ajouter X-Request-Id
        
        return null; // TODO: Implémenter
    }

    /**
     * ÉTAPE 2.2: Client pour Weather Service
     * 
     * LOGIQUE:
     * - Similaire à healthPlannerClient
     * - Timeout plus court (c'est le dernier appelé)
     * - Retry automatique en cas d'échec
     */
    @Bean(name = "weatherClient")
    public WebClient weatherClient() {
        // ÉTAPE: Créer HttpClient avec timeout
        // - Connection timeout: 1500ms
        // - Read timeout: weatherTimeout ms
        
        // ÉTAPE: Construire WebClient
        // - baseUrl = weatherUrl
        // - defaultHeaders
        
        return null; // TODO: Implémenter
    }
}
