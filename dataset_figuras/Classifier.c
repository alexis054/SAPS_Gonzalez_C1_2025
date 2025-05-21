#include "Classifier.h"

/**
* Predict class for features vector
*/
int predict(float *x) {
    uint8_t votes[4] = { 0 };
    // tree #1
    if (x[10] <= 0.9881999790668488) {
        if (x[8] <= 0.35324160754680634) {
            if (x[0] <= -0.010805555852130055) {
                votes[3] += 1;
            }

            else {
                votes[0] += 1;
            }
        }

        else {
            votes[3] += 1;
        }
    }

    else {
        if (x[9] <= 4.0309998989105225) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[4] <= 0.4449999928474426) {
                    if (x[6] <= 0.45116379857063293) {
                        if (x[0] <= 0.013749999925494194) {
                            votes[3] += 1;
                        }

                        else {
                            if (x[6] <= 0.3086165338754654) {
                                votes[2] += 1;
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
                    if (x[6] <= 0.2869444638490677) {
                        votes[2] += 1;
                    }

                    else {
                        if (x[1] <= 0.0013333332899492234) {
                            votes[3] += 1;
                        }

                        else {
                            votes[0] += 1;
                        }
                    }
                }
            }

            else {
                if (x[2] <= -0.002361111080972478) {
                    votes[2] += 1;
                }

                else {
                    if (x[2] <= 0.012305555399507284) {
                        if (x[10] <= 3.891200065612793) {
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

    // tree #2
    if (x[10] <= 0.9881999790668488) {
        if (x[11] <= 11.217249870300293) {
            if (x[0] <= -0.010805555852130055) {
                votes[3] += 1;
            }

            else {
                votes[0] += 1;
            }
        }

        else {
            votes[3] += 1;
        }
    }

    else {
        if (x[9] <= 4.0309998989105225) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[0] <= 0.008694444317370653) {
                    if (x[5] <= 1.4549999833106995) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
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
                    if (x[1] <= 0.005888888845220208) {
                        if (x[2] <= 0.0009444444731343538) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        if (x[4] <= 0.42499999701976776) {
                            votes[2] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }
                }
            }
        }
    }

    // tree #3
    if (x[10] <= 0.9881999790668488) {
        if (x[0] <= -0.00636111106723547) {
            votes[3] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[6] <= 0.1952848806977272) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[0] <= 0.008694444317370653) {
                    if (x[9] <= 17.957449436187744) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }

                else {
                    if (x[8] <= 0.38739846646785736) {
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
                    if (x[1] <= 0.005888888845220208) {
                        if (x[2] <= 0.0009444444731343538) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        if (x[7] <= 0.15378276258707047) {
                            votes[2] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }
                }
            }
        }
    }

    // tree #4
    if (x[10] <= 0.9881999790668488) {
        if (x[0] <= -0.00636111106723547) {
            votes[3] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[6] <= 0.1952848806977272) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[0] <= 0.008694444317370653) {
                    if (x[6] <= 0.44674208760261536) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }

                else {
                    if (x[11] <= 13.386650085449219) {
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
                        if (x[7] <= 0.20230832695960999) {
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

    // tree #5
    if (x[10] <= 0.9881999790668488) {
        if (x[0] <= -0.00636111106723547) {
            votes[3] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 4.0309998989105225) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[4] <= 0.4449999928474426) {
                    if (x[0] <= 0.008694444317370653) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[0] <= 0.019027777947485447) {
                            votes[2] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }
                }

                else {
                    if (x[0] <= 0.006388888810761273) {
                        if (x[11] <= 18.11234951019287) {
                            votes[3] += 1;
                        }

                        else {
                            votes[0] += 1;
                        }
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
                    if (x[1] <= 0.005888888845220208) {
                        if (x[2] <= 0.0009444444731343538) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        if (x[7] <= 0.15378276258707047) {
                            votes[2] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }
                }
            }
        }
    }

    // tree #6
    if (x[10] <= 0.9881999790668488) {
        if (x[11] <= 11.217249870300293) {
            if (x[1] <= 0.003888888983055949) {
                votes[0] += 1;
            }

            else {
                votes[3] += 1;
            }
        }

        else {
            votes[3] += 1;
        }
    }

    else {
        if (x[6] <= 0.1952848806977272) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[4] <= 0.4449999928474426) {
                    if (x[3] <= 0.9850000143051147) {
                        if (x[0] <= 0.013749999925494194) {
                            votes[3] += 1;
                        }

                        else {
                            if (x[8] <= 0.39909982681274414) {
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

                else {
                    if (x[9] <= 7.988149881362915) {
                        votes[2] += 1;
                    }

                    else {
                        if (x[4] <= 0.47999998927116394) {
                            votes[0] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }
                }
            }

            else {
                if (x[1] <= 0.005888888845220208) {
                    if (x[11] <= 35.88479995727539) {
                        votes[2] += 1;
                    }

                    else {
                        if (x[8] <= 0.645135760307312) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }

                else {
                    if (x[10] <= 2.5532500743865967) {
                        votes[2] += 1;
                    }

                    else {
                        votes[3] += 1;
                    }
                }
            }
        }
    }

    // tree #7
    if (x[10] <= 0.9881999790668488) {
        if (x[8] <= 0.35324160754680634) {
            if (x[0] <= -0.010805555852130055) {
                votes[3] += 1;
            }

            else {
                votes[0] += 1;
            }
        }

        else {
            votes[3] += 1;
        }
    }

    else {
        if (x[6] <= 0.1952848806977272) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[0] <= 0.008694444317370653) {
                    if (x[5] <= 1.4549999833106995) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }

                else {
                    if (x[11] <= 13.386650085449219) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }

            else {
                if (x[1] <= 0.005888888845220208) {
                    if (x[11] <= 35.88479995727539) {
                        votes[2] += 1;
                    }

                    else {
                        if (x[8] <= 0.645135760307312) {
                            votes[3] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }
                }

                else {
                    if (x[4] <= 0.42499999701976776) {
                        votes[2] += 1;
                    }

                    else {
                        votes[3] += 1;
                    }
                }
            }
        }
    }

    // tree #8
    if (x[10] <= 0.9881999790668488) {
        if (x[11] <= 11.217249870300293) {
            if (x[0] <= -0.010805555852130055) {
                votes[3] += 1;
            }

            else {
                votes[0] += 1;
            }
        }

        else {
            votes[3] += 1;
        }
    }

    else {
        if (x[9] <= 4.0309998989105225) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[0] <= 0.008694444317370653) {
                    if (x[3] <= 1.375) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }

                else {
                    if (x[8] <= 0.38739846646785736) {
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
                        if (x[7] <= 0.20230832695960999) {
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

    // tree #9
    if (x[10] <= 0.9881999790668488) {
        if (x[0] <= -0.00636111106723547) {
            votes[3] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 4.0309998989105225) {
            votes[1] += 1;
        }

        else {
            if (x[2] <= -0.0012500000302679837) {
                if (x[8] <= 0.5035591125488281) {
                    if (x[6] <= 0.27953147888183594) {
                        votes[2] += 1;
                    }

                    else {
                        if (x[6] <= 0.43798570334911346) {
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

                else {
                    votes[2] += 1;
                }
            }

            else {
                if (x[2] <= 0.016833333298563957) {
                    if (x[10] <= 3.4775500297546387) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }

                else {
                    if (x[0] <= -0.002305555623024702) {
                        votes[3] += 1;
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }
        }
    }

    // tree #10
    if (x[10] <= 0.9881999790668488) {
        if (x[0] <= -0.00636111106723547) {
            votes[3] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[6] <= 0.1952848806977272) {
            votes[1] += 1;
        }

        else {
            if (x[8] <= 0.5021437704563141) {
                if (x[0] <= 0.008694444317370653) {
                    if (x[9] <= 17.957449436187744) {
                        votes[3] += 1;
                    }

                    else {
                        votes[0] += 1;
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