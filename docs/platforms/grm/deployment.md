# eGRM Platform Deployment

## Clone the Django Project

Clone the django project from the repository. This will be the base for your deployment.

```bash
git clone https://github.com/e3tools/grm-backend.git
```

Then follow the installation instructions in the readme https://github.com/e3tools/grm-backend

## Set up a couchdb database

1. Install CouchDB on your server or local machine. You can find installation instructions [here](https://docs.couchdb.org/en/stable/install/index.html).
2. Create a new database for the GRM platform. You can do this using the CouchDB web interface (Fauxton).
3. Create a new user with admin privileges for the GRM platform. You can do this using the CouchDB web interface (Fauxton).
4. Make sure to note down the database name, username, and password as you will need them later.
5. Set up the couchdb variables in the django project env
COUCHDB_DATABASE = env('COUCHDB_DATABASE')
```bash

COUCHDB_ATTACHMENT_DATABASE = env('COUCHDB_ATTACHMENT_DATABASE')

COUCHDB_GRM_DATABASE = env('COUCHDB_GRM_DATABASE')

COUCHDB_GRM_ATTACHMENT_DATABASE = env('COUCHDB_GRM_ATTACHMENT_DATABASE')

COUCHDB_URL = env('COUCHDB_URL')

COUCHDB_USERNAME = env('COUCHDB_USERNAME')

COUCHDB_PASSWORD = env('COUCHDB_PASSWORD')
```

### Configure the CouchDB with the entities for the GRM Process

### Glossary of attributes


"Issue" Document

- _id
- _rev
- _internal_code
- tracking_code
- auto_increment_id
- title
- description
- attachments
- status
- assignee
- reporter
- citizen
- contact_medium: represented by string
- anonymous = Remain anonymous
- facilitator = Receive updates from facilitator
- contact = Receive updates directly
- issue_type
- created_date
- resolution_days
- resolution_date
- issue_date
- comments
- contact_information
- citizen_type: Represents the type of figure that is submitting an issue, and will be represented by an integer
  - 0 = is a beneficiary who doesn't mind his name being visible by anyone on the system.
  - 1 = is a beneficiary who wants his name to only be visible by the person solving the issue.
  - 2 = is an individual filling on behalf of someone else.
- 3 = is an organization filling on behalf of someone else.
- citizen_age_group:
- citizen_group_1
- citizen_group_2
- gender: Options are "Male", "Female", "Other", "Rather not say"
- administrative_region
- confirmed
- type
- resolution_accepted: 0 por default, 1 si fue aceptad0, 2 si no fue aceptado
- rating: 0 as default, range between 1 and 5 being 1 very unhappy and 5 very happy
- escalate_flag: false by default when this is set to true then a cronjob will reasign the issue to the level above

"issue_category" Document
- redirection_protocol: 0 (0 to assign to the head of the department, 1 to assign to the one with the fewest assignments in the department)

Example of issue document

```json
{
  "internal_code": "gbv-01",
  "tracking_code": "Tree254",
  "auto_increment_id": 1,
  "title": "Les eaux usées s'éccoulent sur le côté en raison d'un caniveau de rue bouché",
  "description": "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.",
  "attachments": [
    {
      "name": "report.pdf",
      "url": "/attachments/1253a3516c4e88550768d719be04e43d/report.pdf",
      "local_url": "/relative_path/report.pdf",
      "id": "2021-03-24T12:00:00.000Z",
      "uploaded": true,
      "bd_id": "1253a3516c4e88550768d719be04e43d"
    }
  ],
  "status": {
    "name": "Open",
    "id": 1
  },
  "logs": [
    {
      "text": "Issue collected",
      "timestamp": "2021-03-29T09:00:00.000Z",
    },
    {
      "text": "Issue Accepted",
      "timestamp": "2021-03-30T09:00:00.000Z",
    },
  ],
  "ongoing_issue": true,
  "assignee": {
    "id": 123,
    "name": "Fatima G."
  },
  "reporter": {
    "id": 4556,
    "name": "Gatta Dallo"
  },
  "citizen": "Calvin K.",
  "citizen_type" : 0,
  "citizen_age_group": {
    "name": "18-21",
    "id": 1
  },
  "gender": "Male",
  "citizen_group_1": {
    "name": "Venezuelan",
    "id": 1,
  }
  "citizen_group_2": {
    "name": "Venezuelan",
    "id": 1,
  }
  "contact_medium": "contact",
  "category": {
    "id": 1,
    "name": "Environmental",
    "confidentiality_level": "Confidential",
    "assigned_department": 1,
    "administrative_level": "County",
  },
  "issue_type": {
    "id": 1,
    "name": "Complaint"
  },
  "created_date": "2021-03-24T12:00:00.000Z",
  "resolution_days": 5,
  "resolution_date": "2021-03-29T09:00:00.000Z",
  "intake_date": "2021-03-23T00:00:00.000Z",
  "issue_date": "2021-03-29T00:00:00.000Z",
  "comments": [
    {
      "name": "Cece Conde",
      "id": 121,
      "comment": "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque",
      "due_at": "2021-03-25T08:05:23.000Z"
    }
  ],
  "contact_information": {
    "type": "email",
    "contact": "cklein@gmail.com"
  },
  "administrative_region": {
    "administrative_id": "5101",
    "name": "CU Coyah"
  },
  "confirmed": false,
  "research_result": "",
  "type": "issue"
  "resolution_accepted": 0,
  "rating": 0,
  "escalate_flag": false,
  "escalation_reasons": [
    {
      "name": "Cece Conde",
      "id": 121,
      "comment": "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque",
      "due_at": "2021-03-25T08:05:23.000Z"
    }
  ],
  "reject_reason": ""
}
```

"adl" Document
``` json
{
    "type": "adl",
    "name": "CU Coyah, Coyah",
    "photo": "https://via.placeholder.com/150",
    "location": {
    "lat": 9.6342182,
    "long": -13.6493711
    },
    "representative": {
    "id": 12,
    "name": "Mariama Sylla",
    "email": "m.sylla@anafic.com",
    "phone": "+225 620 653 674",
    "photo": "https://via.placeholder.com/150",
    "is_active": true,
    "last_active": "04-01-2021",
    "password": ""
    },
    "phases": [],
    "administrative_region": "3",
    "department": 1,
    "unique_region": 0,
    "village_secretary" = 1
}
```

"issue_age_group" Document
``` json
{
  "name": "18-21",
  "id": 1,
  "type": "issue_age_group"
}
```

"issue_citizen_group_1"
``` json
{
  "name": "Venezuelan",
  "id": 1,
  "type": "issue_citizen_group_1"
}
```

"issue_citizen_group_2"
``` json
{
    "name": "Venezuelan",
    "id": 1,
    "type": "issue_citizen_group_2"
}
```

"administrative_level" Document
``` json
{
    "administrative_id": "1656446326747883",
    "name": "SAVANES",
    "administrative_level": "commune",
    "type": "administrative_level",
    "parent_id": null,
    "latitude": 9.70643,
    "longitude": -13.38465
}
```


"issue_category" Document
``` json
{
  "name": "Environmental",
  "label": "Environmental",  // same name value (for mobile application dropdown)
  "abbreviation": "M&E",
  "id": 1,
  "value": 1, // same id value (for mobile application dropdown)
  "assigned_department": {
    "name": "Monitoring and Evaluation",
    "id": 1,
    "administrative_level": "Sub-County",
  },
  "assigned_appeal_department": {
    "name": "Monitoring and Evaluation",
    "id": 1,
    // administrative_level can be null or empty and this means the issue will stays on    the administrative level of the Goverment worker or the focal  point
    "administrative_level": "County",
  },
  "assigned_escalation_department": {
    "name": "Monitoring and Evaluation",
    "id": 1,
    "administrative_level": "Sub-County",
  },
  "confidentiality_level": "Confidential",
  "redirection_protocol": 0,
}
``` 
"issue_department" Document
``` json
{
    "name": "Monitoring and Evaluation",
    "id": 1,
    "head": {
        "id": 123,
        "name": "Fatima G."
    },
    "type": "issue_department"
}
```
"issue_status" Document
``` json
{
    "name": "Open",
    "id": 1,
    "final_status": false,
    "initial_status": false,
    "rejected_status": false,
    "open_status": true,
    "type": "issue_status"
}
```

"issue_type" Document
``` json
{
    "name": "Complaint",
    "id": 1,
    "type": "issue_type"
}
```

## Clone the mobile app react-native project

Comming Soon


