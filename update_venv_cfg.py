import os

def update_venv_cfg(venv_path):
    cfg_path = os.path.join(venv_path, 'pyvenv.cfg')
    if not os.path.exists(cfg_path):
        print("Không tìm thấy file pyvenv.cfg.")
        return

    new_python_exe = os.path.join(venv_path, 'Scripts', 'python.exe')
    new_command = f"{new_python_exe} -m venv {venv_path}"

    with open(cfg_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        if line.startswith("executable ="):
            updated_lines.append(f"executable = {new_python_exe}\n")
        elif line.startswith("command ="):
            updated_lines.append(f"command = {new_command}\n")
        elif line.startswith("home ="):
            # Không cần sửa `home`, vì nó chỉ là nơi cài Python gốc
            updated_lines.append(line)
        else:
            updated_lines.append(line)

    with open(cfg_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

    print("✅ Đã cập nhật lại pyvenv.cfg!")

# Ví dụ sử dụng:
# Nhập đường dẫn mới đến venv (hoặc để mặc định nếu chạy script trong cùng thư mục)
venv_folder = os.path.abspath("venv")
update_venv_cfg(venv_folder)
