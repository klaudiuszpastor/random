#pragma once

#include <opencv2/opencv.hpp>
#include "utils.h"

class visionAnalysis
{
public:
    visionAnalysis();

    cv::Mat generateSkinMask(const cv::Mat& bgrImage);

private:

};
