FROM node:18-slim
WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY . .
# Güvenlik için yetkisiz kullanıcıya geçiş (Senior detayı)
USER node
CMD ["node", "src/server.js"]

