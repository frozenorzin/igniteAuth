// ./include/ig_decision.h

#ifndef IG_DECISION_H
#define IG_DECISION_H

#include<stdbool.h>

#define IG_MAX_STR 64

typedef struct {

    char sid[IG_MAX_STR];
    char intent[IG_MAX_STR];
    char command[IG_MAX_STR];
    char target[IG_MAX_STR];
    bool allow;
    char reason[128];   // empty if allowed
} IG_decision;



#endif 
