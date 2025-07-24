# MiniGit Microservices Project

This project demonstrates a microservices architecture with authentication and order management services, deployed using Kubernetes.

## Project Structure

```
/auth
  Dockerfile          # Docker configuration for auth service
  app.py             # Flask authentication service
  requirements.txt   # Python dependencies

/orders
  Dockerfile          # Docker configuration for orders service
  app.py             # Flask orders service
  requirements.txt   # Python dependencies

/k8s
  auth-deployment.yaml    # Kubernetes deployment for auth service
  orders-deployment.yaml  # Kubernetes deployment for orders service
  ingress.yaml           # Ingress configuration

.github/
  workflows/
    ci-cd.yml         # GitHub Actions CI/CD pipeline
```

## Services

### Auth Service (Port 5000)
- **POST /login** - Authenticate user and get JWT token
- **POST /validate** - Validate JWT token
- **GET /health** - Health check endpoint

### Orders Service (Port 5001)
- **GET /orders** - Get all orders (requires authentication)
- **POST /orders** - Create new order (requires authentication)
- **GET /orders/<id>** - Get specific order (requires authentication)
- **GET /health** - Health check endpoint

## Local Development

### Prerequisites
- Docker
- Python 3.9+
- kubectl (for Kubernetes deployment)

### Running Locally

1. **Auth Service:**
   ```bash
   cd auth
   pip install -r requirements.txt
   python app.py
   ```

2. **Orders Service:**
   ```bash
   cd orders
   pip install -r requirements.txt
   python app.py
   ```

### Building Docker Images

```bash
# Build auth service
docker build -t auth:latest ./auth

# Build orders service
docker build -t orders:latest ./orders
```

## Kubernetes Deployment

### Deploy to Kubernetes

```bash
# Apply all Kubernetes configurations
kubectl apply -f k8s/

# Check deployment status
kubectl get pods
kubectl get services
kubectl get ingress
```

### Access the Application

After deployment, the services will be available through the ingress:
- Auth Service: `http://miniapp.local/auth`
- Orders Service: `http://miniapp.local/orders`

## API Usage Examples

### 1. Login to get token
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}'
```

### 2. Create an order (using the token from step 1)
```bash
curl -X POST http://localhost:5001/orders \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{"product":"laptop","quantity":1,"price":999.99}'
```

### 3. Get all orders
```bash
curl -X GET http://localhost:5001/orders \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

## CI/CD Pipeline

The GitHub Actions workflow automatically:
1. Runs tests and linting on both services
2. Builds Docker images and pushes to GitHub Container Registry
3. Deploys to Kubernetes cluster (on main branch)

## Configuration

### Required Secrets (for GitHub Actions)
- `KUBECONFIG` - Base64 encoded Kubernetes configuration file

### Environment Variables
- `SECRET_KEY` - JWT secret key for auth service (configured in Kubernetes deployment)

## Features

- **Microservices Architecture**: Separate auth and orders services
- **JWT Authentication**: Secure token-based authentication
- **Kubernetes Ready**: Complete K8s deployment configurations
- **CI/CD Pipeline**: Automated testing, building, and deployment
- **Health Checks**: Built-in health endpoints for monitoring
- **Ingress**: Single entry point with path-based routing
