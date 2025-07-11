# AWS Deployment Guide

## Recommended: AWS App Runner (Easiest Option)

AWS App Runner is the simplest way to deploy your containerized application. It handles scaling, load balancing, and HTTPS automatically.

### Steps:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/location-tracker.git
   git push -u origin main
   ```

2. **Create App Runner Service**
   - Go to AWS Console → App Runner
   - Click "Create service"
   - Source: "Source code repository"
   - Connect to GitHub and select your repository
   - Runtime: "Docker"
   - Use `apprunner.yaml` configuration
   - **IMPORTANT**: Add environment variables:
     - `DATABASE_URL`: Your Timescale Cloud connection string
     - `FLASK_ENV`: `production`
     - `PORT`: `8080`
   - Click "Create & deploy"

3. **Access Your App**
   - App Runner will provide a public URL
   - Your app will be accessible at: `https://xxxxx.region.awsapprunner.com`

### Cost: ~$25-50/month for light usage

---

## Alternative Options:

### Option 2: AWS Lightsail (Simple & Cheap)
- **Cost**: $10-20/month
- **Steps**:
  1. Create Lightsail container service
  2. Push Docker image to AWS ECR
  3. Deploy container to Lightsail
  4. Configure custom domain (optional)

### Option 3: AWS ECS Fargate (More Control)
- **Cost**: $30-60/month
- **Steps**:
  1. Create ECS cluster
  2. Create task definition
  3. Create service with load balancer
  4. Configure auto-scaling

### Option 4: AWS Elastic Beanstalk (Platform-as-a-Service)
- **Cost**: $20-40/month
- **Steps**:
  1. Create Elastic Beanstalk application
  2. Upload Docker container
  3. Configure environment variables
  4. Deploy

---

## Quick Test Locally:

```bash
# Build the production container
docker build -t location-tracker .

# Run the container
docker run -p 8080:8080 \
  -e DATABASE_URL="your-database-url" \
  location-tracker

# Access at http://localhost:8080
```

## Environment Variables for Production:

```bash
DATABASE_URL=your-timescale-cloud-connection-string
PORT=8080
FLASK_ENV=production
```

## Security Considerations:

1. **Database Security**: Your Timescale Cloud connection is already secured with SSL
2. **Environment Variables**: Use AWS Systems Manager Parameter Store for sensitive data
3. **HTTPS**: App Runner provides HTTPS automatically
4. **Domain**: Configure custom domain in App Runner settings

## Monitoring:

- App Runner provides built-in monitoring
- CloudWatch logs automatically configured
- Health checks included
