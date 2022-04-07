# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Unit Test for the 'video_downloader' module."""

from typing_extensions import Self
from unittest import TestCase
import json

from social_media_catalog import VideoDownloader
from social_media_catalog import VideoList
from social_media_catalog import Video

TEST_PLAYLIST_DATA = "VideoListTest.json"
PLAYLIST_ID = "PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo"


class VideoDownloaderTest(TestCase):
    """Unit tests to check if the down-loader is working as intended."""

    def test_get_video_list(self: Self) -> None:
        """Check if it can download an entire play-list and if the list is
        correct.

        Args:
            self (Self): The test object to test
            'video_downloader'.
        """

        video_downloader = VideoDownloader()
        video_downloader.playlist_id = PLAYLIST_ID
        video_downloader.auth_credentials = credentials
        video_list = video_downloader.get_video_list()

        playlist = VideoList(PLAYLIST_ID, "important videos", video_list)

        with open(TEST_PLAYLIST_DATA, encoding="utf-8") as test_file:
            json_data = json.loads(test_file.read())

        VideoList.from_json(json_data)
        self.assertEqual(json.dumps(playlist.to_dict()), json.dumps(json_data))

    def test_to_object_exceptions(self: Self) -> None:
        """Test exceptions if there are missing keys or values.

        Args:
            self (Self): The test object to test
            exceptions in 'video_downloader'.
        """
        dict_to_video_data = {"Title": "Testing 123"}
        dict_to_video_list_data = {"PlaylistId": "ABC1DEF2GHI3JKL4MNO5"}

        with self.assertRaises(ValueError):
            Video.from_json(dict_to_video_data)

        with self.assertRaises(ValueError):
            VideoList.from_json(dict_to_video_list_data)
