cmake_minimum_required(VERSION 3.2)
project(HelloWorldProject)

# use C++17
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")

# use Boost.Program_options
set(Boost_USE_STATIC_LIBS ON)
find_package(Boost COMPONENTS program_options REQUIRED)
include_directories(${BOOST_INCLUDE_DIRS})

# executable file of sample app
add_executable(sample_app main.cpp hello_world.h)
target_link_libraries(sample_app ${Boost_LIBRARIES})
