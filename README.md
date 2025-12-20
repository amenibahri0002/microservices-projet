**Mini-Projet : Déploiement d’une Architecture Microservices Conteneurisée**



Docker – Kubernetes – CI/CD – Monitoring


**Contexte du projet**



Ce projet consiste à concevoir et déployer une architecture microservices conteneurisée,

orchestrée avec Kubernetes, intégrant une automatisation CI/CD et un monitoring basique.




**Compétence ciblée**



Concevoir et déployer une architecture microservices conteneurisée avec automatisation et supervision.


**Objectifs pédagogiques**



Ce projet permet de :



1. Concevoir une architecture microservices simple et cohérente.
   
2. Conteneuriser des applications avec Docker.
   
3. Déployer des microservices sur Kubernetes (Minikube).
   
4. Comprendre le principe d’un pipeline CI/CD.
   
5. Superviser les services via des outils de monitoring.
   
6. Produire une documentation professionnelle.




**Description de l’architecture**



L’application est composée de deux microservices indépendants :



* **Microservice Calculatrice**



Fournit des opérations mathématiques simples (addition).



Exposé via une API REST.



* **Microservice Statistiques**



Fournit des calculs statistiques simples (moyenne).



Exposé via une API REST.



Chaque microservice est développé en Python (Flask), conteneurisé avec Docker et déployé sur Kubernetes.



**Technologies utilisées**



* Python (Flask)



* Docker



* Docker Compose



* Kubernetes (Minikube)



* Git / GitHub



* GitHub Actions (CI/CD)



* Prometheus et Grafana (monitoring)



**Conteneurisation**



Chaque microservice possède :



* un fichier Dockerfile,pour la construction de l’image.



* un fichier requirements.txt pour la gestion des dépendances.



Un fichier docker-compose.yml permet de lancer l’ensemble des services en local pour les tests.



**Déploiement Kubernetes**



Le déploiement est réalisé à l’aide de manifests Kubernetes :



* Deployment pour chaque microservice,



* Service pour exposer les applications,



* Déploiement de Prometheus et Grafana pour le monitoring.



Les fichiers YAML sont regroupés dans le dossier k8s/.

**Pipeline CI/CD**



Un pipeline CI/CD est mis en place avec GitHub Actions afin de :



* automatiser le build des images Docker,



* faciliter l’intégration continue,



* assurer la traçabilité des modifications via GitHub.





**Monitoring**



Un système de monitoring basique est intégré :



* Prometheus pour la collecte des métriques,



* Grafana pour la visualisation via des dashboards.



Les composants de monitoring sont déployés sur Kubernetes.

**Structure du projet**


microservices-projet/

│

├── service-calculatrice/

│   ├── app.py

│   ├── requirements.txt

│   └── Dockerfile

│

├── service-statistiques/

│   ├── app\_stats.py

│   ├── requirements.txt

│   └── Dockerfile

│

├── k8s/

│   ├── calculatrice-deployment.yaml

│   ├── calculatrice-service.yaml

│   ├── statistiques-deployment.yaml

│   └── statistiques-service.yaml

│

└── docker-compose.yml





