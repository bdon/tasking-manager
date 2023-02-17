FROM node:18 as build

WORKDIR /usr/src/app/frontend
COPY frontend .
COPY tasking-manager.env ..

## SETUP
# --legacy-peer-deps is a temporary hack to make `react-placeholder` install with react v18
RUN npm install --legacy-peer-deps

ARG TM_APP_API_URL=https://tasks-backend.openstreetmap.us/api

# SERVE
RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /usr/src/app/frontend/build /usr/share/nginx/html
COPY --from=build /usr/src/app/frontend/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
