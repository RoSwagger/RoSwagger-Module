[![Alt Text](https://raw.githubusercontent.com/RoSwagger/RoSwagger-Module/0e9b13b0d133f68850be905d9079bf2ccb968dd1/CreatorProgram.png)](https://discord.roswagger.com)

# Newest Updates

- We have released a new module that you can install on Python, `roswagger` via `pip install roswagger` and can be integrated by `from roswagger import Swagger`
- Release #1: https://github.com/RoSwagger/RoSwagger-Module/releases/tag/roswagger

# RoSwagger API Integration

This project integrates with the RoSwagger API, allowing you to make requests to various endpoints.

## Backend

The backend logic is implemented in `pip install roswagger` it only needs 4 lines to use and easy to integrate it into your bot.

## Creator Program

- **Website**: [roswagger.com](https://roswagger.com)
- **Creator Program**: [discord.roswagger.com](https://discord.roswagger.com)

The Creator Program offers no restrictions and is completely free. You must have an active server to participate.

## Endpoints

You can view available endpoints on the RoSwagger website. The API is structured as follows:


## Request Example

Here’s an example of a response you might receive when querying the API:

```json
{
    "creationDate": "2008-06-23T01:35:08.373Z", // The date when the Roblox account was created.
    "description": "", // A brief description of the Roblox account.
    "isBanned": false, // Indicates whether the account is banned.
    "lastLocation": "Website", // The last location where the account was active.
    "lastOnline": "2023-01-31T18:38:42Z", // The last time the account was online.
    "pastUsernames": [], // A list of previous usernames associated with the account.
    "pastUsernamesCount": 0, // The total count of past usernames.
    "private": false, // Indicates if the account's inventory is private.
    "rap": 0, // The account's RAP (Recent Average Price).
    "thumbnails": {
        "avatarThumbnail": "https://tr.rbxcdn.com/30DAY-Avatar-F8C66F037ACED3B0255AEBFD956E492C-Png/420/420/Avatar/Png/noFilter", // The URL for the avatar thumbnail.
        "faceThumbnail": "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-F8C66F037ACED3B0255AEBFD956E492C-Png/420/420/AvatarHeadshot/Png/noFilter" // The URL for the face thumbnail.
    },
    "timeTaken": "0.7219 seconds", // The time taken to retrieve this data.
    "userId": 553440, // The unique user ID of the account.
    "username": "Ilovekittys", // The current username of the account.
    "value": 0, // The value of the Roblox account.
    "verified": false // Indicates whether the account is email verified.
}

```
