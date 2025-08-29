#define BUZZER_PIN 27

void setup() {
  Serial.begin(9600);
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');

    if (command.startsWith("BUZZ:")) {
      int duration = command.substring(5).toInt();
      Serial.println("Buzzer ON");
      digitalWrite(BUZZER_PIN, HIGH);
      delay(duration * 1000);
      digitalWrite(BUZZER_PIN, LOW);
      Serial.println("Buzzer OFF");
    }
  }
}
