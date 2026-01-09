package com.healthroute.gateway;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * ÉTAPE 1: Point d'entrée de l'application
 * 
 * LOGIQUE:
 * - Initialiser le contexte Spring Boot
 * - Configurer GraphQL
 * - Exposer l'endpoint /graphql
 * - Activer GraphiQL pour les tests (interface web)
 */
@SpringBootApplication
public class GraphQLGatewayApplication {

    public static void main(String[] args) {
        // ÉTAPE: Lancer l'application Spring Boot
        // - Charger la configuration depuis application.yml
        // - Initialiser les beans (services, clients REST)
        // - Démarrer le serveur sur le port 8080
        SpringApplication.run(GraphQLGatewayApplication.class, args);
    }
}
