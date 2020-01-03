//
// Created by wangyingwu on 2019/12/31.
//

#include "handy.h"
using namepsace std;
using namespace handy;

int main(int argc, const char *argv[]) {
    EventBase base;
    Signal::signal(SIGINT, [&] {base.exit();});
}
