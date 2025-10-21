# CI/CD Demo

1. Clone repository.
2. Start k3d cluster: `k3d cluster create cicd --agents 2`
3. `cd app` and run tests: `python -m pytest tests/`
4. Build image and push to Docker Hub.
5. Configure Jenkins credentials: dockerhub-creds (username/password), kubeconfig (secret text).
6. Run Jenkins pipeline (Jenkinsfile).
7. Monitor with Prometheus/Grafana (installed via Helm).
