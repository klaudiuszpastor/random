// Camera stream and feature extraction

#include "../inc/vision_analysis.h"

visionAnalysis::visionAnalysis()
{
    projectUtils::logStatus("Vision Analysis component initialized.",
                                projectUtils::logLevel::STATUS);
}

cv::Mat visionAnalysis::generateSkinMask(const cv::Mat& bgrImage)
{
    if (bgrImage.empty())
    {
        projectUtils::logStatus("Input image is empty.",
                                    projectUtils::logLevel::ERROR);
        return cv::Mat();
    }

    projectUtils::logStatus("Generating skin mask placeholder.", projectUtils::logLevel::STATUS);
    return bgrImage.clone();
}
