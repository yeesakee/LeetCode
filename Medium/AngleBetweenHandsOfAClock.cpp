/*
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
Answers within 10-5 of the actual value will be accepted as correct.

Example 1:
    Input: hour = 12, minutes = 30
    Output: 165
Example 2:
    Input: hour = 3, minutes = 30
    Output: 75
Example 3:
    Input: hour = 3, minutes = 15
    Output: 7.5

Constraints:
    1 <= hour <= 12
    0 <= minutes <= 59
*/

#include <math.h>

class Solution {
public:
    double angleClock(int hour, int minutes) {
        int per_minute_degree = 360/60;
        int per_hour_degree = 360/12;
        double hour_position = (hour%12 + (double)minutes/60) * per_hour_degree;
        double minutes_position = minutes * per_minute_degree;
        double angle = abs(hour_position - minutes_position);
        if (angle > 180) {
            return (double)(360 - angle);
        }
        return angle;
        
    }
};