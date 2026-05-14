#!/usr/bin/env python3
import os
import json
import hashlib
import qrcode
from PIL import Image

def generate_soverain_qr_matrix():
    print("=== ⚜ XP SOVERAIN QR PAYLOAD ENGINES INITIALIZING ===")
    
    # 1. Core Compressed Canonical Matrix Dataset
    compressed_payload = {
        "v": "XP-1",
        "ens": "the.holy.high.imperial.house.of.dwd.eth",
        "aid": "IiB-bzj1X29wfgX-poOzQaQUIA_4oWTaC4U2dHBV3wuk",
        "said": "4301abd2d56147f2ec6f74fd650d14251787828fb77c664bf3205d912de8bf61",
        "pid": "IMPERI-BERIT-SUITE-001",
        "lei": "506700GE1G29325QX363"
    }

    # 2. Convert to URI Scheme for Quick Camera Scan and Registry Routing
    qr_uri_string = (
        f"id:keri:{compressed_payload['aid']}?said={compressed_payload['said']}"
        f"&ens={compressed_payload['ens']}&pid={compressed_payload['pid']}&lei={compressed_payload['lei']}"
    )
    print(f"[LOG] Target Routing URI: {qr_uri_string}")

    # 3. Configure QR Matrix Properties (High Error Correction to support icon overlay)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H, # Level H recovery reserves up to 30% area
        box_size=10,
        border=4,
    )
    qr.add_data(qr_uri_string)
    qr.make(fit=True)

    # 4. Compile Base Visual Matrix Asset
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # 5. Icon Overlay Engine Logic
    icon_filename = "signature_icon.png"
    if os.path.exists(icon_filename):
        print(f"[ENGINE] Target signature icon found. Stamping canvas...")
        logo = Image.open(icon_filename)
        
        # Calculate sizing constraints (icon should not occupy more than 20% of code area)
        qr_width, qr_height = qr_image.size
        logo_max_size = int(qr_width * 0.2)
        logo = logo.resize((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
        
        # Determine exact absolute center coordinate points
        position = ((qr_width - logo_max_size) // 2, (qr_height - logo_max_size) // 2)
        
        # Handle transparency masks gracefully
        if logo.mode == 'RGBA':
            qr_image.paste(logo, position, logo)
        else:
            qr_image.paste(logo, position)
        print("[STATUS] Center stamp successfully executed.")
    else:
        print(f"[WARNING] '{icon_filename}' missing from workspace root. Generating raw matrix asset instead.")

    # 6. Secure Folder Check and Document Write
    output_path = "logs/SOVERAIN-QR-MATRIX-FINAL.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    qr_image.save(output_path)
    
    print(f"[SUCCESS] Deep Matrix Built. File saved securely to: {output_path}")
    print("=== ⚜ XP LEDGER BOUNDARIES PROVISIONED ===")

if __name__ == "__main__":
    generate_soverain_qr_matrix()
