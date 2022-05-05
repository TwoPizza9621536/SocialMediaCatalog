# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""A quick way to store information for videos, like a struct."""


from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Video:
    """A class to store the title and the id for YouTube videos."""

    video_id: str
    video_title: str

    @classmethod
    def from_json(cls, video: "dict[str, str]"):
        """Convert a json object back to a Video object.

        Args:
            cls: The object that we want to convert from JSON.
            video (dict[str, str]): The dictionary that constains the keys:
            'Id' and 'Title'.

        Raises:
            ValueError: If dictionary does not contain any of the following
            keys: 'id' or 'title'.

        Returns:
            Self: The Video object that was converted from a dictionary.
        """
        if "id" in video and "title" in video:
            return cls(video["id"], video["title"])

        raise ValueError(
            "The one of the videos does not contain the keys:\n"
            "'id' or 'title'"
        )
