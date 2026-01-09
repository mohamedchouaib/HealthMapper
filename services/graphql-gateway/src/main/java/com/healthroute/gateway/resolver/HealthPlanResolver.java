package com.healthroute.gateway.resolver;

import com.healthroute.gateway.model.*;
import com.healthroute.gateway.service.HealthRouteOrchestrator;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;
import reactor.core.publisher.Mono;

/**
 * ÉTAPE 4: Controller GraphQL - Point d'entrée des requêtes
 * 
 * LOGIQUE:
 * - Exposer la query "healthPlan"
 * - Valider les inputs GraphQL
 * - Déléguer au service orchestrateur
 * - Gérer les erreurs de manière user-friendly
 */
@Controller
@RequiredArgsConstructor
@Slf4j
public class HealthPlanResolver {

    private final HealthRouteOrchestrator orchestrator;

    /**
     * ÉTAPE 4.1: Resolver pour la query principale
     * 
     * LOGIQUE:
     * - Recevoir l'input GraphQL
     * - Logger la requête
     * - Appeler l'orchestrateur
     * - Retourner le résultat ou erreur GraphQL
     */
    @QueryMapping
    public Mono<HealthPlanResponse> healthPlan(@Argument HealthPlanInput input) {
        
        // ÉTAPE 4.1.1: Logger la requête entrante
        // - "Received healthPlan request: origin={}, destination={}"
        
        // ÉTAPE 4.1.2: Validation basique
        // - Vérifier que input n'est pas null
        // - Vérifier origin et destination
        // - Si invalide, retourner Mono.error() avec GraphQL error
        
        // ÉTAPE 4.1.3: Déléguer au service
        // - Appeler orchestrator.planHealthRoute(input)
        // - Laisser le service gérer la logique
        
        // ÉTAPE 4.1.4: Gestion des erreurs
        // - doOnError() pour logger les erreurs
        // - onErrorMap() pour transformer en GraphQLError si nécessaire
        // - Retourner un message clair à l'utilisateur
        
        // ÉTAPE 4.1.5: Logger la réponse
        // - doOnSuccess() pour logger: "Successfully returned health plan"
        
        return null; // TODO: Implémenter
    }
}
