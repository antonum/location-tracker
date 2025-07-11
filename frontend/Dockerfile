# Use Node.js 18 image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Expose port
EXPOSE 3000

# Install serve to serve the build
RUN npm install -g serve

# Serve the build
CMD ["serve", "-s", "build", "-l", "3000"]
