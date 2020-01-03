cmake_minimum_required(VERSION 3.2)
project(online_course_server)
set(CMAKE_CXX_STANDARD 11)

list(APPEND PROJECT_SRCS
        ${PROJECT_SOURCE_DIR}/main.cpp
        )


add_executable(server ${PROJECT_SRCS})
target_include_directories(server PUBLIC ${PROJECT_SOURCE_DIR}/net/handy)
target_link_libraries(server, ${PROJECT_SOURCE_DIR}/lib/libhandy_s.a)