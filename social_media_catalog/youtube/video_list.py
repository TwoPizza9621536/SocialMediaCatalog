# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""A template to store the list of videos from a playlist into json."""

from itertools import zip_longest
from typing import Any
from typing_extensions import Self


from social_media_catalog.youtube import Video


class VideoList:
    """A class to store the videos with the playlist name and id."""

    def __init__(
        self: "VideoList",
        playlist_id: str,
        playlist_name: str,
        videos: list[Video],
    ) -> None:
        self.schema: str = (
            "https://twopizza9621536.github.io/schema/json/videolist.json"
        )
        self.playlist_id: str = playlist_id
        self.playlist_name: str = playlist_name
        self.videos: list[Video] = videos

    def to_dict(self: Self) -> dict[str, Any]:
        """Convert the VideoList object to a dictionary for json usage.

        Args:
            self (Self): The object instance that stores the
            videos in a schema.

        Returns:
            dict[str, Any]: The VideoList object as a dictionary.
        """
        videos_list = []

        for video in self.videos:
            videos_list.append(video.to_dict())

        return {
            "$Schema": self.schema,
            "PlaylistId": self.playlist_id,
            "PlaylistName": self.playlist_name,
            "Videos": videos_list,
        }

    @classmethod
    def from_json(cls: Self, data: dict[str, Any]) -> Self:
        """Convert the formatted json data back to a VideoList object.

        Args:
            data (dict[str, Any]): The dictionary that constains the keys:
            'PlaylistId', 'PlaylistName' and 'Videos'.

        Raises:
            ValueError: If dictionary does not contain any of the following
            keys: 'PlaylistId', 'PlaylistName' or 'Videos'.

        Returns:
            VideoList: The object that was converted from a
            dictionary from json.
        """

        if (
            "PlaylistId" in data
            and "PlaylistName" in data
            and "Videos" in data
        ):
            video_list = []
            for video in data["Videos"]:
                video_list.append(Video.from_json(video))

            return cls(data["PlaylistId"], data["PlaylistName"], video_list)

        raise ValueError(
            "The parsed data does not contain one or more of the "
            "following keys:\n"
            "'PlaylistId', 'PlaylistName' or 'Videos'"
        )

    def __eq__(self: "VideoList", other: object) -> bool:
        if not isinstance(other, VideoList):
            return False
        for a, b in zip_longest(self.videos, other.videos):
            if not a == b:
                return False
        return True
