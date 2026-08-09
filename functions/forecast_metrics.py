def get_mean_absolute_error(actual,predicted):
    if len(actual)==0 or (len(actual) != len(predicted)):
        return None
    total = 0
    for i in range(len(actual)):
        error = abs(actual[i]-predicted[i])
        total+=error
    result = total/len(actual)
    return result
# mean_absolute_error = get_mean_absolute_error([10,20,30],[12,18,33])
# print("Mean absolute error is: ", mean_absolute_error)

def get_mean_squared_error(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    total = 0
    for i in range(len(actual)):
        error_squared = (actual[i] - predicted[i])**2
        total +=error_squared
    result = total/len(actual)
    return result
# mean_squared_error = get_mean_squared_error([10,20,30],[12,18,33])
# print("Mean squared error is: ", mean_squared_error)

def get_root_mean_squared(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    total = 0
    for i in range(len(actual)):
        error_squared = (actual[i] - predicted[i])**2
        total += error_squared
    average = total/len(actual)
    result = average**0.5
    return result
# root_mean_squared_error = get_root_mean_squared([10,20,30],[12,18,33])
# print("The root mean squared error is: ", root_mean_squared_error)

def get_mean_absolute_percentage_error(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    total = 0
    valid_count = 0
    for i in range(len(actual)):
        if actual[i] == 0:
            continue
        error =abs((predicted[i]-actual[i])/(actual[i]))*100
        total+=error
        valid_count+=1
    if valid_count == 0:
        return None
    result = total/valid_count
    return result
# mape =get_mean_absolute_percentage_error([10,20,30],[12,18,33])
# print("The mean absolute percentage error is: ", mape)

def get_forecast_bias(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    total = 0
    for i in range(len(actual)):
        error = predicted[i]-actual[i]
        total+=error
    result = total/len(actual)
    return result
# forecast_bias = get_forecast_bias([10,20,30],[12,18,33])
# print("The forecast bias is: ",forecast_bias)

def count_forecast_direction(actual,predicted):
    if not actual or len(actual)!=len(predicted):
        return None
    over_pred = 0
    under_pred =0
    exact = 0
    for i in range(len(actual)):
        error = predicted[i]-actual[i]
        if error > 0:
            over_pred+=1
        elif error < 0:
            under_pred += 1
        else:
            exact+=1
    return over_pred, under_pred, exact
# result = count_forecast_direction([10,20,30],[12,18,33])
# over_pred, under_pred, exact = result
# if result is None:
#     print("Invalid input")
# else:
#     print("The number of over predictions are: ", over_pred)
#     print("The number of under predictions are: ",under_pred)
#     print("The exact predictions are: ", exact)

                        ## Function composition ##

def get_mean_absolute_error(actual,predicted):
    if not actual or len(actual) != len(predicted):
        return None
    total = 0
    for i in range(len(actual)):
        error = abs(actual[i]-predicted[i])
        total+=error
    result = total/len(actual)
    return result

def compare_forecasts(actual,predicted_a,predicted_b):

    mae_a = get_mean_absolute_error(actual,predicted_a)
    mae_b = get_mean_absolute_error(actual,predicted_b)

    if mae_a is None or mae_b is None:
        return None

    if mae_a < mae_b:
        return "Forecast A"
    elif mae_a > mae_b:
        return "Forecast B"
    else:
        return "Tie"

actual = [100, 120, 140, 130, 150]

predicted_a = [102, 118, 145, 128, 149]
predicted_b = [110, 125, 138, 135, 160]

# result = compare_forecasts(actual,predicted_a,predicted_b)

# print(result)