import argparse
import os

MOCK_ORDERS = {
    "OD1001": {"status": "SHIPPED", "eta": "2026-08-24", "city": "Mumbai"},
    "OD1002": {"status": "PROCESSING", "eta": "2026-08-26", "city": "Pune"},
    "OD1003": {"status": "DELIVERED", "eta": "2026-08-18", "city": "Bengaluru"},
}


def get_order_status(order_id: str) -> dict:
    order_id = str(order_id).strip().upper()
    return MOCK_ORDERS.get(order_id, {"status": "UNKNOWN", "eta": None, "city": None})


def build_reply(order_id: str) -> str:
    info = get_order_status(order_id)
    if info["status"] == "UNKNOWN":
        return f"No order found for {order_id}. Please double-check the ID."
    return (
        f"Order {order_id}: status={info['status']}, "
        f"ETA={info['eta']}, shipping to {info['city']}."
    )


def deploy():
    import vertexai
    from vertexai.preview import reasoning_engines

    project = os.environ["GOOGLE_CLOUD_PROJECT"]
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "asia-south1")
    staging_bucket = os.environ["GOOGLE_CLOUD_STAGING_BUCKET"]

    vertexai.init(project=project, location=location, staging_bucket=staging_bucket)

    remote_app = reasoning_engines.ReasoningEngine.create(
        build_reply,
        requirements=["google-cloud-aiplatform"],
    )
    print(f"Deployed Reasoning Engine: {remote_app.resource_name}")
    return remote_app


def query(resource_name: str, order_id: str):
    from vertexai.preview import reasoning_engines

    remote_app = reasoning_engines.ReasoningEngine(resource_name)
    response = remote_app.query(message=f"What is the status of order {order_id}?")
    print(response)


def demo():
    print("Offline demo mode (no GCP credentials needed):")
    for oid in ("OD1001", "OD9999"):
        print(f"Q: What is the status of order {oid}?")
        print(f"A: {build_reply(oid)}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vertex AI Reasoning Engine order-status agent")
    parser.add_argument("--deploy", action="store_true", help="deploy to Vertex AI Reasoning Engines")
    parser.add_argument("--query", metavar="RESOURCE_NAME", help="query a deployed engine")
    parser.add_argument("--order-id", default="OD1001")
    args = parser.parse_args()

    if args.deploy:
        deploy()
    elif args.query:
        query(args.query, args.order_id)
    else:
        demo()
