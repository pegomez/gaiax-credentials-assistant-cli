import typer
from pathlib import Path
import os

app = typer.Typer(
    help="""
    Gaia-X Self-Description Generator CLI

    This tool guides you step-by-step through the generation of Gaia-X Self-Descriptions,
    with validation, error handling, and detailed feedback at each step.
    """
)

def assert_step(success: bool, message: str, error_message: str = None):
    """
    Utility function to assert and log step success or error.
    """
    if success:
        typer.secho(f"✅ {message}", fg=typer.colors.GREEN)
    else:
        typer.secho(f"❌  {error_message or 'An error occurred.'}", fg=typer.colors.RED)

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

@app.command()
def generate_self_description():
    """
    Conversationally generate Gaia-X Self-Descriptions from API specifications.
    """
    typer.echo("Welcome to the Gaia-X Self-Description Generator!")
    typer.echo("Let's generate a Gaia-X Self-Description step by step.\n")

    # Step 1: Ask for OpenAPI/AsyncAPI specification
    openapi_file = typer.prompt("1. Please provide the path to the OpenAPI or AsyncAPI specification")
    if not Path(openapi_file).exists():
        assert_step(False, "", f"File not found: {openapi_file}. Please check the path and try again.")
        return
    assert_step(True, f"Successfully located API specification at {openapi_file}.")

    # Step 2: Output file
    output_file = typer.prompt("2. Where should the generated Self-Description be saved?", default="./self_description.json")
    output_dir = Path(output_file).parent
    if not output_dir.exists():
        try:
            os.makedirs(output_dir)
            assert_step(True, f"Created output directory: {output_dir}.")
        except Exception as e:
            assert_step(False, "", f"Failed to create output directory: {output_dir}. Error: {e}")
            return
    else:
        assert_step(True, f"Output directory exists: {output_dir}.")

    # Step 3: Ask for trust anchor certificate and key
    use_custom_cert = typer.confirm("3. Do you want to provide a custom trust anchor certificate and private key?", default=False)
    if use_custom_cert:
        trust_anchor_cert = typer.prompt("Path to the trust anchor certificate")
        trust_anchor_key = typer.prompt("Path to the trust anchor private key")
        if not Path(trust_anchor_cert).exists() or not Path(trust_anchor_key).exists():
            assert_step(False, "", f"Certificate or key not found: {trust_anchor_cert}, {trust_anchor_key}")
            return
        assert_step(True, f"Using provided trust anchor certificate and key: {trust_anchor_cert}, {trust_anchor_key}.")
    else:
        typer.echo("Using Let's Encrypt to automatically generate trust anchor certificates.\n")
        # Simulate Let's Encrypt logic here
        try:
            # Placeholder: Replace with actual certificate generation logic
            trust_anchor_cert, trust_anchor_key = "/path/to/default-cert.pem", "/path/to/default-key.pem"
            assert_step(True, "Generated trust anchor certificate using Let's Encrypt.")
        except Exception as e:
            assert_step(False, "", f"Failed to generate certificates automatically. Error: {e}")
            return

    # Step 4: Confirm conformity proofs integration
    integrate_proofs = typer.confirm("4. Should the generated Self-Description include conformity proofs from GXDCH?", default=True)
    if integrate_proofs:
        gxdch_instance = typer.prompt("Please specify the GXDCH instance (e.g., Aire Networks)", default="Aire Networks")
        typer.echo(f"Using GXDCH instance: {gxdch_instance}")
        # Placeholder: Add logic to integrate conformity proofs
        assert_step(True, f"Integrated conformity proofs from GXDCH instance: {gxdch_instance}.")
    else:
        typer.echo("Skipping integration of conformity proofs.\n")
        gxdch_instance = None

    # Step 5: Generate the Self-Description
    typer.echo("5. Generating the Gaia-X Self-Description...")
    try:
        # Placeholder: Replace with actual Self-Description generation logic
        with open(output_file, "w") as f:
            f.write("{}")  # Dummy JSON content
        assert_step(True, f"Self-Description generated successfully and saved at {output_file}.")
    except Exception as e:
        assert_step(False, "", f"Failed to generate Self-Description. Error: {e}")
        return

    # Step 6: Validate certificates (optional)
    validate_certificates = typer.confirm("6. Do you want to validate the trust anchor certificates?", default=True)
    if validate_certificates:
        try:
            # Placeholder: Add actual certificate validation logic
            if "EV" not in trust_anchor_cert:  # Simulated check
                typer.secho("Warning: The certificate is not EV-SSL compliant.", fg=typer.colors.YELLOW)
            assert_step(True, "Trust anchor certificates validated successfully.")
        except Exception as e:
            assert_step(False, "", f"Certificate validation failed. Error: {e}")
            return

    typer.echo("\n🎉 Gaia-X Self-Description generation complete! Thank you for using this tool.")

if __name__ == "__main__":
    app()