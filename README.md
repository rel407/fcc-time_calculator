# Time Calculator

## Project Overview
This project is part of the freeCodeCamp curriculum and focuses on creating a time calculator function. The function, `add_time`, takes in a start time, a duration time, and optionally a starting day of the week. It computes the new time after adding the duration and returns the updated time in a readable format.

## Usage

### Function Definition:
```python
def add_time(start, duration, sday='')
```

## Parameters

- **start**: A string representing the start time in 12-hour format (e.g., `"3:00 PM"`).
- **duration**: A string representing the number of hours and minutes to be added (e.g., `"3:10"`).
- **sday** *(optional)*: A case-insensitive string representing the starting day of the week (e.g., `"Monday"`).

## Expected Output

- The function returns a formatted string showing the updated time.
- If the new time falls on the next day, it includes `"(next day)"`.
- If the new time falls multiple days later, it shows `"(n days later)"`.
- If the starting day is provided, the output includes the updated weekday.

## Examples

```python
add_time('3:00 PM', '3:10')  
# Returns: '6:10 PM'

add_time('11:30 AM', '2:32', 'Monday')  
# Returns: '2:02 PM, Monday'

add_time('10:10 PM', '3:30')  
# Returns: '1:40 AM (next day)'

add_time('11:43 PM', '24:20', 'Tuesday')  
# Returns: '12:03 AM, Thursday (2 days later)'

add_time('6:30 PM', '205:12')  
# Returns: '7:42 AM (9 days later)'
```

## Test Cases

Below are key test cases ensuring the function behaves correctly:

- `add_time('3:30 PM', '2:12')` should return `'5:42 PM'`
- `add_time('11:55 AM', '3:12')` should return `'3:07 PM'`
- Expected time to include `"(next day)"` when relevant.
- Properly handling AM/PM changes at 12:00.
- `add_time('2:59 AM', '24:00')` should return `'2:59 AM (next day)'`
- `add_time('11:59 PM', '24:05')` should return `'12:04 AM (2 days later)'`
- `add_time('8:16 PM', '466:02')` should return `'6:18 AM (20 days later)'`
- Adding `0:00` should return the original time.
- `add_time('3:30 PM', '2:12', 'Monday')` should return `'5:42 PM, Monday'`
- `add_time('2:59 AM', '24:00', 'Saturday')` should return `'2:59 AM, Sunday (next day)'`
- `add_time('11:59 PM', '24:05', 'Wednesday')` should return `'12:04 AM, Friday (2 days later)'`
- `add_time('8:16 PM', '466:02', 'Tuesday')` should return `'6:18 AM, Monday (20 days later)'`

## Implementation

Below is the Python function that implements the time calculator:

```python
def add_time(start, duration, sday=''):
    # Function logic goes here...
```

## Constraints
- No Python libraries should be imported.
- Start times are always valid.
- Minutes in duration are whole numbers less than 60.

## License
This project follows freeCodeCamp's open-source guidelines.
