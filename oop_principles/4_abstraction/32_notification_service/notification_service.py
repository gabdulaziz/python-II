from abc import ABC, abstractmethod
from datetime import datetime


class NotificationService(ABC):
    def __init__(self, service_name: str):
        self.service_name = service_name
        self.sent_count = 0

    @abstractmethod
    def validate_recipient(self, recipient: str) -> bool:
        """Check if recipient is valid"""
        pass

    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        """Send message to recipient, return True if successful"""
        pass

    @abstractmethod
    def get_cost(self) -> float:
        """Return cost per notification"""
        pass

    def log_notification(self, recipient: str, status: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.service_name}: {recipient} - {status}")
        if status.upper() == "SUCCESS":
            self.sent_count += 1


class EmailNotification(NotificationService):
    def __init__(self):
        super().__init__("Email Service")

    def validate_recipient(self, recipient: str) -> bool:
        return "@" in recipient

    def send(self, recipient: str, message: str) -> bool:
        if self.validate_recipient(recipient):
            print(f"Sending email to {recipient}: {message}")
            self.log_notification(recipient, "SUCCESS")
            return True
        else:
            self.log_notification(recipient, "FAILED")
            return False

    def get_cost(self) -> float:
        return 0.001


class SMSNotification(NotificationService):
    def __init__(self):
        super().__init__("SMS Service")

    def validate_recipient(self, recipient: str) -> bool:
        return recipient.startswith("+")

    def send(self, recipient: str, message: str) -> bool:
        if self.validate_recipient(recipient):
            print(f"Sending SMS to {recipient}: {message}")
            self.log_notification(recipient, "SUCCESS")
            return True
        else:
            self.log_notification(recipient, "FAILED")
            return False

    def get_cost(self) -> float:
        return 0.05


class PushNotification(NotificationService):
    def __init__(self):
        super().__init__("Push Notification Service")

    def validate_recipient(self, recipient: str) -> bool:
        return len(recipient) > 5

    def send(self, recipient: str, message: str) -> bool:
        if self.validate_recipient(recipient):
            print(f"Sending push notification to device {recipient}: {message}")
            self.log_notification(recipient, "SUCCESS")
            return True
        else:
            self.log_notification(recipient, "FAILED")
            return False

    def get_cost(self) -> float:
        return 0.01



if __name__ == "__main__":
    try:
        service = NotificationService("Generic")
    except TypeError as e:
        print(f"Error: {e}")


    email = EmailNotification()
    sms = SMSNotification()
    push = PushNotification()


    email.send("user@example.com", "Hello!")
    sms.send("+1234567890", "Verification code: 123456")
    push.send("device_abc123", "New message received")

    # Invalid recipients
    email.send("invalid-email", "Test")
    sms.send("1234567890", "Test")
    push.send("dev1", "Test")


    print(f"Email cost: ${email.get_cost():.3f}, Sent: {email.sent_count}")
    print(f"SMS cost: ${sms.get_cost():.3f}, Sent: {sms.sent_count}")
    print(f"Push cost: ${push.get_cost():.3f}, Sent: {push.sent_count}")


    def send_batch(service: NotificationService, recipients, message):
        for recipient in recipients:
            service.send(recipient, message)
        total_cost = service.sent_count * service.get_cost()
        print(f"Total sent: {service.sent_count}, Total cost: ${total_cost:.3f}")


    send_batch(email, ["alice@test.com", "bob@test.com"], "Batch message")
    send_batch(sms, ["+1111111111", "+2222222222"], "Batch SMS")
    send_batch(push, ["device_xyz789", "device_abc456"], "Batch push")