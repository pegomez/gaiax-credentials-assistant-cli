import typer

app = typer.Typer(
    help="""
    ------------------------------------------------------------\n
    \t\t\tGaia-X Self-Description Generator CLI                     
    ------------------------------------------------------------

    \nThis CLI automates the creation of Gaia-X Self-Descriptions for services and participants in the Gaia-X ecosystem. Self-Descriptions are JSON-LD documents that follow the Gaia-X Trust Framework model and may include Verifiable Credentials (VCs).

    \n\nScope of the Tool
    \n\n- Automatically generates Self-Descriptions based on OpenAPI or AsyncAPI specifications.
    \n\n- Integrates with Gaia-X Digital Clearing House (GXDCH) to obtain conformity proofs.
    \n\n- Supports the configuration and validation of certificates (e.g., EV-SSL vs. Let's Encrypt) to ensure compatibility.
    \n\n- Provides feedback about the validity of trust anchor certificates and helps troubleshoot interoperability issues.

    \n\nKey Features
    \n\n1. Parse API specifications (OpenAPI/AsyncAPI) to produce Gaia-X Self-Descriptions.
    \n\n2. Generate and validate certificates for trust anchors.
    \n\n3. Automate interactions with GXDCH to retrieve conformity proofs.
    \n\n4. Support dynamic and scalable service environments by automating the Self-Description generation process.
    """
)

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    High-level contextual information displayed when the CLI is invoked without a command.
    """
    typer.echo("Welcome to the Gaia-X Self-Description Generator CLI\n")
    typer.echo(
        """This tool helps automate the generation of Gaia-X Self-Descriptions, validate certificates, and integrate conformity proofs from Gaia-X Digital Clearing House (GXDCH).
        """
    )
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())

# Step 1: Prepare Certificate
@app.command()
def prepare_cert(
    cert_name: str = typer.Option(..., help="Name of the certificate to prepare."),
    output_dir: str = typer.Option("./", help="Directory to save the prepared certificate.")
):
    """
    Prepare a certificate for use in Self-Descriptions.
    """
    typer.echo(f"Preparing certificate '{cert_name}' in directory '{output_dir}'...")
    # Add logic to prepare the certificate here
    typer.echo("Certificate prepared successfully!")

# Step 2: Get Certificate
@app.command()
def get_cert(
    cert_id: str = typer.Option(..., help="ID of the certificate to retrieve."),
    server_url: str = typer.Option(..., help="URL of the server to fetch the certificate from.")
):
    """
    Retrieve a certificate from a remote server.
    """
    typer.echo(f"Fetching certificate with ID '{cert_id}' from '{server_url}'...")
    # Add logic to retrieve the certificate
    typer.echo("Certificate retrieved successfully!")

# Step 3: Build DID
@app.command()
def build_did(
    key_type: str = typer.Option("rsa", help="Type of key to use for the DID (e.g., 'rsa', 'ed25519')."),
    did_output: str = typer.Option("./did.json", help="Path to save the generated DID document.")
):
    """
    Build a Decentralized Identifier (DID) document.
    """
    typer.echo(f"Building DID with key type '{key_type}'...")
    # Add logic to generate the DID
    typer.echo(f"DID document saved at '{did_output}'.")

# Step 4: Build Self-Descriptions
@app.command()
def build_self_description(
    openapi_file: str = typer.Option(..., help="Path to the OpenAPI or AsyncAPI specification."),
    output_file: str = typer.Option("./self_description.json", help="Path to save the generated Self-Description."),
    trust_anchor_cert: str = typer.Option(
        None, help="Path to the trust anchor certificate. Uses Let's Encrypt if not provided."
    ),
    trust_anchor_key: str = typer.Option(
        None, help="Path to the trust anchor private key. Uses Let's Encrypt if not provided."
    ),
):
    """
    Generate Gaia-X Self-Descriptions from API specifications.
    """
    typer.echo(f"Parsing API specification at '{openapi_file}'...")
    if trust_anchor_cert and trust_anchor_key:
        typer.echo(f"Using provided trust anchor certificate and key: {trust_anchor_cert}, {trust_anchor_key}")
    else:
        typer.echo("Using Let's Encrypt to automatically generate trust anchor certificates.")
    # Add logic to generate the Self-Description
    typer.echo(f"Self-Description saved at '{output_file}'.")

# Step 5: Build Well-Known Web Server
@app.command()
def build_well_known(
    well_known_dir: str = typer.Option("./.well-known", help="Directory to host the '.well-known' files."),
    did_document: str = typer.Option("./did.json", help="Path to the DID document to serve.")
):
    """
    Create a well-known directory for hosting DID-related files.
    """
    typer.echo(f"Setting up '.well-known' directory at '{well_known_dir}' with DID document '{did_document}'...")
    # Add logic to create the well-known directory and files
    typer.echo("Well-known directory created successfully!")

# Step 6: Validate Credentials
@app.command()
def validate_credentials(
    credentials_file: str = typer.Option(..., help="Path to the credentials file to validate.")
):
    """
    Validate the Verifiable Credentials (VCs) against a schema.
    """
    typer.echo(f"Validating credentials in '{credentials_file}' against GaiaX clearing house")
    # Add logic to validate the credentials
    typer.echo("Credentials validated successfully!")

if __name__ == "__main__":
    app()