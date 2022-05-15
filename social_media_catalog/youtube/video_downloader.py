# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""A method to get video metadata from a playlist."""

from typing import Any

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from social_media_catalog.youtube import Video


def get_youtube_credentials(client_secret: str = "client_secrets.json") -> Any:
    """The credentials needed to get personal play list, e.g. liked
    videos.

    Args:
        client_secret (str): A string to the filename of the client
        secret. Defaults to "client_secrets.json".
    Returns:
        Any: The OAuth 2.0 used to getvideo meta-data.
    """

    credentials = InstalledAppFlow.from_client_secrets_file(
        client_secret, ["https://www.googleapis.com/auth/youtube.readonly"]
    ).run_console()

    return build("youtube", "v3", credentials=credentials)


class VideoDownloader:
    """Gets video meta-data using YouTube Data API v3."""

    def __init__(self) -> None:
        self.playlist_id: str = ""
        self.auth_credentials: Any = None

    def get_single_page(self, page_token: str = "") -> Any:
        """Asynchronously download 50 video meta-data at a time as a
        play-list item list.

        Args:
            self: The VideoDownloader object to download
            videos.
            page_token (str, optional): The token to get the next page.
            Defaults to an empty string.

        Returns:
            Any: The meta-data for the 50 videos in the list.
        """

        return (
            self.auth_credentials.playlistItems()
            .list(
                maxResults=50,
                pageToken=page_token,
                part="snippet",
                playlistId=self.playlist_id,
            )
            .execute()
        )

    def get_playlist(self) -> "list[Video]":
        """Recursively download meta-data from a play-list using
        'get_single_page'.

        Args:
            self: The VideoDownloader object to download
            videos.

        Returns:
            list[Video]: A list of videos from a play-list.
        """

        videos = []
        page_token = ""

        while page_token is not None:
            response = self.get_single_page(page_token)

            videos.extend(
                Video(
                    video["snippet"]["resourceId"]["videoId"],
                    video["snippet"]["title"],
                )
                for video in response["items"]
            )

            page_token = (
                response["nextPageToken"]
                if "nextPageToken" in response
                else None
            )

        return videos
