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

# Request Example Explanation

The API explained for you to use it

```json
{
    "creationDate": "2008-06-23T01:35:08.373Z", // Creation date of the roblox account
    "description": "", // Description of the roblox account
    "isBanned": false, // Is the account banned
    "lastLocation": "Website", // Last place account was seen
    "lastOnline": "2023-01-31T18:38:42Z", // Last online information
    "pastUsernames": [], // Past Usernames on Roblox
    "pastUsernamesCount": 0, // Count of past usernames
    "private": false, // Is the inventory private
    "rap": 0, // Account RAP
    "thumbnails": {
        "avatarThumbnail": "https://tr.rbxcdn.com/30DAY-Avatar-F8C66F037ACED3B0255AEBFD956E492C-Png/420/420/Avatar/Png/noFilter", // Avatar thumbnail
        "faceThumbnail": "https://tr.rbxcdn.com/30DAY-AvatarHeadshot-F8C66F037ACED3B0255AEBFD956E492C-Png/420/420/AvatarHeadshot/Png/noFilter" // Just the face thumbnail
    },
    "timeTaken": "0.7219 seconds", // How long it took to get that data
    "userId": 553440, // userId of that account
    "username": "Ilovekittys", // username of that Account
    "value": 0, // value of the Roblox account
    "verified": false // Roblox account verified (email)
}
```
