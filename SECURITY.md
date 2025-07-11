# Security Configuration Guide

## Environment Variables Setup

### 🔐 **Local Development**

1. **Copy the example file:**
   ```bash
   cp backend/.env.example backend/.env
   ```

2. **Edit `backend/.env` with your credentials:**
   ```bash
   DATABASE_URL=postgres://username:password@host:port/database?sslmode=require
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```

3. **Never commit `.env` files** (already in `.gitignore`)

### ☁️ **AWS App Runner Deployment**

1. **Deploy without credentials in code:**
   ```bash
   git add .
   git commit -m "Secure deployment setup"
   git push origin main
   ```

2. **Set environment variables in AWS Console:**
   - Go to App Runner → Your Service → Configuration → Environment variables
   - Add these variables:
     - `DATABASE_URL`: `your-database-connection-string`
     - `FLASK_ENV`: `production`
     - `PORT`: `8080`

3. **Deploy the updated service**

### 🧪 **Local Testing**

```bash
# Set environment variable
export DATABASE_URL='postgres://username:password@host:port/database?sslmode=require'

# Run the test script
./build-and-test.sh
```

### 🛡️ **Security Best Practices**

1. **Never commit secrets:**
   - Database passwords
   - API keys
   - Connection strings

2. **Use environment variables:**
   - Local: `.env` files
   - AWS: App Runner environment variables
   - Docker: `-e` flags

3. **Rotate credentials regularly:**
   - Update database passwords
   - Update environment variables

4. **Use AWS Secrets Manager (Advanced):**
   - Store sensitive data in AWS Secrets Manager
   - Reference secrets in App Runner

### 📋 **Checklist Before Deployment**

- [ ] Remove hardcoded credentials from all files
- [ ] Add credentials to `.env` for local development
- [ ] Ensure `.env` is in `.gitignore`
- [ ] Set environment variables in AWS App Runner
- [ ] Test locally with environment variables
- [ ] Verify deployment works without embedded secrets

### 🔍 **How to Check for Exposed Secrets**

```bash
# Search for potential secrets in your code
grep -r "postgres://" --exclude-dir=.git .
grep -r "password" --exclude-dir=.git --exclude="*.md" .
grep -r "tsdbadmin" --exclude-dir=.git .
```

### 🚨 **If You Accidentally Committed Secrets**

1. **Change your database password immediately**
2. **Remove secrets from git history:**
   ```bash
   git filter-branch --force --index-filter \
     'git rm --cached --ignore-unmatch backend/.env' \
     --prune-empty --tag-name-filter cat -- --all
   ```
3. **Force push to overwrite history:**
   ```bash
   git push origin --force --all
   ```

### 💡 **Pro Tips**

- Use different database users for development and production
- Consider using AWS RDS Proxy for additional security
- Enable database connection logging for monitoring
- Use IAM roles instead of passwords when possible
