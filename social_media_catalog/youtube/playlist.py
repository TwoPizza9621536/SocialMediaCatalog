# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""A template to store the list of videos from a playlist into json."""

from dataclasses import dataclass, asdict
from typing import Any

from social_media_catalog.youtube import Video


@dataclass(frozen=True, order=True)
class Playlist:
    """A class to store the videos with the playlist name and id."""

    playlist_id: str
    playlist_name: str
    videos: "list[Video]"

    def to_dict(self) -> "dict[str, Any]":
        """Convert the VideoList object to a dictionary for json usage.

        Args:
            self: The object instance that stores the
            videos in a schema.

        Returns:
            dict[str, Any]: The VideoList object as a dictionary.
        """
        videos_list = [asdict(video) for video in self.videos]

        return {
            "playlistId": self.playlist_id,
            "playlistName": self.playlist_name,
            "videos": videos_list,
        }

    @classmethod
    def from_json(cls, data: "dict[str, Any]"):
        """Convert a formatted json data back to a VideoList object.

        Args:
            data (dict[str, Any]): The dictionary that contains the following
            keys: 'playlistId', 'playlistName' and 'videos'.

        Raises:
            ValueError: If dictionary does not contain any of the following
            keys: 'playlistId', 'playlistName' or 'videos'.

        Returns:
            Self: The object that was converted from a
            dictionary from json.
        """

        if (
            "playlistId" not in data
            or "playlistName" not in data
            or "videos" not in data
        ):
            raise ValueError(
                "The parsed data does not contain one or more of the "
                "following keys:\n"
                "'playlistId', 'playlistName' or 'videos'"
            )

        video_list = [Video.from_json(video) for video in data["videos"]]
        return cls(data["playlistId"], data["playlistName"], video_list)
