import time
import subprocess
import os

def keep_dashwave_active():
    while True:  # Infinite loop for 24×7 execution
        try:
            start_time = time.time()

            while True:
                # Prevent inactivity in Dashwave
                subprocess.run(["echo", "Keeping workspace active"], check=True)

                # Print uptime message to prevent session timeout
                elapsed = int(time.time() - start_time)
                print(f"✅ Dashwave active. Uptime: {elapsed} sec", flush=True)

                # Wait 5 minutes before the next action
                time.sleep(300)

        except Exception as e:
            print(f"⚠️ Error: {e}. Restarting script...", flush=True)
            time.sleep(5)  # Short delay before auto-restart

# **Run the script forever, even if it crashes**
while True:
    keep_dashwave_active()
    print("🔄 Restarting Dashwave keep-alive script...", flush=True)
    time.sleep(3)  # Short delay before restarting
