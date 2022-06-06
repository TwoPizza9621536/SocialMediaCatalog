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
            video (dict[str, str]): The dictionary that contains the following
            keys: 'id' and 'title'.

        Raises:
            ValueError: If dictionary does not contain any of the following
            keys: 'id' or 'title'.

        Returns:
            Self: The Video object that was converted from a dictionary.
        """
        if "id" not in video or "title" not in video:
            raise ValueError(
                "The one of the videos does not contain the keys:\n"
                "'id' or 'title'"
            )

        return cls(video["id"], video["title"])
