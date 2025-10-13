#include <iostream>
#include <opencv2/opencv.hpp>

int main() {
  std::cout << "OpenCV Version: " << CV_VERSION << std::endl;

  cv::Mat image = cv::imread("lena.jpg"); 

  if (image.empty()) {
      std::cerr << "Error: Could not load image." << std::endl;
      return -1;
  }

  cv::imshow("Hello OpenCV", image);
  cv::waitKey(0);
  return 0;
}
