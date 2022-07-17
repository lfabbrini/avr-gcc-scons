

#ifndef APPLICATION_H
#define APPLICATION_H


#ifdef __cplusplus
extern "C" {
#endif

//WHY????????????'
void init() __attribute__((weak));


void loop();
void setup();

#ifdef __cplusplus
}
#endif

#endif



