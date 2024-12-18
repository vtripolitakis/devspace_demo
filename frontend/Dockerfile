# frontend/Dockerfile
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the application files
COPY . .

# Expose Vite default port
EXPOSE 5173

# Start the development server
CMD ["yarn", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
