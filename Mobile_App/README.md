# User Guide

## Prerequisites
- [Android Studio](https://developer.android.com/studio) 
- A physical/virtual android device running version 4.0 or above.
- Knowlege of using android studio or a similar JetBrains IDE.

## Testing

### Via Android Studio 

- Open the project folder for **Mobile App** in Android Studio.
- Hit the green play button in the top nav bar just like you would run a program in similar JetBrains IDEs.
- You will be prompted to select a vitual device. Choose which one you plan to run the app on. If you have not yet configured a device, do the following from within the window:
  - Select **Create New Virtual Device** tab. 
  - Choose a device to emulate. (Dev Config: Pixel)
  - Choose an API level for your virtual device. (Dev Config: 24 Nougat)
  **__Note__:** The app will run on anything over API 21 (Android Lollipop)
  - Lastly, name your device and hit **Finish**.

- Once you have your device selected, hit **Ok**. You will see your vitual device come up and start running the app. 
- Stop the app by hitting the red button in Android Studio or by closing the app from within the virtual device.

### Via a Physical Device

- Follow the steps to open the project as mentioned in the previous section
- Navigate to the **Build** Tab at the top navbar of Android Studio and select it.
- Scroll down to the **Build Bundle(s)/APK(s)** option and hit **Build APK(s)**
- After a moment, the IDE will notify you that the building is complete. You can either hit "locate" from within this notification to find the apk or navigate to `~/your_repo/location/Mobile_App/app/build/outputs/apk/debug` and see your apk with the extention .apk.
- Trasfer this file to your phone via your preferred transfer method (Google Drive recommended) and open it on your phone.
- Ensure you have Third Party Apps enabled and follow the prompts to install.
- Lastly, simply open the app from your device's app menu.