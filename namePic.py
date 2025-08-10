import os
import json

def get_image_files(folder_path):
    """
    ดึงรายชื่อไฟล์รูปภาพทั้งหมดในโฟลเดอร์ที่กำหนด

    Args:
        folder_path (str): พาธของโฟลเดอร์ที่ต้องการสแกน

    Returns:
        list: รายชื่อไฟล์รูปภาพพร้อมพาธ (เช่น ['Pic/image1.jpg', 'Pic/image2.png'])
    """
    image_files = []
    
    # ตรวจสอบว่าโฟลเดอร์มีอยู่จริงหรือไม่
    if not os.path.isdir(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return image_files

    # กำหนดนามสกุลไฟล์รูปภาพที่ต้องการ
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')

    # วนลูปผ่านไฟล์และโฟลเดอร์ทั้งหมดในโฟลเดอร์ที่กำหนด
    for filename in os.listdir(folder_path):
        # สร้างพาธเต็มของไฟล์
        file_path = os.path.join(folder_path, filename)
        
        # ตรวจสอบว่าเป็นไฟล์และมีนามสกุลเป็นรูปภาพ
        if os.path.isfile(file_path) and filename.lower().endswith(valid_extensions):
            # เพิ่มพาธของไฟล์ลงในรายการ
            # .replace('\\', '/') เพื่อให้พาธเป็นรูปแบบ URL ที่ถูกต้องสำหรับเว็บ
            image_files.append(file_path.replace('\\', '/'))
            
    return image_files

if __name__ == "__main__":
    # กำหนดพาธของโฟลเดอร์รูปภาพ
    image_folder_path = 'Pic'
    
    # เรียกฟังก์ชันเพื่อดึงรายชื่อไฟล์
    images = get_image_files(image_folder_path)
    
    # พิมพ์รายชื่อไฟล์ทั้งหมด
    if images:
        print("Found the following image files:")
        for img in images:
            print(f"- '{img}'")
            
        # ถ้าต้องการนำไปใช้ใน JavaScript โดยตรง สามารถแปลงเป็น JSON ได้
        # และคัดลอกส่วนนี้ไปวางในโค้ดของคุณ
        print("\n--- JSON format for JavaScript ---")
        json_images = json.dumps(images, indent=2)
        print(json_images)
    else:
        print("No image files found in the folder.")