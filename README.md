# RoSwagger API Integration

This project integrates with the RoSwagger API, allowing you to make requests to various endpoints.

## Backend

The backend logic is implemented in `modules/request.py`. You can modify this file to fit your needs and integrate it into your bot.

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
    "creationDate": "2006-02-27T21:06:40.3Z",
    "description": "Welcome to the Roblox profile! This is where you can check out the newest items in the catalog, and get a jumpstart on exploring and building on our Imagination Platform. If you want news on updates to the Roblox platform, or great new experiences to play with friends, check out blog.roblox.com. Please note, this is an automated account. If you need to reach Roblox for any customer service needs find help at www.roblox.com/help",
    "isBanned": false,
    "lastLocation": "Website",
    "lastOnline": "2023-04-17T21:39:32Z",
    "pastUsernames": [],
    "pastUsernamesCount": 0,
    "private": false,
    "rap": 294671811,
    "thumbnails": {
        "avatarThumbnail": "https://tr.rbxcdn.com/30DAY-Avatar-310966282D3529E36976BF6B07B1DC90-Png/420/420/Avatar/Png/noFilter",
        "faceThumbnail": "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-310966282D3529E36976BF6B07B1DC90-Png/420/420/AvatarHeadshot/Png/noFilter"
    },
    "timeTaken": "0.2878 seconds",
    "userId": 1,
    "username": "Roblox",
    "value": 464088625,
    "verified": true
}

## Request Example Explanation

This section provides an explanation of the API response structure and its fields for easier understanding and usage.

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

