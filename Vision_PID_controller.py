from controller import Display
from vehicle import Car
from vehicle import Driver
import numpy as np
from controller import Camera
import matplotlib.pyplot as plt
import CV_utils


def main():
    car= Car()
    Car_driver = Driver()
    # camera = car.getCamera("camera")// This function depricated
    camera= car.getDevice("camera")
    timestep = int(car.getBasicTimeStep())
    camera.enable(timestep)
    display_th= Display("display_th")
    colour = np.array([25,127,127])
    error = np.array([8,80,80])

    while car.step() != -1:
        image = CV_utils.get_image(camera)
        binary_image = CV_utils.convert_binary_image(image, colour, error)
        norm_column, average_column = CV_utils.calculate_average_col_and_norm_col(binary_image)
        angle = norm_column *1.0
        print(f"Info: Normalized column {norm_column:.2f}")
        print(f"Info: Average column {average_column:.2f}")
        
        CV_utils.display_binary_image(display_th, binary_image, average_column)
        Car_driver.setSteeringAngle(angle)
        Car_driver.setCruisingSpeed(50)
if __name__ == "__main__":
    main()