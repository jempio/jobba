# Jobba - Easily Schedule Interviews

## **Context**
Job seekers often apply to hundreds of positions over several months, leading to a manual and time-consuming interview scheduling process. The back-and-forth emails required to coordinate interviews result in unnecessary delays, missed opportunities, or even unnoticed responses. 

To solve this, Jobba will integrate **calendar-based interview scheduling**, allowing users to **suggest available time slots** and receive **automated reminders**. This feature will help users reduce scheduling friction with recruiters, avoid missing important interviews, and track all scheduled interviews in one place.

---

## **Current State**
- Jobba’s **interview scheduling feature** needs to be built from the ground up.
- There is **no dedicated dashboard or calendar** for tracking scheduled interviews.
- **Gmail integration** currently extracts company names from emails but does not capture interview dates, times, or meeting links.

---

## **Jobs To Be Done**
### **1. Implement Email Parsing**
- **Gmail API** scans emails → Extracts interview details.
- **Implement an email parser** to detect interview-related emails using keywords and structured data.
- **Ensure secure OAuth authentication** for handling Gmail API requests.

### **2. Database Setup**
- **Create a schema** for tracking scheduled interviews.
- **Store extracted interview details** in Jobba’s database.
- **Link interviews to respective job applications** within Jobba.

### **3. Interview Dashboard (React)**
- **Users track interviews** in an organized UI.
- **Scheduling methods**:
  1. Share availability link with recruiter (self-scheduling).
  2. Accept proposed time with one-click confirmation.
  3. Manually set a time (if needed).
- **Calendar sync**: Jobba syncs with the user’s calendar and sends reminders:
  - When a new interview is detected.
  - Before upcoming interviews.
  - When a recruiter confirms a proposed time.

---

## **Use Cases**
### **1. Scheduling an Interview via Jobba**
1. Select a job application and click **“Schedule Interview.”**
2. Suggest available time slots based on preferences.
3. Confirm the interview once the recruiter selects a time.
4. Receive a **confirmation email** and **calendar invite**.
5. Get an **automatic reminder** before the interview.

### **2. Sharing Availability with a Recruiter**
1. Click **“Share Availability”** from the job application dashboard.
2. Select preferred time slots from the calendar.
3. Generate a **shareable link** for the recruiter.

### **3. Receiving an Automated Interview from Email**
1. **Jobba scans incoming emails** for interview-related messages.
2. Extracts **date, time, and recruiter details**.
3. Suggests a **pre-filled scheduling form** for quick confirmation.

---

## **Edge Cases**
### **1. Scheduling an Interview**
- **No available time slots set** → Prompt the user to set availability.
- **Recruiter proposes a time outside of available slots** → Allow manual confirmation or propose alternatives.
- **User forgets to confirm** → Send an automated reminder.

### **2. Sharing Availability**
- **User has not set availability** → Prompt them before generating a shareable link.
- **Recruiter does not select a time** → Send a follow-up email reminder.
- **Time slot is no longer available** → Notify the recruiter and prompt the user to update availability.

### **3. Miscellaneous**
- **Email parsing fails** → Show a manual entry form.
- **Multiple interview requests detected** → Let the user choose the correct interview.
- **User deletes an interview request email** → Allow manual entry.
- **Recruiter cancels or reschedules** → Detect cancellation emails and notify the user.

---

## **Data Model**
We will use **FastAPI with SQLModel** and a **PostgreSQL database** to efficiently manage interview data.

### **Collections**
#### **1. Interviews Collection**
| Field            | Type   | Description |
|-----------------|--------|-------------|
| `id`           | int    | Unique interview ID |
| `userId`       | int    | Jobba user ID |
| `jobId`        | int    | Associated job application ID |
| `recruiterEmail` | string | Recruiter's email |
| `scheduledTime` | date   | Confirmed interview time |
| `status`       | array<string> | ["Pending", "Scheduled", "Completed", "Rescheduled"] |
| `calendarEventId` | int  | Google Calendar event ID |

#### **2. User Availability Collection**
| Field           | Type   | Description |
|----------------|--------|-------------|
| `userId`       | int    | Jobba user ID |
| `availableSlots` | array<date> | User's available time slots |
| `timezone`     | string | User's preferred time zone |

### **Example Data**
```json
{
    "interviews": [
        {
            "id": 1001,
            "userId": 5023,
            "jobId": 7890,
            "recruiterEmail": "recruiter@example.com",
            "scheduledTime": "2025-02-10T14:30:00Z",
            "status": ["Scheduled"],
            "calendarEventId": 30567
        },
        {
            "id": 1002,
            "userId": 5023,
            "jobId": 7891,
            "recruiterEmail": "hiring.manager@company.com",
            "scheduledTime": "2025-02-12T10:00:00Z",
            "status": ["Pending"],
            "calendarEventId": 30999
        }
    ],
    "user_availability": {
        "userId": 5023,
        "availableSlots": [
            "2025-02-08T09:00:00Z",
            "2025-02-08T14:00:00Z",
            "2025-02-09T11:30:00Z",
            "2025-02-10T13:00:00Z"
        ],
        "timezone": "America/New_York"
    }
}
```

## Overall Approach

### **Frontend**
- Implement interview scheduling UI in React.
- Create forms for setting availability and confirming interviews.
- Show interview status and reminders in the dashboard.

### **Backend**
- Build API endpoints for scheduling and managing interviews.
- Integrate with Gmail API for extracting interview invites.
- Sync scheduled interviews with Google Calendar.

### **Notifications/Automation**
- Send automated email reminders before interviews.
- Provide alerts for scheduling conflicts.
- Generate pre-filled follow-up emails for rescheduling.

---

## **Showing User’s Interviews**
Since we have the `userId` field on each interview record, we can query against that to retrieve all interviews associated with a user. This eliminates the need to modify the **User Model** itself. Instead, interviews are stored separately and fetched via queries when needed.

---

## **Trade-offs**
The primary alternative is to store the list of interviews in the **User Model**:

```json
{
    "userId": 5023,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "interviews": [
        {
            "id": 1001,
            "jobId": 7890,
            "recruiterEmail": "recruiter@example.com",
            "scheduledTime": "2025-02-10T14:30:00Z",
            "status": ["Scheduled"],
            "calendarEventId": 30567
        },
        {
            "id": 1002,
            "jobId": 7891,
            "recruiterEmail": "hiring.manager@company.com",
            "scheduledTime": "2025-02-12T10:00:00Z",
            "status": ["Pending"],
            "calendarEventId": 30999
        }
    ]
}
