# AI-Powered Dynamic Environment Generator for Meta Quest 2

## Overview
This project is an immersive VR application designed for the **Meta Quest 2** platform. It uses **Unity** as the development environment and integrates the **OpenAI API** to allow users to create and interact with 3D environments through natural language input.

The application enables users to:
- **Generate dynamic 3D environments** based on chat-based inputs.
- **Interact with a custom-built VR user interface (UI)** optimized for virtual reality.
- Leverage the **OpenAI API** for conversational inputs and environment generation prompts.

## Features
### 1. Dynamic Environment Generation
- Users can describe their desired environment (e.g., "Create a tropical island with palm trees and a beach.").
- The system translates text input into 3D assets and generates a corresponding VR scene in real-time.

### 2. Integrated VR UI
- A fully interactive VR user interface allows users to type, chat, and submit their inputs seamlessly.
- Uses Unity's VR-compatible UI elements and **sample assets** from the Unity Asset Store.

### 3. OpenAI-Powered Interaction
- The application leverages OpenAI’s generative AI models to understand natural language and refine environment specifications.
- Context-aware suggestions and corrections improve user experience during input.

## System Requirements
- **Hardware:** Meta Quest 2
- **Software:**
  - Unity (2023.1 or later)
  - OpenAI API Key (Configured via environment variables)
  - Meta Quest 2 SDK

## Getting Started

### 1. Prerequisites
Ensure the following software and tools are installed:
- Unity Hub and Editor (2023.1 or later)
- Meta Quest 2 device setup with the Meta Quest Developer Hub
- OpenAI API key

### 2. Clone the Repository
git clone https://github.com/W2Viswajit/team_matrix.git
cd team_matrix

### 3. Setup Unity Project

1. Open the project in Unity.
2. Import required packages:
   - **Oculus Integration package** (for Meta Quest 2 compatibility).
   - **OpenAI API integration package** (custom or third-party).
   - **Unity UI Toolkit**.
3. Set up the build platform for **Android** (Meta Quest 2’s operating system).

### 4. Configure Environment Variables

1. Create a `.env` file in the root of your project directory.
2. Add your OpenAI API key securely:
   ```makefile
   OPENAI_API_KEY=your-openai-api-key

3. Update the project script to read the key from environment variables instead of hardcoding:
    private string apiKey = System.Environment.GetEnvironmentVariable("OPENAI_API_KEY");

### 5. Run the Application

1. Connect your Meta Quest 2 device to your system.
2. Build and deploy the Unity project to the headset.
3. Launch the application from the device menu.

---

## Usage

1. Launch the application and access the VR UI.
2. Use the on-screen keyboard or voice input to describe your desired environment.
3. Submit the input to see the environment generated dynamically in VR.
4. Interact with the generated environment or provide additional inputs to modify it.

---

## Built With

- **Unity** - The game engine powering the application.
- **Meta Quest SDK** - For VR development and interaction.
- **OpenAI API** - For text-to-environment translation and conversational functionality.

---

## Future Enhancements

- Adding voice-to-text input for seamless environment descriptions.
- Expanding the library of 3D assets for more diverse environments.
- Implementing real-time collaboration for multi-user VR experiences.

---

## Contributors

- Rohan Naveen Gajan
- Abhishek Venkatesh
- Dishita Kamath
- R. Viswajit

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
