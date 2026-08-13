# from .energy_utils import calculate_energy_efficiency
# from .energy_utils import calculate_power_ratio as power_ratio
from .helpers import kw_to_mw
from functions import get_mean_absolute_error as mae

actual = [100, 120, 140]
predicted = [110, 115, 150]

print(mae(actual, predicted))

# print(calculate_energy_efficiency(80,100))
# print(power_ratio(500,1000))
print(kw_to_mw(2500))
# print(mw_to_kw(2.5))




