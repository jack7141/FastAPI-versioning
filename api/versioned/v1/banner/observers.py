from common.decorator import subscribe_to


@subscribe_to("user_signup")
def send_welcome_email(data: dict):
    print(f"Sending welcome email to {data['email']} with username {data['username']}")