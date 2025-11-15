#pragma once

#include <iostream>
#include <string>

namespace projectUtils
{
    enum class logLevel
    {
      STATUS,
      ERROR

    };

    void logStatus(const std::string& message, logLevel status);

    std::string logLevelType(logLevel status);
}
