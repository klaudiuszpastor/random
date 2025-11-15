#include "../inc/utils.h"
#include "../inc/vision_analysis.h"

int main()
{
    projectUtils::logStatus("Hand Gesture Recognition Project starting up.",
                            projectUtils::logLevel::STATUS);

    visionAnalysis analyzer;

    cv::Mat testImage = cv::imread("test_image.jpg");

    if (testImage.empty()) 
    {
        projectUtils::logStatus("Warning: Could not load test_image.jpg. Using a dummy image.", 
                                projectUtils::logLevel::STATUS);

        // Create a dummy image if file not found
        testImage = cv::Mat(100, 100, CV_8UC3, cv::Scalar(0, 255, 0)); 
    }

    // 3. Process the image
    cv::Mat mask = analyzer.generateSkinMask(testImage);

    projectUtils::logStatus("Processing complete. Mask dimensions: " + 
                             std::to_string(mask.rows) + "x" + std::to_string(mask.cols),
                            projectUtils::logLevel::STATUS);
    
    // Note: cv::imshow will require cv::waitKey(0) and a highgui dependency to show a window.

    return 0;
}
