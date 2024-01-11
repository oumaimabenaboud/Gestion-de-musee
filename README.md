# Museum Management Web Application

This repository contains the source code and documentation for a web application designed to manage a museum. The application is developed using Python and the Django framework.

## Table of Contents
1. [Introduction](#introduction)
2. [Package Diagram](#package-diagram)
3. [Use Case Diagrams](#use-case-diagrams)
4. [Sequence Diagrams](#sequence-diagrams)
5. [Class Diagram](#class-diagram)
6. [Application Interface](#application-interface)
7. [Setup Instructions](#setup-instructions)

## Introduction
Welcome to the dynamic tourist website showcasing the Dar El Bacha Museum in Marrakech, Morocco.
The project aims to provide an engaging online platform that highlights the cultural richness of the Dar El Bacha Museum, offering visitors a virtual tour and comprehensive information about its exhibits, artists, events, and more.

### Package Diagram
![image](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/b9bcea8d-b881-4a05-8780-9661256ab51a)

### Use Case Diagrams
Use case diagrams provide a representation of the functional behavior of a software system. The main elements include Actors, Use Cases, and Relationships.

| Use Case Diagram for Customer Management | Use Case Diagram for Conference Management | Use Case Diagram for Artwork and Artist Management | Use Case Diagram for Visit Management |
| --- | --- | --- | --- |
| ![Customer Management](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/580ee720-c731-46a7-b9dc-45d6548257a8) | ![Conference Management](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/b7ed01cd-3de2-49e8-bfc3-96efe18f983f) | ![Artwork and Artist Management](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/9ea5cdeb-7a54-41b3-ab97-799e3fa2a317) | ![Visit Management](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/502d5cbe-75cd-45d8-92c9-ed95dd7fd81a) |

### Sequence Diagrams
Sequence diagrams graphically represent interactions between actors and the system in chronological order within the UML framework.

| Sequence Diagram: Administration Management | Sequence Diagram: Subscriber Management | Sequence Diagram: Non-subscriber Management |
| --- | --- | --- |
| ![Administration Management](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/276dc1a8-d929-4541-a038-626f729cc5a7) | ![Subscriber Management](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/97ccf8db-253d-4bf8-a452-2810d9356b3f) | ![Non-subscriber Management](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/b94be0d8-b0ff-4585-bf86-033a557bbcdc) |

### Class Diagram
The class diagram serves as the central point in object-oriented development, representing the static structure of the system in terms of classes and relationships.

  ![Class Diagram](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/cc738533-7b1c-4432-84cd-d2e947e13077)


## Application Interface

In this technical section, we provide an overview of the languages used, development tools, and screenshots of the web application's interface

- **Languages Used:**
  - Python
  - Django Framework

- **Development Tools:**
  - Visual Studio Code
  - PostgreSQL

- **Application Interfaces:**

| Home Page | Upcoming Events Page | Artwork and Artist Exhibition Page | Contact and Location Page |
| --- | --- | --- | --- |
| ![Home Page](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/94d8e9ca-9a5c-4753-b27b-8bae71a5c3ee) | ![Upcoming Events Page](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/e59f5aad-7e45-41a6-bfcd-02a363e3340a) | ![Artwork and Artist Exhibition Page](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/59ab9518-439b-4088-bf2e-5e48be9c0921) | ![Contact and Location Page](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/9976474d-e5d5-4fff-a18a-fed85c742b6a) |

| Login Page | Subscription Page | Subscriber Home Page | Reservation Page |
| --- | --- | --- | --- |
| ![Login Page](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/a631d5c8-ad78-4d9a-bdeb-b34f36d60370) | ![Subscription Page](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/a89fc43e-dd8c-4442-a7cf-ff7cd821fa91) | ![Subscriber Home Page](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/49258778-7813-401d-aaac-cd5b8efbad8b) | ![Reservation Page](https://github.com/oumaimabenaboud/Gestion-de-musee/assets/120368654/04969ef9-f236-4c3a-a0ea-0a0b3631063d) |

## Setup Instructions

Follow the steps below to set up the project environment and install the required dependencies.

### Step 1: Install Virtual Environment Wrapper (Windows)

```bash
py -m pip install virtualenvwrapper-win
```

### Step 2: Create Virtual Environment

```bash
py -m venv myvenv
```

### Step 3: Activate Virtual Environment

```bash
myvenv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
py -m pip install -r requirements.txt
```

These commands create a virtual environment named "myvenv" and activate it. Then, it installs the project dependencies listed in the "requirements.txt" file.

Now, your environment is set up, and you are ready to work on the project.
