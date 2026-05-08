# Fall Guardian

> Here TinyML and sensor fusion are used to run a classification model to detect if a fall has occurred and Arduinos Nano BLE sense kit.

---

# Overview
- Fall Guardian is an attempt to solve the problem of finding fall victims much to late.
- This product is for anyone or any company who aims limit the risk of falls
- We use TinyML to predict if a fall has occurred, from which alerts can be sent to gather help.

---


# Tech
- Arduino Nano 33 BLE Sense

---

# How to use repo
This repo has:
- 2 data sets (SisFall_dataset.sip & adultFallData.zip)
- 1 data formatting script (dataprep.py)
- 1 edge impulse build (ei-fall_detection_v2-arduino-1.0.2-impulse-#1.zip)
- 1 .ino file (nano_ble33_sense_fusion/nano_ble33_sense_fusion.ino)

The 2 datasets and 1 data formatting components of this file can be used to replicate building the model using edge impulse.

The 1 edge impulse build and 1 .ino file can be used to run the current solution.

## How to run current solution

Step:
1. add the ei-fall_detection_v2-arduino-1.0.2-impulse-#1.zip to the library of your Arduino IDE
2. open the example Fall_Detection_V2_inferenceing > nano_ble_sense > nano_ble_sense_fusion
3. copy into the now open file the code found in nano_ble33_sense_fusion/nano_ble33_sense_fusion.ino (this file is in the repo)
4. plug your Arduino  Nano BLE33 Sense into your computer, connect via COM, and upload to board.
5. Test and play, open your serial monitor to observe prediction %, or use the LED to see predictions

