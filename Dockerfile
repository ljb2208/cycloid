FROM resin/rpi-raspbian:stretch AS build

# Make the number of compile jobs configurable.
ARG jobs=8

# Install build tools and remove apt-cache afterwards
RUN apt-get -q update
RUN apt-get install -yq --no-install-recommends \
  build-essential \
  cmake \
  libeigen3-dev \
  pkg-config

# Install debugging packages. TODO Remove once this Dockerfile is stable.
RUN apt-get install -yq --no-install-recommends \
  cmake-curses-gui \
  vim
RUN apt-get clean 

# Copy all the app source into docker context
COPY . /usr/cycloid

# Build our binary
WORKDIR /usr/build
# LIBRARY_TYPE is a custom way of 'userland' to switch between static/shared.
# There is also a 'vcos' library whose static behavior can be controlled through
# VCOS_PTHREADS_BUILD_SHARED; however setting this to FALSE does not work (obvious link error).
# In order not to modify 'userland', we just set the library install target correctly.
# VMCS_INSTALL_PREFIX.
RUN cmake /usr/cycloid/src \
  -DBUILD_SHARED_LIBS=OFF -DLIBRARY_TYPE=STATIC \
  -DCMAKE_INSTALL_PREFIX=/usr/local -DVMCS_INSTALL_PREFIX=/usr/local
RUN cmake --build . -- --jobs=$jobs
RUN cmake --build . -- --jobs=$jobs install

FROM resin/rpi-raspbian:stretch
COPY --from=build /usr/local /usr/local

RUN ldconfig
#switch on systemd init system in container
ENV INITSYSTEM on

CMD drive
