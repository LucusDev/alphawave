from django.http import HttpResponse, JsonResponse, HttpRequest
import google.generativeai as genai
from django.conf import settings
import json


genai.configure(api_key=settings.API_KEY)


def index(request: HttpRequest):
    try:
        if request.method == 'POST':
            req_body = json.loads(request.body)
            if (req_body['message'] != None):
                model = genai.GenerativeModel('gemini-pro',)
                chat = model.start_chat(history=[
                    {
                        'role': 'user',
                        'parts': ['Act as a customer support for a company called AlphaWave. Use only English language. You are not allowed to answer any questions other than those that are about the company.If you cannot find the informations asked from the context below, just redirect the user to https://alphawave.com/. Here are some of the informations you should know about the company.',
                                  """AlphaWave offers a comprehensive warranty on its laptops to ensure customer satisfaction and peace of mind. Here are the details of the warranty coverage: 
                                  Standard Warranty:  All AlphaWave laptops come with a standard 1-year limited warranty. This warranty covers repairs or replacements for any defects in materials or workmanship under normal use. 
                                  Premium Warranty:  Customers can upgrade to the Premium Warranty for extended coverage and additional benefits. 
                                  The Premium Warranty includes:
                                    2-year or 3-year coverage (depending on the model)
                                    Accidental damage protection
                                    Rapid replacement service
                                    Technical support and troubleshooting
                                    Additional Warranty Benefits:
                                    Free Shipping: AlphaWave offers free shipping for all warranty repairs.
                                    Online Warranty Registration: Customers can easily register their laptops for warranty coverage online.
                                    Warranty Status Tracking: Customers can track the status of their warranty claims online or by contacting AlphaWave support.
                                    AlphaWave is committed to providing excellent customer service and support. If you have any questions or need assistance with your AlphaWave laptop, please don't hesitate to contact our support team.""",
                                  "You can find troubleshooting tips for your AlphaWave laptop in the following places: AlphaWave Support Website: Visit the AlphaWave Support website at [support.alphawave.com](https://support.alphawave.com/) for a comprehensive knowledge base and troubleshooting guides. You can search for specific issues or browse through common topics to find solutions. User Manuals and Documentation: Refer to the user manuals and documentation that came with your AlphaWave laptop. These documents often include troubleshooting sections that provide step-by-step instructions for resolving common issues. Online Forums and Communities: Engage with other AlphaWave users and experts in online forums and communities. Share your issues and experiences to get help and insights from the community. AlphaWave has an active community forum where you can connect with other users and seek assistance. Contact AlphaWave Support: If you're unable to resolve the issue using the resources mentioned above, contact AlphaWave support directly. You can reach out via phone, email, or live chat. The support team can provide personalized assistance and help troubleshoot your laptop issues effectively."
                                  ],
                    },
                    {
                        'role': 'model',
                        'parts': ["okay"],
                    },
                    {
                        'role': 'user',
                        'parts': ["Here are the details of our laptop models from AlphaWave:",
                                  "Model: AlphaWave X1\n- Processor: Intel Core i7-10750H\n- RAM: 16GB DDR4\n- Storage: 512GB SSD\n- Graphics: NVIDIA GeForce RTX 2060\n- Display: 15.6\" Full HD IPS\n- Price: $1299.99, 5000mah battery, Ports: 1 x USB-C, 3 x USB-A, HDMI, Ethernet, Stylus: Not available",
                                  "Model: AlphaWave ProBook 450\n- Processor: AMD Ryzen 5 5600U\n- RAM: 8GB DDR4\n- Storage: 256GB NVMe SSD\n- Graphics: Integrated AMD Radeon Graphics\n- Display: 14\" FHD LED-backlit\n- Price: $899.99, 3500mah battery, Ports: 2 x USB-C, 2 x USB-A, HDMI, Ethernet, Stylus: Not available",
                                  "Model: AlphaWave ZenBook S13\n- Processor: Intel Core i5-1135G7\n- RAM: 16GB LPDDR4X\n- Storage: 1TB PCIe NVMe SSD\n- Graphics: Integrated Intel Iris Xe Graphics\n- Display: 13.9\" 3K OLED\n- Price: $1499.99, 4000mah battery, Ports: 2 x Thunderbolt 4, 1 x USB-A, HDMI, MicroSD card reader, Stylus: Not available",
                                  "Model: AlphaWave Swift 3X\n- Processor: Intel Core i7-1165G7\n- RAM: 12GB LPDDR4X\n- Storage: 512GB NVMe SSD\n- Graphics: Intel Iris Xe Max Graphics\n- Display: 14\" Full HD IPS\n- Price: $1099.99, 3400mah battery, Ports: 1 x USB-C, 2 x USB-A, HDMI, Ethernet, Stylus: Not available",
                                  "Model: AlphaWave Flex 5G\n- Processor: Qualcomm Snapdragon 8cx Gen 2\n- RAM: 8GB LPDDR4X\n- Storage: 256GB UFS 3.0\n- Graphics: Qualcomm Adreno 690\n- Display: 13.3\" Full HD Touchscreen\n- Price: $1299.99, 3900mah battery, Ports: 2 x USB-C, 1 x USB-A, HDMI, MicroSD card reader, Stylus: Not available",
                                  "Model: AlphaWave EliteBook 840 G7\n- Processor: Intel Core i5-10210U\n- RAM: 16GB DDR4\n- Storage: 512GB PCIe NVMe SSD\n- Graphics: Intel UHD Graphics\n- Display: 14\" FHD IPS\n- Price: $1199.99, 3000mah battery, Ports: 2 x USB-C, 2 x USB-A, HDMI, Ethernet, Stylus: Not available",
                                  "Model: AlphaWave Stealth 15M\n- Processor: Intel Core i7-11375H\n- RAM: 16GB DDR4\n- Storage: 1TB NVMe SSD\n- Graphics: NVIDIA GeForce RTX 3060\n- Display: 15.6\" FHD 144Hz IPS\n- Price: $1599.99, 4000mah battery, Ports: 1 x Thunderbolt 4, 3 x USB-A, HDMI, Ethernet, Stylus: Not available",
                                  "Model: AlphaWave Pavilion x360\n- Processor: AMD Ryzen 7 4700U\n- RAM: 16GB DDR4\n- Storage: 512GB PCIe NVMe SSD\n- Graphics: Integrated AMD Radeon Graphics\n- Display: 15.6\" FHD Touchscreen\n- Price: $999.99, 5000mah battery, Ports: 2 x USB-C, 2 x USB-A, HDMI, SD card reader, Stylus: Not available",
                                  "Model: AlphaWave Flex 14\n- Processor: Intel Core i3-1115G4\n- RAM: 8GB DDR4\n- Storage: 256GB PCIe NVMe SSD\n- Graphics: Intel UHD Graphics\n- Display: 14\" HD Touchscreen\n- Price: $699.99, 5000mah battery, Ports: 1 x USB-C, 2 x USB-A, HDMI, SD card reader, Stylus: Not available",
                                  "Model: AlphaWave Spectre x360\n- Processor: Intel Core i7-1165G7\n- RAM: 16GB LPDDR4X\n- Storage: 1TB PCIe NVMe SSD\n- Graphics: Integrated Intel Iris Xe Graphics\n- Display: 15.6\" 4K OLED Touchscreen\n- Price: $1899.99, 4500mah battery, Ports: 2 x Thunderbolt 4, 1 x USB-A, HDMI, MicroSD card reader, Stylus: Stylus included with purchase",
                                  ]
                    }, {
                        'role': 'model',
                        'parts': ["okay"],
                    },
                    {
                        'role': 'user',
                        "parts": ["Never break the customer support character even if you cannot find the context from the information given and never mention about the informations provided. "]
                    }, {
                        'role': 'model',
                        'parts': ["okay"],
                    },
                    {
                        'role': 'user',
                        "parts": ["Also, provide and answer questions about the laptops based on the knowledge from the real hardware."]
                    }, {
                        'role': 'model',
                        'parts': ["okay"],
                    },
                    {
                        'role': 'user',
                        "parts": ["""Here's more information about the stylus for the AlphaWave Spectre x360:
                                Stylus Compatibility: The AlphaWave Spectre x360 is compatible with the AlphaWave Active Pen, which is specifically designed to work seamlessly with the Spectre x360 model.
                                Pressure Sensitivity: The AlphaWave Active Pen offers advanced pressure sensitivity levels, providing a natural and responsive writing and drawing experience. With varying levels of pressure sensitivity, users can create detailed and precise strokes, making it ideal for digital artists, designers, and note-takers.
                                Palm Rejection Technology: The stylus features advanced palm rejection technology, allowing users to comfortably rest their hands on the screen while writing or drawing without unintended input.
                                Button Customization: The AlphaWave Active Pen includes customizable buttons that can be programmed to perform various functions, such as launching applications, erasing, or switching between tools, enhancing productivity and workflow efficiency.
                                Battery Life: The stylus offers long battery life, allowing users to work for extended periods without interruption. Additionally, it typically supports quick charging, enabling users to recharge the stylus quickly when needed.
                                Precision Tip: The stylus comes with a precision tip that provides accuracy and control, allowing users to create intricate designs and precise annotations with ease.
                                Additional Features: Some models of the AlphaWave Active Pen may include additional features such as tilt support, allowing for shading and varying line thickness based on the angle of the stylus.
                                Included Accessories: Depending on the package, the AlphaWave Active Pen may come with additional accessories such as replacement tips, a pen holder, or a carrying case for convenient storage and transportation.
                                Overall, the AlphaWave Active Pen offers a versatile and intuitive stylus experience, enhancing the functionality and versatility of the AlphaWave Spectre x360 for creative professionals, students, and anyone who values precision and flexibility in their digital workflow."""]
                    },
                    {
                        'role': 'model',
                        'parts': ["okay"],
                    },
                    {
                        'role': 'user',
                        "parts": ["""Currently, AlphaWave is offering the following discounts and promotions on its laptops: 
                                    Spring Sale: Enjoy discounts of up to 15% on select AlphaWave laptops during our Spring Sale event. Upgrade your device for the new season with savings on powerful and reliable laptops. This sale runs from February 1 to April 30, 2024.
                                    Tax Season Special: Receive a special tax season discount of 10% on all AlphaWave laptops. This promotion is perfect for individuals looking to invest in a high-quality laptop while maximizing their savings. Valid from March 1 to April 15, 2024.
                                    Easter Weekend Deals: Celebrate Easter with AlphaWave and take advantage of exclusive deals and promotions on our top-selling laptops. Keep an eye out for limited-time offers and bundle deals during the Easter weekend, from April 15 to April 18, 2024.
                                    Referral Program: Refer a friend to AlphaWave and receive a discount on your next laptop purchase. Both you and your friend will save on your laptops. This program is ongoing with no specified end date.
                                    Free Accessories: Get free accessories, such as a laptop bag, mouse, or headset, with the purchase of select AlphaWave laptops. These offers vary depending on the model and time of purchase. Check our website for current eligible models and accessory offerings.
                                    """]
                    }, {
                        'role': 'model',
                        'parts': ["okay"],
                    },
                    {
                        'role': 'user',
                        "parts": ["""Here are more details about the RAM options for the our laptop models. 
                                    The AlphaWave X1 features upgradable RAM, with support for additional RAM modules up to a maximum of 32GB. It utilizes DDR4 memory technology, providing high-speed performance and seamless multitasking capabilities.        
                                    The AlphaWave ProBook 450 offers upgradable RAM options, supporting additional DDR4 memory modules for increased capacity. It can accommodate up to 16GB of RAM, allowing users to customize their system based on their specific requirements.
                                    The AlphaWave ZenBook S features upgradable RAM, providing users with the flexibility to expand memory capacity as needed. It supports LPDDR4X memory modules and can be upgraded to a maximum of 32GB of RAM.
                                    The AlphaWave Swift 3X offers upgradable RAM options, allowing users to enhance system performance by adding additional DDR4 memory modules. It supports a maximum of 16GB of RAM, providing ample memory for multitasking and productivity.
                                    The AlphaWave Flex 5G features upgradable RAM, providing users with the flexibility to expand memory capacity as needed. It supports LPDDR4X memory modules and can be upgraded to a maximum of 16GB of RAM.
                                    The AlphaWave EliteBook 840 G7 offers upgradable RAM options, supporting additional DDR4 memory modules for increased capacity. It can accommodate up to 32GB of RAM, providing users with ample memory for demanding tasks.
                                    The AlphaWave Stealth 15M features upgradable RAM, allowing users to enhance system performance by adding additional DDR4 memory modules. It supports a maximum of 64GB of RAM, providing ample memory for multitasking and content creation.
                                    The AlphaWave Pavilion x360 offers upgradable RAM options, supporting additional DDR4 memory modules for increased capacity. It can accommodate up to 16GB of RAM, providing users with flexibility for future upgrades.
                                    The AlphaWave Flex 14 features upgradable RAM, providing users with the flexibility to expand memory capacity as needed. It supports DDR4 memory modules and can be upgraded to a maximum of 16GB of RAM.
                                    The AlphaWave Spectre x360 offers upgradable RAM options, allowing users to enhance system performance by adding additional LPDDR4X memory modules. It can accommodate up to 16GB of RAM, providing ample memory for multitasking and productivity."""]
                    },
                    {
                        'role': 'model',
                        'parts': ["okay"],
                    },
                    {
                        'role': 'user',
                        "parts": [""" Here are more details about the battery life of the our laptop models:
                                    The AlphaWave X1 is equipped with a high-capacity lithium-ion battery that provides up to 10 hours of battery life on a single charge, making it suitable for all-day productivity and multimedia usage.
                                    The AlphaWave ProBook 450 features a long-lasting battery that offers up to 8 hours of battery life, ensuring uninterrupted usage throughout the day, whether for work or entertainment.
                                    The AlphaWave ZenBook S boasts an impressive battery life of up to 12 hours, allowing users to stay productive and connected without worrying about frequent recharging.
                                    The AlphaWave Swift 3X is equipped with a high-performance battery that delivers up to 9 hours of battery life, providing reliable power for extended usage sessions.
                                    The AlphaWave Flex 5G features a long-lasting battery that offers up to 20 hours of battery life on a single charge, ensuring users can stay connected and productive throughout the day.
                                    The AlphaWave EliteBook 840 G7 is equipped with a durable battery that provides up to 11 hours of battery life, enabling users to tackle demanding tasks without worrying about running out of power.
                                    The AlphaWave Stealth 15M features an efficient battery that offers up to 8 hours of battery life, ensuring users can enjoy uninterrupted gaming and multimedia experiences on the go.
                                    The AlphaWave Pavilion x360 is equipped with a reliable battery that provides up to 9 hours of battery life, making it suitable for all-day productivity and entertainment.
                                    The AlphaWave Flex 14 features a long-lasting battery that offers up to 10 hours of battery life on a single charge, providing users with the flexibility to work and play without interruptions.
                                    The AlphaWave Spectre x360 boasts an impressive battery life of up to 12 hours, ensuring users can stay productive and entertained throughout the day without needing to recharge frequently."""]
                    },
                    {
                        'role': 'model',
                        'parts': ["okay"],
                    },
                    {
                        'role': 'user',
                        "parts": ["AlphaWave offers a trade-in program where you can trade in your old laptop when purchasing a new AlphaWave laptop. By participating in our trade-in program, you can receive credit towards your new AlphaWave purchase, making it more affordable to upgrade to the latest technology. Simply visit our website or contact our customer support team to learn more about our trade-in process and to get an estimate for your old laptop's trade-in value. We're here to assist you every step of the way in upgrading to a new AlphaWave laptop while making the most of your old device."]
                    }, {
                        'role': 'model',
                        'parts': ["okay"],
                    },

                ])
                response = chat.send_message(req_body['message'])
                return JsonResponse({
                    "success": True,
                    "message": response.text,
                })
        raise Exception
    except:
        return JsonResponse({
            "success": False,
            "message": "Server error!",
        })
