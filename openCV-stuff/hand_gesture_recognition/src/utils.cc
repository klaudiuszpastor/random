#include "../inc/utils.h"

namespace projectUtils
{
    std::string logLevelType(logLevel status)
    {
        switch (status)
        {
            case logLevel::STATUS:
                return "[STATUS] "; 

            case logLevel::ERROR:
                return "[ERROR] ";

            default:
                return "[UNKNOWN] ";
        }
    }

    void logStatus(const std::string& message, logLevel status)
    {
        std::string statusString = logLevelType(status);

        std::cout << statusString << message << std::endl;
    }
}
