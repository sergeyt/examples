FROM gcc:latest as build

RUN apt-get update && apt-get install -y \
    libboost-dev \
    libboost-program-options-dev \
    cmake

ADD ./src /core/src

WORKDIR /core/build

RUN cmake ../src && cmake --build .

FROM ubuntu

RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

WORKDIR /core

COPY --from=build /core/build/sample_app .
