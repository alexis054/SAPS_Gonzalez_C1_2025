#include "classifier.h"

/**
* Predict class for features vector
*/
int predict(float *x) {
    uint8_t votes[4] = { 0 };
    // tree #1
    if (x[6] <= 0.20362336933612823) {
        if (x[7] <= 0.1259133778512478) {
            if (x[2] <= 106.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[8] <= 0.5021437704563141) {
            if (x[7] <= 0.08939755335450172) {
                votes[0] += 1;
            }

            else {
                if (x[6] <= 0.27297917008399963) {
                    if (x[7] <= 0.15301983058452606) {
                        if (x[5] <= 105.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[6] <= 0.44674208760261536) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[4] <= 80.5) {
                            votes[0] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }
        }

        else {
            if (x[1] <= 78.5) {
                if (x[8] <= 0.5543814301490784) {
                    votes[2] += 1;
                }

                else {
                    if (x[8] <= 0.6410063803195953) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }

            else {
                votes[2] += 1;
            }
        }
    }

    // tree #2
    if (x[6] <= 0.20362336933612823) {
        if (x[7] <= 0.1259133778512478) {
            if (x[2] <= 106.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[8] <= 0.5021437704563141) {
            if (x[8] <= 0.2500763237476349) {
                votes[0] += 1;
            }

            else {
                if (x[6] <= 0.27297917008399963) {
                    if (x[7] <= 0.15301983058452606) {
                        if (x[5] <= 105.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[6] <= 0.44674208760261536) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[3] <= 80.5) {
                            votes[0] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }
        }

        else {
            if (x[2] <= 78.5) {
                if (x[8] <= 0.5543814301490784) {
                    votes[2] += 1;
                }

                else {
                    if (x[7] <= 0.20230832695960999) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }

            else {
                votes[2] += 1;
            }
        }
    }

    // tree #3
    if (x[7] <= 0.08939755335450172) {
        votes[0] += 1;
    }

    else {
        if (x[6] <= 0.1952848806977272) {
            if (x[8] <= 0.26722465455532074) {
                if (x[3] <= 85.5) {
                    votes[0] += 1;
                }

                else {
                    votes[1] += 1;
                }
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[6] <= 0.27297917008399963) {
                    if (x[7] <= 0.15301983058452606) {
                        if (x[2] <= 105.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[6] <= 0.44674208760261536) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[2] <= 80.5) {
                            votes[0] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }

            else {
                if (x[4] <= 78.5) {
                    if (x[8] <= 0.5543814301490784) {
                        votes[2] += 1;
                    }

                    else {
                        if (x[7] <= 0.20230832695960999) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }

                else {
                    votes[2] += 1;
                }
            }
        }
    }

    // tree #4
    if (x[6] <= 0.20362336933612823) {
        if (x[7] <= 0.1259133778512478) {
            if (x[4] <= 106.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[8] <= 0.5021437704563141) {
            if (x[8] <= 0.2500763237476349) {
                votes[0] += 1;
            }

            else {
                if (x[6] <= 0.27297917008399963) {
                    if (x[7] <= 0.15301983058452606) {
                        if (x[4] <= 105.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[6] <= 0.44674208760261536) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[7] <= 0.12093666195869446) {
                            votes[0] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }
        }

        else {
            if (x[5] <= 78.5) {
                if (x[8] <= 0.5543814301490784) {
                    votes[2] += 1;
                }

                else {
                    if (x[6] <= 0.33735930919647217) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }

            else {
                votes[2] += 1;
            }
        }
    }

    // tree #5
    if (x[6] <= 0.20362336933612823) {
        if (x[7] <= 0.1259133778512478) {
            if (x[9] <= 106.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[8] <= 0.5021437704563141) {
            if (x[7] <= 0.08939755335450172) {
                votes[0] += 1;
            }

            else {
                if (x[6] <= 0.27297917008399963) {
                    if (x[8] <= 0.38244062662124634) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[6] <= 0.21952588856220245) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }

                else {
                    if (x[11] <= 18.0) {
                        votes[0] += 1;
                    }

                    else {
                        if (x[2] <= 136.0) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }
        }

        else {
            if (x[3] <= 78.5) {
                if (x[8] <= 0.5543814301490784) {
                    votes[2] += 1;
                }

                else {
                    if (x[7] <= 0.20230832695960999) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }

            else {
                votes[2] += 1;
            }
        }
    }

    // tree #6
    if (x[6] <= 0.20362336933612823) {
        if (x[7] <= 0.1259133778512478) {
            if (x[1] <= 106.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[7] <= 0.1913100853562355) {
            if (x[1] <= 134.0) {
                if (x[3] <= 53.5) {
                    if (x[7] <= 0.12689630687236786) {
                        if (x[6] <= 0.3374037742614746) {
                            if (x[8] <= 0.20776142925024033) {
                                votes[0] += 1;
                            }

                            else {
                                votes[3] += 1;
                            }
                        }

                        else {
                            votes[0] += 1;
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[6] <= 0.2658356875181198) {
                        if (x[4] <= 105.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        if (x[8] <= 0.574612557888031) {
                            votes[3] += 1;
                        }

                        else {
                            if (x[1] <= 79.5) {
                                votes[3] += 1;
                            }

                            else {
                                votes[2] += 1;
                            }
                        }
                    }
                }
            }

            else {
                votes[2] += 1;
            }
        }

        else {
            votes[2] += 1;
        }
    }

    // tree #7
    if (x[7] <= 0.08939755335450172) {
        votes[0] += 1;
    }

    else {
        if (x[6] <= 0.1952848806977272) {
            if (x[8] <= 0.26722465455532074) {
                if (x[0] <= 85.5) {
                    votes[0] += 1;
                }

                else {
                    votes[1] += 1;
                }
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[6] <= 0.27297917008399963) {
                    if (x[7] <= 0.15301983058452606) {
                        if (x[0] <= 105.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[10] <= 18.0) {
                        votes[0] += 1;
                    }

                    else {
                        if (x[6] <= 0.45116379857063293) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }

            else {
                if (x[8] <= 0.5543814301490784) {
                    votes[2] += 1;
                }

                else {
                    if (x[5] <= 78.5) {
                        if (x[8] <= 0.6410063803195953) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }
        }
    }

    // tree #8
    if (x[6] <= 0.20362336933612823) {
        if (x[7] <= 0.1259133778512478) {
            if (x[2] <= 106.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[8] <= 0.5021437704563141) {
            if (x[7] <= 0.08939755335450172) {
                votes[0] += 1;
            }

            else {
                if (x[6] <= 0.27297917008399963) {
                    if (x[8] <= 0.38244062662124634) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[6] <= 0.21952588856220245) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }

                else {
                    if (x[6] <= 0.44674208760261536) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[10] <= 80.5) {
                            votes[0] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }
        }

        else {
            if (x[8] <= 0.5543814301490784) {
                votes[2] += 1;
            }

            else {
                if (x[9] <= 78.5) {
                    if (x[8] <= 0.6410063803195953) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    votes[2] += 1;
                }
            }
        }
    }

    // tree #9
    if (x[6] <= 0.20362336933612823) {
        if (x[7] <= 0.1259133778512478) {
            if (x[10] <= 106.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[10] <= 134.0) {
            if (x[7] <= 0.1913100853562355) {
                if (x[1] <= 53.5) {
                    if (x[7] <= 0.12689630687236786) {
                        if (x[7] <= 0.09156909584999084) {
                            votes[0] += 1;
                        }

                        else {
                            if (x[9] <= 18.0) {
                                votes[0] += 1;
                            }

                            else {
                                votes[3] += 1;
                            }
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[6] <= 0.2658356875181198) {
                        if (x[0] <= 105.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        if (x[8] <= 0.574612557888031) {
                            votes[3] += 1;
                        }

                        else {
                            if (x[1] <= 79.5) {
                                votes[3] += 1;
                            }

                            else {
                                votes[2] += 1;
                            }
                        }
                    }
                }
            }

            else {
                votes[2] += 1;
            }
        }

        else {
            votes[2] += 1;
        }
    }

    // tree #10
    if (x[6] <= 0.20362336933612823) {
        if (x[7] <= 0.1259133778512478) {
            if (x[1] <= 106.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[8] <= 0.5021437704563141) {
            if (x[8] <= 0.2500763237476349) {
                votes[0] += 1;
            }

            else {
                if (x[6] <= 0.27297917008399963) {
                    if (x[7] <= 0.15301983058452606) {
                        if (x[5] <= 105.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[11] <= 18.0) {
                        votes[0] += 1;
                    }

                    else {
                        if (x[3] <= 136.0) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }
        }

        else {
            if (x[3] <= 78.5) {
                if (x[8] <= 0.5543814301490784) {
                    votes[2] += 1;
                }

                else {
                    if (x[6] <= 0.33735930919647217) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }

            else {
                votes[2] += 1;
            }
        }
    }

    // return argmax of votes
    uint8_t classIdx = 0;
    float maxVotes = votes[0];

    for (uint8_t i = 1; i < 4; i++) {
        if (votes[i] > maxVotes) {
            classIdx = i;
            maxVotes = votes[i];
        }
    }

    return classIdx;
};
/**
* Predict readable class name
*/
const char* predictLabel(float *x) {
    return idxToLabel(predict(x));
};
/**
* Convert class idx to readable name
*/
const char* idxToLabel(uint8_t classIdx) {
    switch (classIdx) {
        case 0:
        return "espera";
        case 1:
        return "primer movimiento 2 cuartos";
        case 2:
        return "segundo movimiento 3 cuartos";
        case 3:
        return "tercer movimiento 4 cuartos";
        default:
        return "Peña, una consulta por favor";
    }
};