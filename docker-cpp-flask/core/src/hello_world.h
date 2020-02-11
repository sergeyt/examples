#ifndef HELLO_WORLD_H
#define HELLO_WORLD_H

struct HelloWorld
{
    template <class OS>
    friend OS &operator<<(OS &os, const HelloWorld &)
    {
        os << "Hello World!";
        return os;
    }
};

#endif
