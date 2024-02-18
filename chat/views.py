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
                model = genai.GenerativeModel('gemini-pro')
                chat = model.start_chat(history=[
                    {
                        'role': 'user',
                        'parts': ['Give me the detailed informations of your laptop models'],
                    },
                    {
                        'role': 'model',
                        'parts': ["Sure! Here are the details of our laptop models:",
                        "Model: AlphaWave X1\n- Processor: Intel Core i7-10750H\n- RAM: 16GB DDR4\n- Storage: 512GB SSD\n- Graphics: NVIDIA GeForce RTX 2060\n- Display: 15.6\" Full HD IPS\n- Price: $1299.99",
                        "Model: AlphaWave ProBook 450\n- Processor: AMD Ryzen 5 5600U\n- RAM: 8GB DDR4\n- Storage: 256GB NVMe SSD\n- Graphics: Integrated AMD Radeon Graphics\n- Display: 14\" FHD LED-backlit\n- Price: $899.99",
                        "Model: AlphaWave ZenBook S\n- Processor: Intel Core i5-1135G7\n- RAM: 16GB LPDDR4X\n- Storage: 1TB PCIe NVMe SSD\n- Graphics: Integrated Intel Iris Xe Graphics\n- Display: 13.9\" 3K OLED\n- Price: $1499.99",
                        "Model: AlphaWave Swift 3X\n- Processor: Intel Core i7-1165G7\n- RAM: 12GB LPDDR4X\n- Storage: 512GB NVMe SSD\n- Graphics: Intel Iris Xe Max Graphics\n- Display: 14\" Full HD IPS\n- Price: $1099.99",
                        "Model: AlphaWave Flex 5G\n- Processor: Qualcomm Snapdragon 8cx Gen 2\n- RAM: 8GB LPDDR4X\n- Storage: 256GB UFS 3.0\n- Graphics: Qualcomm Adreno 690\n- Display: 13.3\" Full HD Touchscreen\n- Price: $1299.99",
                        "Model: AlphaWave EliteBook 840 G7\n- Processor: Intel Core i5-10210U\n- RAM: 16GB DDR4\n- Storage: 512GB PCIe NVMe SSD\n- Graphics: Intel UHD Graphics\n- Display: 14\" FHD IPS\n- Price: $1199.99",
                        "Model: AlphaWave Stealth 15M\n- Processor: Intel Core i7-11375H\n- RAM: 16GB DDR4\n- Storage: 1TB NVMe SSD\n- Graphics: NVIDIA GeForce RTX 3060\n- Display: 15.6\" FHD 144Hz IPS\n- Price: $1599.99",
                        "Model: AlphaWave Pavilion x360\n- Processor: AMD Ryzen 7 4700U\n- RAM: 16GB DDR4\n- Storage: 512GB PCIe NVMe SSD\n- Graphics: Integrated AMD Radeon Graphics\n- Display: 15.6\" FHD Touchscreen\n- Price: $999.99",
                        "Model: AlphaWave Flex 14\n- Processor: Intel Core i3-1115G4\n- RAM: 8GB DDR4\n- Storage: 256GB PCIe NVMe SSD\n- Graphics: Intel UHD Graphics\n- Display: 14\" HD Touchscreen\n- Price: $699.99",
                        "Model: AlphaWave Spectre x360\n- Processor: Intel Core i7-1165G7\n- RAM: 16GB LPDDR4X\n- Storage: 1TB PCIe NVMe SSD\n- Graphics: Integrated Intel Iris Xe Graphics\n- Display: 15.6\" 4K OLED Touchscreen\n- Price: $1899.99"],
                    },
                    {
                        'role': 'user',
                        'parts': ["If the user asks about the laptops from other brands such as ASUS, Dell, Lenovo, Acer or asks to compare AlphaWave laptop models with the laptops from other brands, respond like this-> I apologize, but I am designed to provide information specifically about AlphaWave laptop models. If you have any inquiries regarding AlphaWave laptops or need assistance with our products, feel free to ask, and I'll be happy to help."],
                    },
                    {
                        'role': 'model',
                        'parts': ["okay. Got it"],
                    },
                    {
                        'role': 'user',
                        'parts': ["If the user asks about the AlphaWave laptop models which are not AlphaWave X1, AlphaWave ProBook 450, AlphaWave ZenBook S, AlphaWave Swift 3X, AlphaWave Flex 5G, AlphaWave EliteBook 840 G7, AlphaWave Stealth 15M, AlphaWave Pavilion x360, AlphaWave Flex 14 and AlphaWave Spectre x360, respond like this->Thank you for your inquiry. It seems there might be a misunderstanding regarding the model name. Currently, we don't have a model named \"AlphaWave XYZ.\" However, if you're referring to a different AlphaWave laptop model, please provide the correct name, and I'll gladly provide you with the details you're looking for."],
                    },
                    {
                        'role': 'model',
                        'parts': ["okay. Got it"],
                    },
                    {
                        'role': 'user',
                        'parts': ["What kind of warranty does AlphaWave offer on its laptops?"],
                    },
                    {
                        'role': 'model',
                        'parts': ["""AlphaWave offers a comprehensive warranty on its laptops to ensure customer satisfaction and peace of mind. Here are the details of the warranty coverage: 
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

                                    AlphaWave is committed to providing excellent customer service and support. If you have any questions or need assistance with your AlphaWave laptop, please don't hesitate to contact our support team."""],
                    },
                    {
                        'role': 'user',
                        'parts': ["What are the latest discounts or promotions available on AlphaWave laptops?"],
                    },
                    {
                        'role': 'model',
                        'parts': ["""Currently, AlphaWave is offering the following discounts and promotions on its laptops: 
                                    Spring Sale: Enjoy discounts of up to 15% on select AlphaWave laptops during our Spring Sale event. Upgrade your device for the new season with savings on powerful and reliable laptops. This sale runs from February 1 to April 30, 2024.
                                    Tax Season Special: Receive a special tax season discount of 10% on all AlphaWave laptops. This promotion is perfect for individuals looking to invest in a high-quality laptop while maximizing their savings. Valid from March 1 to April 15, 2024.
                                    Easter Weekend Deals: Celebrate Easter with AlphaWave and take advantage of exclusive deals and promotions on our top-selling laptops. Keep an eye out for limited-time offers and bundle deals during the Easter weekend, from April 15 to April 18, 2024.
                                    Referral Program: Refer a friend to AlphaWave and receive a discount on your next laptop purchase. Both you and your friend will save on your laptops. This program is ongoing with no specified end date.
                                    Free Accessories: Get free accessories, such as a laptop bag, mouse, or headset, with the purchase of select AlphaWave laptops. These offers vary depending on the model and time of purchase. Check our website for current eligible models and accessory offerings.
                                    Seasonal Promotions: Keep an eye out for seasonal promotions throughout the year. AlphaWave runs special offers during holidays, such as Black Friday, Cyber Monday, and Christmas. To stay updated on the latest discounts and promotions, visit the AlphaWave website or follow us on social media. You can also sign up for our email newsletter to receive exclusive offers and updates."""],
                    },
                    {
                        'role': 'user',
                        'parts': ["Where can I find troubleshooting tips for my AlphaWave laptop?"],
                    },
                    {
                        'role': 'model',
                        'parts': ["You can find troubleshooting tips for your AlphaWave laptop in the following places: AlphaWave Support Website: Visit the AlphaWave Support website at [support.alphawave.com](https://support.alphawave.com/) for a comprehensive knowledge base and troubleshooting guides. You can search for specific issues or browse through common topics to find solutions. User Manuals and Documentation: Refer to the user manuals and documentation that came with your AlphaWave laptop. These documents often include troubleshooting sections that provide step-by-step instructions for resolving common issues. Online Forums and Communities: Engage with other AlphaWave users and experts in online forums and communities. Share your issues and experiences to get help and insights from the community. AlphaWave has an active community forum where you can connect with other users and seek assistance. Contact AlphaWave Support: If you're unable to resolve the issue using the resources mentioned above, contact AlphaWave support directly. You can reach out via phone, email, or live chat. The support team can provide personalized assistance and help troubleshoot your laptop issues effectively."],
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
