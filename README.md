# Power Pay with Rapyd
B2B payments are done smart, fast, and in an extra secure way with Microsoft's Power Platform tools

### NOTE: Please check the Judge section for email and password to access the Microsoft office tenant used to build this application and steps to use/test the application

## YouTube Demo Video 📺📺
### [Click here to watch the demo](https://www.youtube.com/watch?v=WWD2JrgJoss&ab_channel=LateNightCodewithSanthosh)


<a href="https://youtu.be/WWD2JrgJoss">
  <img src="https://img.youtube.com/vi/WWD2JrgJoss/hqdefault.jpg" alt="video">
</a>

## Setup environment variable
#### Please set the below variables
- RAPYD_ACCESS_KEY - Rapyd sandbox access key
- RAPYD_SECRET_KEY - Rapyd sandbox secret key
- MSFT_CLIENT_ID - Microsoft Azure Active Directory Client ID
- MSFT_CLIENT_SECRET - Microsoft Azure Active Directory Client Secret
- TENANT_ID - Microsoft Account Tenant ID
- RAPYD_URL - Rapyd's sandbox URL
- SITE_ID - SharePoint Site ID you wish to connect to

## Run Tests
#### Note: Set the Rapyd environment variable before running the tests

```
python -m unittest discover
```

## Architecture Diagram
![Architecture Diagram](./PowerAppsImages/architecture-diagram.png)


## Checkout Page - Embedded inside Microsoft Teams
![Checkout Page - Embedded inside Microsoft Teams](./PowerAppsImages/checkout-page-inside-teams.png)

## Dashboard - Dark
![Dashboard - Dark](./PowerAppsImages/dashboard-dark.png)


## Invoice Generation View - Dark
![Invoice Generation View - Dark](./PowerAppsImages/invoice-generation-dark.png)

## Loading Screen
![Loading Screen](./PowerAppsImages/loading-screen.png)

## Teams Approval Flow - Adaptive Card
![Teams Approval Flow - Adaptive Card](./PowerAppsImages/approval-inside-teams.png)
## Invoice View Mode - Dark
![Invoice View Mode - Dark](./PowerAppsImages/invoice-view-mode-dark.png)
## Invoice Update email trigger
![Invoice Update email trigger](./PowerAppsImages/invoice-update-mail-trigger.png)

## Invoice List View - Reload - Dark
![Invoice List View - Reload - Dark](./PowerAppsImages/invoice-list-view-dark.png)

## Checkout Page Filled - Dark
![Checkout Page Filled - Dark](./PowerAppsImages/checkout-page-filled.png)

## Checkout Page Success
![Checkout Page Success](./PowerAppsImages/checkout-page-success.png)

## SharePoint - Invoice List
![SharePoint - Invoice List](./PowerAppsImages/invoice-list-view-SharePoint.png)
## Invoice Generation Power Automate Flow
![Invoice Generation Power Automate Flow](./PowerAppsImages/invoice-generation-power-automate-flow.png)
## Invoice Generation Power Automate Flow - Runs
![Invoice Generation Power Automate Flow - Runs](./PowerAppsImages/invoice-generation-power-automate-flow-runs.png)

## Invoice Approval Power Automate Flow
![Invoice Approval Power Automate Flow](./PowerAppsImages/invoice-approval-power-automate-flow.png)

## Invoice Approval Power Automate Flow - Runs
![Invoice Approval Power Automate Flow - Runs](./PowerAppsImages/invoice-approvl-power-automate-flow-runs.png)
## Invoice Approval Rejected email
![Invoice Approval Rejected email](./PowerAppsImages/invoice-rejected-email-trigger.png)
## Invoice View Mode - Light
![Invoice View Mode - Light](./PowerAppsImages/invoice-view-mode-light.png)

## Invoice Generation View - Light
![Invoice Generation View - Light](./PowerAppsImages/invoice-generation-light.png)

## Invoice List View - Light
![Invoice List View - Light](./PowerAppsImages/invoice-list-view-light.png)
## Dashboard - Light
![Dashboard - Light](./PowerAppsImages/dashboard-light.png)
