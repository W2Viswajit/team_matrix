#AI-Powered Dynamic Environment Generator for Meta Quest 2
##Overview
This project is an immersive VR application designed for the Meta Quest 2 platform. It uses Unity as the development environment and integrates the OpenAI API to allow users to create and interact with 3D environments through natural language input.

The application enables users to:

Generate dynamic 3D environments based on chat-based inputs.
Interact with a custom-built VR user interface (UI) optimized for virtual reality.
Leverage the OpenAI API for conversational inputs and environment generation prompts.
Features
-1. Dynamic Environment Generation
Users can describe their desired environment (e.g., "Create a tropical island with palm trees and a beach.")
The system translates text input into 3D assets and generates a corresponding VR scene in real-time.
-2. Integrated VR UI
A fully interactive VR user interface allows users to type, chat, and submit their inputs seamlessly.
Uses Unity's VR-compatible UI elements and sample assets from the Unity Asset Store.
-3. OpenAI-Powered Interaction
The application leverages OpenAI’s generative AI models to understand natural language and refine environment specifications.
Context-aware suggestions and corrections improve user experience during input.
System Requirements
Hardware: Meta Quest 2
Software:
Unity (2023.1 or later)
OpenAI API Key
Meta Quest 2 SDK
Getting Started
-1. Prerequisites
Ensure the following software and tools are installed:

Unity Hub and Editor (2023.1 or later)
Meta Quest 2 device setup with the Meta Quest Developer Hub
sk-JeLY4pInXTEQjCTeA2YUGZ-3HO6YN_jj2Fy3EBOI_iT3BlbkFJ-I1esxQd4qLVqK3dpWUwHF7Nnmeqtvwwozdv4eQdAA
##2. Clone the Repository
git clone https://github.com/W2Viswajit/team_matrix.git 
cd ai-vr-environment-generator  
##3. Setup Unity Project
Open the project in Unity.
Import required packages:
Oculus Integration package (for Meta Quest 2 compatibility).
OpenAI API integration package (custom or third-party).
Unity UI Toolkit.
Set up the build platform for Android (Meta Quest 2’s operating system).
##4. Configure OpenAI API
In the project, locate the script managing OpenAI API requests (e.g., OpenAIManager.cs).
Add your OpenAI API key:
private string apiKey = "sk-JeLY4pInXTEQjCTeA2YUGZ-3HO6YN_jj2Fy3EBOI_iT3BlbkFJ-I1esxQd4qLVqK3dpWUwHF7Nnmeqtvwwozdv4eQdAA";  
##5. Run the Application
Connect your Meta Quest 2 device to your system.
Build and deploy the Unity project to the headset.
Launch the application from the device menu.
##Usage
Launch the application and access the VR UI.
Use the on-screen keyboard or voice input to describe your desired environment.
Submit the input to see the environment generated dynamically in VR.
Interact with the generated environment or provide additional inputs to modify it.
##Built With
Unity - The game engine powering the application.
Meta Quest SDK - For VR development and interaction.
OpenAI API - For text-to-environment translation and conversational functionality.
##Future Enhancements
Adding voice-to-text input for seamless environment descriptions.
Expanding the library of 3D assets for more diverse environments.
Implementing real-time collaboration for multi-user VR experiences.
##Contributors
Rohan Naveen Gajan
Abhishek
Dishita Kamath
R Viswajit
##License
This project is licensed under the MIT License. See the LICENSE file for details.

##Acknowledgments
Unity Asset Store for sample assets and resources.
OpenAI for the powerful conversational AI APIs.