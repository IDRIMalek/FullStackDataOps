## Projet Data Engineering E2E - Suivi et Prédiction de Performance d’Installations Énergétiques

### Objectif

Construire une plateforme de supervision de la performance de centrales photovoltaïques, intégrant ingestion batch + temps réel, traitement PySpark, orchestration Airflow 3, data catalog OpenMetadata, data warehouse Snowflake, base PostgreSQL, visualisation, ML/DL, CI/CD et déploiement Kubernetes + cloud.

### Thème central

**Surveillance, nettoyage, analyse, prédiction et exposition des données de performance énergétique (prod, temp, irradiance...)**

---

## Plan par Sprint Hebdomadaire (12 sprints)

### Semaine 1 - Environnement & Orchestrateur (Airflow 3 + Docker Compose)

* **Outils**: Docker, Docker Compose, Airflow 3 (avec DAG UI)
* **Objectifs**: setup local + premiers DAGs dummy + bonne structure repo
* **Livrables**: repo GitLab avec README, DAGs démo, CI minimal (lint + tests)

### Semaine 2 - Ingestion batch (API + fichiers CSV/Parquet)

* **Outils**: Airflow, requests/httpx, pandas, stockage local/S3
* **Objectifs**: ingestion de mesures PV simulées (API mock ou open), stockage brut
* **Livrables**: DAG ingestion API + CSV vers S3/PostgreSQL

### Semaine 3 - Streaming temps réel (Kafka)

* **Outils**: Kafka (Docker), Kafka Python client, Airflow sensor/consumer
* **Objectifs**: mock Kafka topic (données PV ou météo en temps réel)
* **Livrables**: Producer + Consumer Kafka, ingestion temps réel vers raw storage

### Semaine 4 - Traitement PySpark (ETL batch + streaming)

* **Outils**: PySpark, Airflow, Docker
* **Objectifs**: transformations basiques, nettoyage, enrichissement
* **Livrables**: jobs PySpark batch + streaming, DAGs associés

### Semaine 5 - Modélisation avec dbt (Snowflake & PostgreSQL)

* **Outils**: dbt-core, dbt-snowflake/postgres
* **Objectifs**: création de modèles, gestion des sources + tests dbt
* **Livrables**: modèles dbt, documentation, tests, lineage dbt

### Semaine 6 - Data Catalog + Lineage

* **Outils**: OpenMetadata (Docker), intégration Airflow/dbt/PostgreSQL/Snowflake
* **Objectifs**: automatiser la découverte des métadonnées + lineage complet
* **Livrables**: OpenMetadata déployé, connecteurs configurés

### Semaine 7 - CI/CD avancé

* **Outils**: GitLab CI, dbt Cloud, tests Airflow, docker build, YAML jobs
* **Objectifs**: tests auto, déploiement images, dbt run/test
* **Livrables**: pipelines GitLab CI/CD complètes (tests, build, deploy)

### Semaine 8 - Déploiement Kubernetes + Cloud

* **Outils**: K8s (kind ou AKS), Helm, MinIO/S3, Snowflake
* **Objectifs**: déployer Airflow/dbt/OpenMetadata sur cluster K8s
* **Livrables**: fichiers Helm/manifestes, accès distant

### Semaine 9 - Visualisation

* **Outils**: Metabase, Streamlit, Power BI (connecteurs)
* **Objectifs**: dashboards production, anomalies, forecast
* **Livrables**: 2-3 visualisations + lien public ou screenshot repo

### Semaine 10 - ML / DL avec scikit-learn ou PyTorch

* **Outils**: scikit-learn / PyTorch, MLflow
* **Objectifs**: prédiction de la performance ou détection de pannes
* **Livrables**: notebooks + modèle versionné + code d'entraînement/test

### Semaine 11 - Déploiement API de prédiction

* **Outils**: FastAPI, MLflow serving, Docker
* **Objectifs**: créer une API REST pour exposer les prédictions
* **Livrables**: endpoint prédiction, Swagger, test Postman/curl

### Semaine 12 - Gouvernance avancée & Sécurité

* **Outils**: RBAC OpenMetadata, tagging, audits
* **Objectifs**: politiques RGPD, accès détaillés, validation pipeline
* **Livrables**: documentation gouvernance, accès scénarisés, test sécurité

---

## Architecture Technique

* **Ingestion**: Airflow + Python + Kafka
* **Traitement**: PySpark
* **Modélisation**: dbt (Snowflake, PostgreSQL)
* **Catalog/Lineage**: OpenMetadata
* **Orchestration**: Airflow 3
* **ML**: scikit-learn / PyTorch + MLflow + FastAPI
* **Déploiement**: Docker + Kubernetes (AKS ou EKS)
* **CI/CD**: GitLab CI
* **Visualisation**: Metabase / Streamlit / Power BI

---

## Bonnes pratiques

* Versionning et environnement (dev/stage/prod)
* Nommage clair des assets (sources, modèles, tables)
* Documentation automatique dbt + OpenMetadata
* Logs centralisés et alerting Airflow
* Découplage ingestion / traitement / serving

---

## Livrables finaux

* Repo Git complet avec README, CI/CD, Dockerfile, YAML
* Documentation complète (Data/ML pipeline, sécu, lineage)
* Dashboard visuel
* API de prédiction déployée
* Screenshots / gif / démo vidéo

---

## Valorisation en entretien / CV

* **Titre**: "Data Platform Engineer - Projet Open Source Complet de Supervision Photovoltaïque"
* **Focus**: ingestion temps réel, orchestration avancée, ML déployé, gouvernance automatisée
* **Pitch**: "J’ai construit une plateforme complète de A à Z : ingestion batch & streaming avec Kafka, traitement PySpark, orchestration Airflow3, modélisation dbt, déploiement K8s cloud, suivi ML avec MLflow, exposition via API FastAPI et documentation lineage/gouvernance avec OpenMetadata."

Souhaites-tu maintenant que je te fournisse les fichiers de base (Airflow 3, dbt, PySpark, MLflow, etc.) pour chaque sprint ?
