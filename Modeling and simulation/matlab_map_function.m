function mapped_value = map_value(value)
%MAP_VALUE maps a value from one range to another

    from_low=-50;
    from_high= 50;
    to_low=30;
    to_high=160;
    % Avoid division by zero
    if (from_high - from_low) == 0
        mapped_value = to_low;
        return;
    end

    % mapping equation
    mapped_value = (value - from_low) / (from_high - from_low) * ...
                   (to_high - to_low) + to_low;
end
