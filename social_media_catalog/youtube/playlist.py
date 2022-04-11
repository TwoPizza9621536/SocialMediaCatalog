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
    videos: list[Video]

    def to_dict(self) -> dict[str, Any]:
        """Convert the VideoList object to a dictionary for json usage.

        Args:
            self: The object instance that stores the
            videos in a schema.

        Returns:
            dict[str, Any]: The VideoList object as a dictionary.
        """
        videos_list = [asdict(video) for video in self.videos]

        return {
            "PlaylistId": self.playlist_id,
            "PlaylistName": self.playlist_name,
            "Videos": videos_list,
        }

    @classmethod
    def from_json(cls, data: dict[str, Any], /):
        """Convert the formatted json data back to a VideoList object.

        Args:
            data (dict[str, Any]): The dictionary that constains the keys:
            'PlaylistId', 'PlaylistName' and 'Videos'.

        Raises:
            ValueError: If dictionary does not contain any of the following
            keys: 'PlaylistId', 'PlaylistName' or 'Videos'.

        Returns:
            Self: The object that was converted from a
            dictionary from json.
        """

        if (
            "PlaylistId" in data
            and "PlaylistName" in data
            and "Videos" in data
        ):
            video_list = [Video.from_json(video) for video in data["Videos"]]
            return cls(data["PlaylistId"], data["PlaylistName"], video_list)

        raise ValueError(
            "The parsed data does not contain one or more of the "
            "following keys:\n"
            "'PlaylistId', 'PlaylistName' or 'Videos'"
        )
