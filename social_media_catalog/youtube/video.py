# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""A quick way to store information for videos, like a struct."""


from typing_extensions import Self


class Video:
    """A class to store the title and the id for YouTube videos."""

    def __init__(self: Self, video_id: str, video_title: str) -> None:
        self.video_id: str = video_id
        self.video_title: str = video_title

    def to_dict(self: Self) -> dict[str, str]:
        """Convert the Video object to a readable dictionary.

        Args:
            self (Self): The object that stores the title and the id of
            the video.

        Returns:
            dict[str, str]: The Video object as a dictionary.
        """
        return {"Id": self.video_id, "Title": self.video_title}

    @classmethod
    def from_json(cls: Self, video: dict[str, str]) -> Self:
        """Convert a json object back to a Video object.

        Args:
            cls (Self): The object that we want to convert from JSON.
            video (dict[str, str]): The dictionary that constains the keys:
            'Id' and 'Title'.

        Raises:
            ValueError: If dictionary does not contain any of the following
            keys: 'Id' or 'Title'.

        Returns:
            Video: The Video object that was converted from a dictionary.
        """
        if "Id" in video and "Title" in video:
            return cls(video["Id"], video["Title"])

        raise ValueError(
            "The one of the videos does not contain the keys:\n"
            "'Id' or 'Title'"
        )

    def __eq__(self: "Video", other: object) -> bool:
        if self is None or other is None or not isinstance(other, Video):
            return False
        return self.video_id == other.video_id and self.title == other.title
