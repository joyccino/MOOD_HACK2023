import asyncio
from bleak import BleakClient

ADDRESS = "D8:B6:73:04:F1:F2"  # Replace with your device's address
CHARACTERISTIC_UUID = "0000FFE1-0000-1000-8000-00805F9B34FB"  # Replace with the characteristic UUID you want to interact with
textFile = open("emotionCodes.txt", "r")

async def main():
    async with BleakClient(ADDRESS) as client:
        while True:
            # Write data to the characteristic

            lines = textFile.readlines()
            

            #last = lines[-1].strip
            last = lines[len(lines)-1].strip()
            # if not last:
            #     last = last.strip()
            # else:
            #     last = '0'
            

            print(f"{last}, {lines}")
            if last == '1':

                await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray([0x01]))
                print("Sent: 1")
                await asyncio.sleep(5)
                response = await client.read_gatt_char(CHARACTERISTIC_UUID)
            elif last == '2':

                await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray([0x02]))
                print("Sent: 2")
                await asyncio.sleep(5)
                response = await client.read_gatt_char(CHARACTERISTIC_UUID)
            else:
                await client.write_gatt_char(CHARACTERISTIC_UUID, bytearray([0x03]))
                print("Sent: 3")
                await asyncio.sleep(5)
                response = await client.read_gatt_char(CHARACTERISTIC_UUID)



            
            
            

          
            # Write data to the characteristic

            # Read data from the characteristic
            
            
                
          
            
            
asyncio.run(main())
textFile.close()


