#include "Classifier.h"

/**
* Predict class for features vector
*/
int predict(float *x) {
    uint8_t votes[4] = { 0 };
    // tree #1
    if (x[9] <= 0.20362336933612823) {
        if (x[10] <= 0.1259133778512478) {
            if (x[8] <= 106.0) {
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
        if (x[11] <= 0.5021437704563141) {
            if (x[0] <= 0.008694444317370653) {
                if (x[3] <= 1.1150000095367432) {
                    if (x[5] <= 0.5499999970197678) {
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
                if (x[11] <= 0.38739846646785736) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[1] <= 0.005888888845220208) {
                if (x[3] <= 0.929999977350235) {
                    votes[2] += 1;
                }

                else {
                    if (x[11] <= 0.5730530619621277) {
                        votes[2] += 1;
                    }

                    else {
                        votes[3] += 1;
                    }
                }
            }

            else {
                if (x[9] <= 0.3334805965423584) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }
    }

    // tree #2
    if (x[9] <= 0.20362336933612823) {
        if (x[10] <= 0.1259133778512478) {
            if (x[8] <= 106.0) {
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
        if (x[11] <= 0.5021437704563141) {
            if (x[0] <= 0.008694444317370653) {
                if (x[11] <= 0.2500763237476349) {
                    votes[0] += 1;
                }

                else {
                    if (x[8] <= 18.0) {
                        votes[0] += 1;
                    }

                    else {
                        votes[3] += 1;
                    }
                }
            }

            else {
                if (x[5] <= 0.7700000107288361) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[2] <= -0.002361111080972478) {
                votes[2] += 1;
            }

            else {
                if (x[2] <= 0.012305555399507284) {
                    if (x[0] <= -0.0084166667656973) {
                        votes[2] += 1;
                    }

                    else {
                        votes[3] += 1;
                    }
                }

                else {
                    votes[2] += 1;
                }
            }
        }
    }

    // tree #3
    if (x[9] <= 0.20362336933612823) {
        if (x[4] <= 0.3150000125169754) {
            if (x[8] <= 104.0) {
                if (x[10] <= 0.1304033286869526) {
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
            votes[1] += 1;
        }
    }

    else {
        if (x[11] <= 0.5021437704563141) {
            if (x[0] <= 0.008694444317370653) {
                if (x[11] <= 0.2500763237476349) {
                    votes[0] += 1;
                }

                else {
                    if (x[5] <= 1.4549999833106995) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }
            }

            else {
                if (x[11] <= 0.38739846646785736) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[2] <= -0.002361111080972478) {
                votes[2] += 1;
            }

            else {
                if (x[2] <= 0.012305555399507284) {
                    if (x[7] <= 96.5) {
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

    // tree #4
    if (x[9] <= 0.20362336933612823) {
        if (x[10] <= 0.1259133778512478) {
            if (x[8] <= 106.0) {
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
        if (x[11] <= 0.5021437704563141) {
            if (x[0] <= 0.008694444317370653) {
                if (x[11] <= 0.2500763237476349) {
                    votes[0] += 1;
                }

                else {
                    if (x[9] <= 0.44674208760261536) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }
            }

            else {
                if (x[5] <= 0.7700000107288361) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[2] <= -0.002361111080972478) {
                votes[2] += 1;
            }

            else {
                if (x[2] <= 0.012305555399507284) {
                    if (x[8] <= 38.0) {
                        votes[2] += 1;
                    }

                    else {
                        votes[3] += 1;
                    }
                }

                else {
                    votes[2] += 1;
                }
            }
        }
    }

    // tree #5
    if (x[9] <= 0.20362336933612823) {
        if (x[10] <= 0.1259133778512478) {
            if (x[2] <= -0.005083333235234022) {
                votes[1] += 1;
            }

            else {
                votes[0] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[11] <= 0.5021437704563141) {
            if (x[0] <= 0.008694444317370653) {
                if (x[11] <= 0.2500763237476349) {
                    votes[0] += 1;
                }

                else {
                    if (x[9] <= 0.44674208760261536) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }
            }

            else {
                if (x[5] <= 0.7700000107288361) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[2] <= -0.002361111080972478) {
                votes[2] += 1;
            }

            else {
                if (x[2] <= 0.012305555399507284) {
                    if (x[6] <= 125.0) {
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

    // tree #6
    if (x[9] <= 0.20362336933612823) {
        if (x[10] <= 0.1259133778512478) {
            if (x[2] <= -0.005083333235234022) {
                votes[1] += 1;
            }

            else {
                votes[0] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[11] <= 0.5021437704563141) {
            if (x[0] <= 0.008694444317370653) {
                if (x[3] <= 1.1150000095367432) {
                    if (x[10] <= 0.08211669325828552) {
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
                if (x[11] <= 0.38739846646785736) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[2] <= -0.002361111080972478) {
                votes[2] += 1;
            }

            else {
                if (x[6] <= 105.5) {
                    if (x[4] <= 0.6949999928474426) {
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

    // tree #7
    if (x[9] <= 0.20362336933612823) {
        if (x[10] <= 0.1259133778512478) {
            if (x[2] <= -0.005083333235234022) {
                votes[1] += 1;
            }

            else {
                votes[0] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[5] <= 1.1749999523162842) {
            if (x[0] <= -0.001472222211305052) {
                votes[3] += 1;
            }

            else {
                if (x[3] <= 0.6599999964237213) {
                    votes[2] += 1;
                }

                else {
                    if (x[10] <= 0.1311853975057602) {
                        if (x[1] <= 0.0015555555582977831) {
                            votes[0] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[3] += 1;
                    }
                }
            }
        }

        else {
            if (x[11] <= 0.47498151659965515) {
                if (x[3] <= 1.1299999952316284) {
                    votes[3] += 1;
                }

                else {
                    votes[0] += 1;
                }
            }

            else {
                if (x[2] <= -0.002361111080972478) {
                    votes[2] += 1;
                }

                else {
                    if (x[1] <= -0.0004444444493856281) {
                        votes[2] += 1;
                    }

                    else {
                        if (x[6] <= 113.5) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }
            }
        }
    }

    // tree #8
    if (x[9] <= 0.20362336933612823) {
        if (x[10] <= 0.1259133778512478) {
            if (x[8] <= 106.0) {
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
        if (x[5] <= 1.1749999523162842) {
            if (x[0] <= -0.001472222211305052) {
                votes[3] += 1;
            }

            else {
                if (x[3] <= 0.6599999964237213) {
                    votes[2] += 1;
                }

                else {
                    if (x[10] <= 0.1311853975057602) {
                        if (x[1] <= 0.0015555555582977831) {
                            votes[0] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        votes[3] += 1;
                    }
                }
            }
        }

        else {
            if (x[2] <= -0.005277777789160609) {
                votes[2] += 1;
            }

            else {
                if (x[2] <= 0.012305555399507284) {
                    if (x[9] <= 0.34502314031124115) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[2] <= -0.004777777707204223) {
                            votes[0] += 1;
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

    // tree #9
    if (x[9] <= 0.20362336933612823) {
        if (x[10] <= 0.1259133778512478) {
            if (x[2] <= -0.005083333235234022) {
                votes[1] += 1;
            }

            else {
                votes[0] += 1;
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[11] <= 0.5021437704563141) {
            if (x[0] <= 0.008694444317370653) {
                if (x[11] <= 0.2500763237476349) {
                    votes[0] += 1;
                }

                else {
                    if (x[5] <= 1.4549999833106995) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }
            }

            else {
                if (x[11] <= 0.38739846646785736) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[2] <= -0.002361111080972478) {
                votes[2] += 1;
            }

            else {
                if (x[2] <= 0.012305555399507284) {
                    if (x[5] <= 1.465000033378601) {
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

    // tree #10
    if (x[9] <= 0.20362336933612823) {
        if (x[4] <= 0.3150000125169754) {
            if (x[2] <= -0.004444444552063942) {
                votes[1] += 1;
            }

            else {
                if (x[10] <= 0.1305241622030735) {
                    votes[0] += 1;
                }

                else {
                    votes[1] += 1;
                }
            }
        }

        else {
            votes[1] += 1;
        }
    }

    else {
        if (x[11] <= 0.5021437704563141) {
            if (x[0] <= 0.008694444317370653) {
                if (x[10] <= 0.08939755335450172) {
                    votes[0] += 1;
                }

                else {
                    if (x[8] <= 18.0) {
                        votes[0] += 1;
                    }

                    else {
                        votes[3] += 1;
                    }
                }
            }

            else {
                if (x[11] <= 0.38739846646785736) {
                    votes[3] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[2] <= -0.002361111080972478) {
                votes[2] += 1;
            }

            else {
                if (x[2] <= 0.012305555399507284) {
                    if (x[9] <= 0.3454544246196747) {
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
        return "espera - espera.csv - espera - espera.csv.csv";
        case 1:
        return "primer_mov_2cuartos  - primer_mov_2cuartos .csv - primer_mov_2cuartos  - primer_mov_2cuartos .csv.csv";
        case 2:
        return "segundo_mov_3cuartos - segundo_mov_3cuartos.csv - segundo_mov_3cuartos - segundo_mov_3cuartos.csv.csv";
        case 3:
        return "tercer_mov_4cuartos - tercer_mov_4cuartos.csv";
        default:
        return "Houston we have a problem";
    }
};