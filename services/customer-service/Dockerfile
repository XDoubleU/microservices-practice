FROM node:latest
WORKDIR /app
COPY ./services/customer-service .
RUN npm install
EXPOSE 4002
ENTRYPOINT ["node", "index.js"]