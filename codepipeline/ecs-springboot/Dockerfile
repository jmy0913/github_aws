FROM gradle:8.1.1-jdk17-alpine as build

ENV APP_HOME=/apps

WORKDIR $APP_HOME

COPY build.gradle settings.gradle gradlew $APP_HOME/

COPY gradle $APP_HOME/gradle

RUN chmod +x gradlew

RUN ./gradlew build || return 0

COPY src $APP_HOME/src

RUN ./gradlew clean build

FROM openjdk:17-jdk-slim

ENV APP_HOME=/apps
ARG ARTIFACT_NAME=app.jar
# ARG JAR_FILE_PATH=build/libs/[프로젝트명]-0.0.1-SNAPSHOT.jar 
ARG JAR_FILE_PATH=build/libs/ecs-springboot-0.0.1-SNAPSHOT.jar 

WORKDIR $APP_HOME

COPY --from=build $APP_HOME/$JAR_FILE_PATH $ARTIFACT_NAME

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "app.jar"]

