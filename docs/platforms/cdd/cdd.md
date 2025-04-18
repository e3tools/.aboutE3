# Community Driven Development

**Community-Driven Development (CDD)** is a development approach that empowers local communities to identify, plan, and manage projects that address their own needs, often with support from external organizations or governments. It emphasizes participation, local ownership, and accountability to improve the relevance and sustainability of development efforts.

## CDD Platform
The Community Driven Development (CDD) platform is designed to empower communities to actively participate in their own development processes. It provides a suite of tools and applications that facilitate local engagement, monitoring, and implementation of development initiatives.

The platform encourages an organized CDD approach diving the activities to be performed in the process in Phases, Steps and Tasks. This are meant to be a live guide for facilitators to perform their job, reducing the amount of training necessary to deploy facilitators and provide project teams with the tools to monitor, control and evaluate the work of facilitators and the CDD Process.

Tasks are the smallest activity performed in the platform by facilitators and usually includes as form so that the facilitator can report and collect the information of the activities performed in the field. 

### CDD Web Monitoring Dashboard

The CDD Web Monitoring Dashboard is a web-based interface designed for project teams to manage and monitor CDD projects. It provides a comprehensive set of tools for tracking project progress, generating reports, and managing user roles and permissions.

#### Tech Stack

Is build on Django using postgres as a database and connects to the CDD Mobile App using CouchDB and API rest endpoints.

#### Features

- **Dashboard**: Provides an overview of project progress, including status, categories, and trends.
- **Facilitators Management**: Monitor the work of the facilitators in the field and allow the CDD Specialist to confirm the information collected submit feedback to the facilitators.
- **Reporting**: Generates reports on project progress, facilitators performance, and response times.
- **User Management**: Manages user roles and permissions within the system.

### CDD Facilitator Mobile App

The CDD Facilitator Mobile App is an offline-first tool that allows facilitators to collect data, manage tasks, and report on project activities in the field. It is designed to work seamlessly with the CDD Web Monitoring Dashboard, ensuring that all project activities are tracked and managed effectively.

#### Tech Stack

Is build on React Native and connects to the CDD Web Monitoring Dashboard using CouchDB and API rest endpoints.

#### Features

- **Offline Functionality**: Allows users to collect data without an internet connection and sync them when a connection is available.
- **Task Management**: Facilitators can view and manage their tasks organized inside Phases and Steps.
- **Data Collection**: Facilitators can collect data using forms and submit them for review.
- **Training Materials**: Provides access to training materials and resources for facilitators.


## Operationalization

The CDD platform is designed to be deployed in a way that ensures effective community engagement and project management. This includes:

- **Platform Customization**: The teams are encouraged to organize their CDD Process into Phases, Steps, Tasks and forms to collect inside tasks.
- **Couch DB Implenentations of the CDD Process**: After documenting the CDD Process in the step above the team can use JSON to create the process in CouchDB and use JSON Schema to create the forms to be used in the CDD Mobile App. This will allow the team to create the forms and deploy them in the CDD Mobile App.
- **Platform Testing**: The teams are encouraged to [deploy](deployment.md) the platform in a testing environment to test the functionalities and ensure that the platform is working as expected. this can also serve as a training environment for the project teams.
- **Training and Capacity Building**: Provide training to project teams and facilitators on how to use the platform effectively.
- **Piloting**: Conduct a pilot phase to test the platform in a real-world setting and gather feedback for improvements.
- **Scale Up**: Once the pilot is successful, scale up the platform to cover all project areas and stakeholders.

In the future we will include a repository of examples of CDD Processes, forms and training materials that can be used as a reference for the project teams. This will help to ensure that the platform is used effectively and that grievances are managed in a timely and efficient manner.
