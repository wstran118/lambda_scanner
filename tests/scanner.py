import argparse
import boto3
from lambda_function import LambdaScanner

def main():
    parser = argparse.ArgumentParser(description="Secure Lambda Vulnerability Scanner")
    parser.add_argument("--region", default="us-east-1", help="AWS region")
    parser.add_argument("--output", default="report.json", help="Output file")
    parser.add_argument("--format", choices=["json","html"], default="json", help="Report format")

    boto3.setup_default_session(region_name=args.region)
    scanner = LambdaScanner()
    vulnerabilities = scanner.scan_functions()
    report = scanner.generate_report(vulnerabilities, args.format)

    with open(args.output, "w") as f:
        f.write(report)
    print(f"Saved report to {args.output}")

if __name__ == "__main__":
    main()