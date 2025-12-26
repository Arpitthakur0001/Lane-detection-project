from inference_sdk import InferenceHTTPClient


def detect_lanes(image_path):
    """
    Detects lane markings from a road image using a deployed inference workflow.
    """
    client = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com",
        api_key="YOUR_API_KEY"
    )

    result = client.run_workflow(
        workspace_name="arpit-ai-projects",
        workflow_id="detect-count-and-visualize-2",
        images={"image": image_path}
    )

    return result


if __name__ == "__main__":
    output = detect_lanes("images/input.jpg")
    print(output)
