import RPi.GPIO as GPIO
import sys
import time
import PyNAU7802
import smbus2
import logging
from statistics import median

# Create the bus
bus = smbus2.SMBus(1)
# Create the scale and initialize it
scale = PyNAU7802.NAU7802()

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)

logging.basicConfig(level=logging.INFO)

fault_button = 27

CalFactor = 353.273
Zerooffset = -85376.75

# initializing relays
relay_pump = 4
relay_reversePump = 17
relay_I1 = 22
relay_I2 = 10
relay_I3 = 9
relay_I4 = 11
relay_I5 = 5
relay_I6 = 6
relay_I7 = 13
relay_I8 = 19
relay_I9 = 26
relay_I10 = 18
relay_I11 = 23
relay_I12 = 24
relay_I13 = 25
relay_I14 = 8
relay_I15 = 12
relay_I16 = 16
relay_I17 = 20
relay_I18 = 21

GPIO.setup(fault_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(relay_pump, GPIO.OUT)
GPIO.setup(relay_reversePump, GPIO.OUT)
GPIO.setup(relay_I1, GPIO.OUT)
GPIO.setup(relay_I2, GPIO.OUT)
GPIO.setup(relay_I3, GPIO.OUT)
GPIO.setup(relay_I4, GPIO.OUT)
GPIO.setup(relay_I5, GPIO.OUT)
GPIO.setup(relay_I6, GPIO.OUT)
GPIO.setup(relay_I7, GPIO.OUT)
GPIO.setup(relay_I8, GPIO.OUT)
GPIO.setup(relay_I9, GPIO.OUT)
GPIO.setup(relay_I10, GPIO.OUT)
GPIO.setup(relay_I11, GPIO.OUT)
GPIO.setup(relay_I12, GPIO.OUT)
GPIO.setup(relay_I13, GPIO.OUT)
GPIO.setup(relay_I14, GPIO.OUT)
GPIO.setup(relay_I15, GPIO.OUT)
GPIO.setup(relay_I16, GPIO.OUT)
GPIO.setup(relay_I17, GPIO.OUT)
GPIO.setup(relay_I18, GPIO.OUT)

GPIO.output(relay_pump, 1)
GPIO.output(relay_reversePump, 1)
GPIO.output(relay_I1, 1)
GPIO.output(relay_I2, 1)
GPIO.output(relay_I3, 1)
GPIO.output(relay_I4, 1)
GPIO.output(relay_I5, 1)
GPIO.output(relay_I6, 1)
GPIO.output(relay_I7, 1)
GPIO.output(relay_I8, 1)
GPIO.output(relay_I9, 1)
GPIO.output(relay_I10, 1)
GPIO.output(relay_I11, 1)
GPIO.output(relay_I12, 1)
GPIO.output(relay_I13, 1)
GPIO.output(relay_I14, 1)
GPIO.output(relay_I15, 1)
GPIO.output(relay_I16, 1)
GPIO.output(relay_I17, 1)
GPIO.output(relay_I18, 1)

def convert_to_grams(raw_reading, zero_offset, calibration_factor):
    """
    Convert the raw reading from the scale to grams.
    """
    return (raw_reading - zero_offset) / calibration_factor

def tareIngredient():
    measurements = []
    counter = 0
    while len(measurements) < 5:  # Collect exactly 5 measurements
        if scale.available():
            raw_reading = scale.getReading()
            weight_in_grams = convert_to_grams(raw_reading, Zerooffset, CalFactor)
            measurements.append(weight_in_grams)
            print(f"Measurement #{len(measurements)}: {weight_in_grams} grams")
        else:
            counter += 1
            print(f"Attempt #{counter}: No data available yet.")
        
        time.sleep(0.01)  # Short delay between measurements
        
    # Now calculate and return the median of the measurements as the tare weight
    tare_weight = median(measurements)
    print("Final Tare Weight (Median):", tare_weight)
    return tare_weight

def pourIngredient(data):
    ingredientNo = int(data[0])
    amount = float(data[1])
    #include weight offset
    offset = 0
    #get the weight of scale to tarr it
    initialweight =  tareIngredient()
    print("Initial Weight on Sacale:", initialweight)
    if ingredientNo == 1:
        #switch valve of 1st ingredient
        GPIO.output(relay_I1, 0)
        offset = 2
        rOffset = 8
        print("Disaronno valve Open")
    elif ingredientNo == 2:
        #switch valve of 2nd ingredient
        GPIO.output(relay_I2, 0)
        offset = 3
        rOffset = 5
        print("Gin valve Open")
    elif ingredientNo == 3:
        #switch valve of 3rd ingredient
        GPIO.output(relay_I3, 0)
        offset = 10
        rOffset = 0
        print("Coca Cola valve Open")
    elif ingredientNo == 4:
        #switch valve of 4th ingredient
        GPIO.output(relay_I4, 0)
        offset = 10
        rOffset = 0
        print("Sodavann valve Open")
    elif ingredientNo == 5:
        #switch valve of 5th ingredient
        GPIO.output(relay_I5, 0)
        offset = 3
        rOffset = 5
        print("Cointreau valve Open")
    elif ingredientNo == 6:
        #switch valve of 6th ingredient
        GPIO.output(relay_I6, 0)
        offset = 3
        rOffset = 5
        print("Malibu valve Open")
    elif ingredientNo == 7:
        #switch valve of 7th ingredient
        GPIO.output(relay_I7, 0)
        offset = 3
        rOffset = 5
        print("Whiskey valve Open")
    elif ingredientNo == 8:
        #switch valve of 8th ingredient
        GPIO.output(relay_I8, 0)
        offset = 3
        rOffset = 8
        print("Mango valve Open")
    elif ingredientNo == 9:
        #switch valve of 9th ingredient
        GPIO.output(relay_I9, 0)
        offset = 5
        rOffset = 10
        print("Midori valve Open")
    elif ingredientNo == 10:
        #switch valve of 10th ingredient
        GPIO.output(relay_I10, 0)
        offset = 2
        rOffset = 5
        print("Sugar syrup valve Open")
    elif ingredientNo == 11:
        #switch valve of 11th ingredient
        GPIO.output(relay_I11, 0)
        offset = 10
        rOffset = 0
        print("Sprite valve Open")
    elif ingredientNo == 12:
        #switch valve of 12th ingredient
        GPIO.output(relay_I12, 0)
        offset = 3
        rOffset = 5
        print("Vodka valve Open")
    elif ingredientNo == 13:
        #switch valve of 13th ingredient
        GPIO.output(relay_I13, 0)
        offset = 3
        rOffset = 5
        print("Rom valve Open")
    elif ingredientNo == 14:
        #switch valve of 14th ingredient
        GPIO.output(relay_I14, 0)
        offset = 5
        rOffset = 10
        print("Limejuice valve Open")
    elif ingredientNo == 15:
        #switch valve of 15th ingredient
        GPIO.output(relay_I15, 0)
        offset = 7
        rOffset = 20
        print("Appelsinjuice valve Open")
    elif ingredientNo == 16:
        #switch valve of 16th ingredient
        GPIO.output(relay_I16, 0)
        offset = 5
        rOffset = 10
        print("Pineapple valve Open")
    elif ingredientNo == 17:
        #switch valve of 17th ingredient
        GPIO.output(relay_I17, 0)
        offset = 2
        rOffset = 5
        print("Peachtree valve Open")
    elif ingredientNo == 18:
        #switch valve of 18th ingredient
        GPIO.output(relay_I18, 0)
        offset = 10
        rOffset = 0
        print("Ingefærøl valve Open")
    else:
        print("Invalid Ingredient Number")
    #open start regulated air pump here
    GPIO.output(relay_pump, 0)
    print("Regulated Air Pump Start")
    #get current weight
    while not scale.available():
        #pause uf scale not available
        pass
    medianMeasurements = []
    while len(medianMeasurements) < 5:
        if scale.available():
            raw_reading = scale.getReading()
            weight_in_grams = convert_to_grams(raw_reading, Zerooffset, CalFactor)
            medianMeasurements.append(weight_in_grams)
        time.sleep(0.01)  # Short delay between measurements

    # Calculate the median of the measurements
    currentWeight = median(medianMeasurements)
    lastCurrentWeight = currentWeight
    pourWeight = currentWeight - initialweight
    #variables to monitor empty bottle or not pouring
    time_to_monitor_not_pouring = time.time()
    #monitor weight
    msgTime = time.time()
    while pourWeight < (amount - offset):
        #to monitor not pouring
        if ((time.time() - time_to_monitor_not_pouring) > 7.0):
            GPIO.output(relay_pump, 1)
            #stuck here until button is pressed
            n=0
            while(GPIO.input(fault_button)):
                #wait for manual fault correct
                while(GPIO.input(fault_button)):
                    if n==0:
                        print("!! Tom ingredients !!", ingredientNo)
                        n=1
                time.sleep(0.5)
            print("restarting pouring")
            GPIO.output(relay_pump, 0)
            time_to_monitor_not_pouring = time.time()
        if scale.available():
            # Collect exactly 5 measurements for median calculation
            tareMeasurements = []
            while len(tareMeasurements) < 5:
                raw_reading = scale.getReading()
                weight_in_grams = convert_to_grams(raw_reading, Zerooffset, CalFactor)
                tareMeasurements.append(weight_in_grams)
                time.sleep(0.01)  # Short delay between measurements
            # Calculate the median of the collected measurements
            currentWeight = median(tareMeasurements)
        else:
            print("Scale not available right now")
        pourWeight = currentWeight - initialweight
        if (currentWeight - lastCurrentWeight) > 2.0:
            time_to_monitor_not_pouring = time.time()
            lastCurrentWeight = currentWeight
        if (time.time()-msgTime) > 1:
            msgTime = time.time()
            print("Send message to Node-Red to monitor time")
            print(pourWeight)
        if pourWeight > (amount - (offset + rOffset)):
            # switch on reverse air pump
           GPIO.output(relay_reversePump, 0)
        if pourWeight <= -30:
            print("Weight sensor error, stopping pour.", pourWeight)
            break
        time.sleep(0.01)
    #Goal weight acheived
    # switch of regulated air pump
    GPIO.output(relay_pump, 1)
    time.sleep(4)
    # switch off reverse air pump
    GPIO.output(relay_reversePump, 1)
    # switch off valve
    GPIO.output(relay_I1, 1)
    GPIO.output(relay_I2, 1)
    GPIO.output(relay_I3, 1)
    GPIO.output(relay_I4, 1)
    GPIO.output(relay_I5, 1)
    GPIO.output(relay_I6, 1)
    GPIO.output(relay_I7, 1)
    GPIO.output(relay_I8, 1)
    GPIO.output(relay_I9, 1)
    GPIO.output(relay_I10, 1)
    GPIO.output(relay_I11, 1)
    GPIO.output(relay_I12, 1)
    GPIO.output(relay_I13, 1)
    GPIO.output(relay_I14, 1)
    GPIO.output(relay_I15, 1)
    GPIO.output(relay_I16, 1)
    GPIO.output(relay_I17, 1)
    GPIO.output(relay_I18, 1)
    time.sleep(1)
    # send message to node-red
    currentWeight = (tareIngredient())
    pourWeight = currentWeight - initialweight
    print("Ingredient No:", ingredientNo, "with poured weight of:", pourWeight, "grams")
    logging.info("Ingredient %d ble fylt med %d gram.", ingredientNo, pourWeight)
    return 0

def main():
    noOfIngredients = len(sys.argv) - 1
    print ("No of Ingredients =", noOfIngredients)
    if noOfIngredients < 1:
        print ("Mangler data")
        global validIngredientsFlag
        validIngredientsFlag= False
    else:
        #checks for ingredients are valid or not
        for arg in sys.argv:
            print(arg)
            if arg[0]!="/" and arg[0]!="m":
                value = arg.split(".",1)
                try:
                    print ("Ingredient No:", int(value[0]),"Amount:", int(value[1]), "grams")
                    print("Valid Ingredient")
                    validIngredientsFlag = True
                except:
                    print("Feil på argument")
                    validIngredientsFlag = False
                    break
            else:
                print("Program Name")
    #Setup/ Check Scale
    if scale.begin(bus):
        print("Scale Connected!")
        scale.setCalibrationFactor(353.273)
        scale.setZeroOffset(-85376.75)
        scale.setSampleRate(320)
        #scale.calibrateAFE()
    else:
        a = 0
        while not scale.begin(bus):
            if a == 0:
                print("Can't find the scale, please check wiring ...")
            # freeze program while scale not connected
        print("Scale Connected!")
        scale.setCalibrationFactor(353.273)
        scale.setZeroOffset(-85376.75)
        scale.setSampleRate(320)
        #exit()
    # will pour ingredients in input sequence
    if validIngredientsFlag:
        for arg in sys.argv:
            if arg[0]!="/" and arg[0]!="m":
                value = arg.split(".",1)
                print("pouring ingredient no:", value[0],"of", value[1], "grams")
                logging.info("fyller ingrediens %s med %s gram.", value[0], value[1])
                pourIngredient(value)
        print("Drink er ferdig!")
        logging.info("Drink ferdigmikset.")
    return 0

if __name__ == "__main__":
    main()
