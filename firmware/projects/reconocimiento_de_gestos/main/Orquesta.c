#include "Orquesta.h"

/**
* Predict class for features vector
*/
int predict(float *x) {
    uint8_t votes[4] = { 0 };
    // tree #1
    if (x[11] <= 0.26613976061344147) {
        if (x[8] <= 85.5) {
            votes[0] += 1;
        }

        else {
            if (x[7] <= 58.0) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }
    }

    else {
        if (x[9] <= 0.1473548337817192) {
            if (x[8] <= 19.5) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[5] <= 1.1749999523162842) {
                if (x[6] <= 156.0) {
                    if (x[0] <= 0.008666666690260172) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[1] <= 0.0024999999441206455) {
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
                if (x[11] <= 0.43478260934352875) {
                    if (x[11] <= 0.35181164741516113) {
                        votes[0] += 1;
                    }

                    else {
                        votes[3] += 1;
                    }
                }

                else {
                    if (x[9] <= 0.20376970618963242) {
                        votes[1] += 1;
                    }

                    else {
                        if (x[10] <= 0.16702331602573395) {
                            votes[2] += 1;
                        }

                        else {
                            if (x[10] <= 0.19996266812086105) {
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
    }

    // tree #2
    if (x[11] <= 0.26613976061344147) {
        if (x[2] <= -0.005027777631767094) {
            votes[1] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 0.1473548337817192) {
            if (x[10] <= 0.08267807960510254) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[11] <= 0.5035591125488281) {
                if (x[6] <= 156.0) {
                    if (x[0] <= 0.008666666690260172) {
                        if (x[9] <= 0.18422697484493256) {
                            votes[0] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }

                    else {
                        if (x[1] <= 0.0024999999441206455) {
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
                if (x[2] <= -0.0022500001068692654) {
                    votes[2] += 1;
                }

                else {
                    if (x[6] <= 104.5) {
                        if (x[2] <= 0.007583333179354668) {
                            votes[3] += 1;
                        }

                        else {
                            if (x[8] <= 64.0) {
                                votes[2] += 1;
                            }

                            else {
                                votes[1] += 1;
                            }
                        }
                    }

                    else {
                        votes[2] += 1;
                    }
                }
            }
        }
    }

    // tree #3
    if (x[9] <= 0.14847218990325928) {
        if (x[11] <= 0.27504701912403107) {
            if (x[8] <= 68.5) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[10] <= 0.08267807960510254) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }
    }

    else {
        if (x[11] <= 0.25831739604473114) {
            votes[0] += 1;
        }

        else {
            if (x[11] <= 0.5035591125488281) {
                if (x[0] <= -0.0003333333370392211) {
                    votes[3] += 1;
                }

                else {
                    if (x[6] <= 103.0) {
                        if (x[3] <= 0.4999999850988388) {
                            votes[2] += 1;
                        }

                        else {
                            if (x[10] <= 0.07552462071180344) {
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
            }

            else {
                if (x[2] <= -0.0022500001068692654) {
                    votes[2] += 1;
                }

                else {
                    if (x[6] <= 104.5) {
                        if (x[10] <= 0.24331261217594147) {
                            votes[3] += 1;
                        }

                        else {
                            if (x[3] <= 0.6449999809265137) {
                                votes[1] += 1;
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
    }

    // tree #4
    if (x[11] <= 0.26613976061344147) {
        if (x[2] <= -0.005027777631767094) {
            votes[1] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 0.1473548337817192) {
            if (x[10] <= 0.08267807960510254) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[5] <= 1.1749999523162842) {
                if (x[0] <= -0.00027777778086601757) {
                    votes[3] += 1;
                }

                else {
                    if (x[6] <= 104.0) {
                        if (x[7] <= 134.5) {
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

            else {
                if (x[9] <= 0.20376970618963242) {
                    if (x[3] <= 0.6949999928474426) {
                        votes[1] += 1;
                    }

                    else {
                        votes[0] += 1;
                    }
                }

                else {
                    if (x[11] <= 0.43478260934352875) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[7] <= 91.0) {
                            if (x[0] <= 0.007250000024214387) {
                                if (x[10] <= 0.20763222873210907) {
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
                            votes[2] += 1;
                        }
                    }
                }
            }
        }
    }

    // tree #5
    if (x[11] <= 0.26613976061344147) {
        if (x[2] <= -0.005027777631767094) {
            votes[1] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[3] <= 0.3799999952316284) {
            if (x[8] <= 19.5) {
                votes[0] += 1;
            }

            else {
                if (x[0] <= 0.006999999983236194) {
                    votes[1] += 1;
                }

                else {
                    votes[2] += 1;
                }
            }
        }

        else {
            if (x[11] <= 0.4993947148323059) {
                if (x[6] <= 156.0) {
                    if (x[9] <= 0.18104712665081024) {
                        if (x[1] <= 0.0006111111288191751) {
                            votes[0] += 1;
                        }

                        else {
                            votes[2] += 1;
                        }
                    }

                    else {
                        if (x[3] <= 1.0600000023841858) {
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
                if (x[6] <= 103.5) {
                    if (x[6] <= 84.0) {
                        if (x[4] <= 0.6599999964237213) {
                            votes[2] += 1;
                        }

                        else {
                            votes[1] += 1;
                        }
                    }

                    else {
                        if (x[11] <= 0.645135760307312) {
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

    // tree #6
    if (x[11] <= 0.26613976061344147) {
        if (x[2] <= -0.005027777631767094) {
            votes[1] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 0.1473548337817192) {
            if (x[10] <= 0.08267807960510254) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[11] <= 0.5035591125488281) {
                if (x[6] <= 156.0) {
                    if (x[0] <= 0.008666666690260172) {
                        if (x[10] <= 0.062191981822252274) {
                            votes[0] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }

                    else {
                        if (x[1] <= 0.0024999999441206455) {
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
                if (x[4] <= 0.42499999701976776) {
                    votes[2] += 1;
                }

                else {
                    if (x[1] <= 0.0004722222365671769) {
                        votes[2] += 1;
                    }

                    else {
                        if (x[11] <= 0.5577256977558136) {
                            if (x[10] <= 0.28619977831840515) {
                                votes[2] += 1;
                            }

                            else {
                                votes[1] += 1;
                            }
                        }

                        else {
                            votes[3] += 1;
                        }
                    }
                }
            }
        }
    }

    // tree #7
    if (x[11] <= 0.26613976061344147) {
        if (x[2] <= -0.005027777631767094) {
            votes[1] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 0.1473548337817192) {
            if (x[10] <= 0.08267807960510254) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[11] <= 0.5035591125488281) {
                if (x[6] <= 156.0) {
                    if (x[9] <= 0.18104712665081024) {
                        if (x[3] <= 0.6949999928474426) {
                            votes[2] += 1;
                        }

                        else {
                            votes[0] += 1;
                        }
                    }

                    else {
                        if (x[5] <= 1.3650000095367432) {
                            if (x[3] <= 1.0600000023841858) {
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

                else {
                    votes[2] += 1;
                }
            }

            else {
                if (x[2] <= -0.0022500001068692654) {
                    votes[2] += 1;
                }

                else {
                    if (x[6] <= 104.5) {
                        if (x[4] <= 0.6649999916553497) {
                            votes[3] += 1;
                        }

                        else {
                            if (x[11] <= 0.6069234609603882) {
                                votes[1] += 1;
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
    }

    // tree #8
    if (x[11] <= 0.26613976061344147) {
        if (x[2] <= -0.005027777631767094) {
            votes[1] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 0.1473548337817192) {
            if (x[10] <= 0.08267807960510254) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[11] <= 0.5035591125488281) {
                if (x[6] <= 156.0) {
                    if (x[0] <= 0.008666666690260172) {
                        if (x[9] <= 0.18422697484493256) {
                            votes[0] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }

                    else {
                        if (x[1] <= 0.0024999999441206455) {
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
                if (x[2] <= -0.0022500001068692654) {
                    votes[2] += 1;
                }

                else {
                    if (x[11] <= 0.6385021805763245) {
                        if (x[3] <= 0.6500000059604645) {
                            if (x[10] <= 0.262151874601841) {
                                votes[2] += 1;
                            }

                            else {
                                votes[1] += 1;
                            }
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

    // tree #9
    if (x[11] <= 0.26613976061344147) {
        if (x[2] <= -0.005027777631767094) {
            votes[1] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 0.1473548337817192) {
            if (x[10] <= 0.08267807960510254) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[5] <= 1.1749999523162842) {
                if (x[6] <= 156.0) {
                    if (x[0] <= 0.008666666690260172) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[1] <= 0.0024999999441206455) {
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
                if (x[9] <= 0.20376970618963242) {
                    if (x[0] <= 0.0016944444287219085) {
                        votes[0] += 1;
                    }

                    else {
                        votes[1] += 1;
                    }
                }

                else {
                    if (x[6] <= 8.0) {
                        votes[3] += 1;
                    }

                    else {
                        if (x[10] <= 0.16702331602573395) {
                            votes[2] += 1;
                        }

                        else {
                            if (x[10] <= 0.19996266812086105) {
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
    }

    // tree #10
    if (x[11] <= 0.26613976061344147) {
        if (x[2] <= -0.005027777631767094) {
            votes[1] += 1;
        }

        else {
            votes[0] += 1;
        }
    }

    else {
        if (x[9] <= 0.1473548337817192) {
            if (x[10] <= 0.08267807960510254) {
                votes[0] += 1;
            }

            else {
                votes[1] += 1;
            }
        }

        else {
            if (x[11] <= 0.5035591125488281) {
                if (x[6] <= 156.0) {
                    if (x[0] <= 0.008666666690260172) {
                        if (x[8] <= 17.0) {
                            votes[0] += 1;
                        }

                        else {
                            votes[3] += 1;
                        }
                    }

                    else {
                        if (x[1] <= 0.0024999999441206455) {
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
                if (x[2] <= -0.0022500001068692654) {
                    votes[2] += 1;
                }

                else {
                    if (x[6] <= 104.5) {
                        if (x[10] <= 0.24331261217594147) {
                            votes[3] += 1;
                        }

                        else {
                            if (x[5] <= 1.5299999713897705) {
                                votes[1] += 1;
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
        return "primer_mov_2cuartos";
        case 2:
        return "segundo_mov_3cuartos";
        case 3:
        return "tercer_mov_4cuartos";
        default:
        return "Houston we have a problem";
    }
};