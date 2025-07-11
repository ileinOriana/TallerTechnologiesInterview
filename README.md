Appium iOS Test – TestApp Demo

App Used

Name: TestApp (official Appium demo app)
Why: It is lightweight, easy to compile, and designed for quick UI testing. Ideal for challenges like this one.

⸻

Test Environment
	•	Device: iPhone 16 Simulator
	•	iOS Version: 18.5
	•	Operating System: macOS with Xcode
	•	Appium: v2
	•	Language: Python 3.13
	•	Library: Appium-Python-Client 3.1.1
	•	Driver: xcuitest

⸻

What the Test Does
	1.	Launches the app TestApp.app in the iOS simulator.
	2.	Taps the “show alert” button on the main screen.
	3.	Waits for an alert with an “OK” button to appear.
	4.	Takes a screenshot and saves it as screenshot.png.

⸻

Test Result
	•	Result: Test passed successfully
	•	Screenshot: screenshot.png

⸻

Test Design Rationale

I chose TestApp.app because it is simple and designed specifically for UI testing. It does not require additional setup or real-world data. The interaction with the “show alert” button allows us to validate visible UI changes after a user action, which makes it ideal for a straightforward and effective test.