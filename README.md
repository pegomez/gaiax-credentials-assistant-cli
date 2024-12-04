# Gaia-X Self-Description Credentials Assistant CLI

This project was developed for the **Gaia-X Hackathon December 2024**, addressing the challenges proposed by Aire Networks and CTIC.

**DISCLAIMER**: This is a **proof of concept** created for the Gaia-X Hackathon and is not an official tool endorsed by Gaia-X AISBL or any other Gaia-X entity.

---

## Hackathon Challenge Context

This solution responds to the Professional Challenge: **Automatic Generation of Gaia-X Self-Descriptions**, focusing on:
- Automating the creation of Gaia-X Self-Descriptions based on OpenAPI/AsyncAPI specifications.
- Validating and managing trust anchor certificates, including integration with Let's Encrypt.
- Ensuring compliance with the Gaia-X Trust Framework.
- Supporting the integration of conformity proofs from Gaia-X Digital Clearing House (GXDCH).

---

## Features

- **Conversational Workflow**: Guides users step-by-step through the generation of Self-Descriptions.
- **Integration with OpenAPI/AsyncAPI**: Automatically extracts metadata to generate JSON-LD compliant Self-Descriptions.
- **Certificate Management**: Supports both custom EV-SSL certificates and Let's Encrypt for trust anchors.
- **Error Handling and Validation**: Detects issues, provides detailed feedback enhanced by AI, and ensures compliance with Gaia-X requirements.
- **Conformity Proofs**: Automatically integrates proofs from the specified GXDCH instance.

---

## Prerequisites

- Python 3.8 or higher.
- `pipenv` or `pip` for managing dependencies.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/pegomez/gaiax-credentials-assistant-cli
cd gaiax-credentials-assistant-cli
```

### 2. Install Dependencies
Using `pip`:
```bash
pip install -r requirements.txt
```

Or, using `pipenv`:
```bash
pipenv install
```

---

## Running the CLI

### Generate a Self-Description

To start the interactive CLI and generate a Gaia-X Self-Description:
```bash
python gaiax_credentials_assistant_cli_interactive.py generate-self-description
```

You will be guided step-by-step through:
1. Providing the OpenAPI/AsyncAPI specification file.
2. Specifying the output file for the generated Self-Description.
3. Configuring trust anchor certificates (custom or Let's Encrypt).
4. Integrating conformity proofs from GXDCH.

---

## Example Usage

### Step-by-Step CLI Interaction

#### Command
```bash
python gaiax_credentials_assistant_cli_interactive.py generate-self-description
```

#### Example Output
```
Welcome to the Gaia-X Self-Description Generator!
Let's generate a Gaia-X Self-Description step by step.

1. Please provide the path to the OpenAPI or AsyncAPI specification: ./api-specs/service-api.yaml
✅ Successfully located API specification at ./api-specs/service-api.yaml.

2. Where should the generated Self-Description be saved? [./self_description.json]: ./output/self_description.json
✅ Created output directory: ./output.

3. Do you want to provide a custom trust anchor certificate and private key? [y/N]: y
Path to the trust anchor certificate: ./certs/my-cert.pem
Path to the trust anchor private key: ./certs/my-key.pem
✅ Using provided trust anchor certificate and key: ./certs/my-cert.pem, ./certs/my-key.pem.

4. Should the generated Self-Description include conformity proofs from GXDCH? [Y/n]: y
Please specify the GXDCH instance (e.g., Aire Networks) [Aire Networks]: Aire Networks
✅ Integrated conformity proofs from GXDCH instance: Aire Networks.

5. Generating the Gaia-X Self-Description...
✅ Self-Description generated successfully and saved at ./output/self_description.json.

6. Do you want to validate the trust anchor certificates? [Y/n]: y
Warning: The certificate is not EV-SSL compliant.
✅ Trust anchor certificates validated successfully.

🎉 Gaia-X Self-Description generation complete! Thank you for using this tool.
```

---

## Key Objectives Addressed

1. **Automatic Self-Description Generation**:
   - Integrates with OpenAPI/AsyncAPI to extract metadata.
   - Generates JSON-LD documents compliant with Gaia-X Trust Framework.
2. **Trust Anchor Certificate Management**:
   - Supports custom EV-SSL certificates.
   - Automatically generates Let's Encrypt certificates for testing or staging environments.
3. **Conformity Proofs Integration**:
   - Fetches proofs from Gaia-X Digital Clearing House (GXDCH) instances.
4. **User-Friendly Workflow**:
   - Conversational flow with detailed error handling and feedback.

---

## Troubleshooting

- **File Not Found**: Ensure the paths to your OpenAPI/AsyncAPI specification or certificates are correct.
- **Missing Dependencies**: Verify all dependencies are installed with `pip install -r requirements.txt`.
- **Conformity Proofs**: Ensure you have access to the specified GXDCH instance.

---

## References

- [Gaia-X Trust Framework](https://gaia-x.eu/trust-framework/)
- [Gaia-X Digital Clearing House (GXDCH)](https://gaia-x.eu/gxdch/)
- [JSON-LD Specifications](https://json-ld.org/)
- [Let's Encrypt Documentation](https://letsencrypt.org/docs/)

---

## Authors

This project was developed by the following contributors as part of the Gaia-X Hackathon December 2024:

- [Jacinto Arias](https://github.com/jacintoArias)
- [Kiko Cisneros](https://github.com/kikoCis)
- [Pedro Gómez](https://github.com/pegomez)
- [Álvaro Manuel Recio Pérez](https://github.com/amrecio)
- [Javier D. Serrano](https://github.com/JavierDSer)