# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Unit Test for downloading video metadata."""

from typing_extensions import Self
from unittest import TestCase
import json

from social_media_catalog.youtube import get_youtube_credentials
from social_media_catalog.youtube import VideoDownloader
from social_media_catalog.youtube import Playlist
from social_media_catalog.youtube import Video

TEST_PLAYLIST_DATA = "playlist.json"
PLAYLIST_ID = "PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo"


class YoutubeDownloadTest(TestCase):
    """Unit tests to check if the downloader is working as intended."""

    def test_get_playlist(self: Self) -> None:
        """Check if it can download an entire playlist and if the list is
        correct.

        Args:
            self (Self): The test object to assert if the list is correct.
        """

        video_downloader = VideoDownloader()
        video_downloader.auth_credentials = get_youtube_credentials()
        video_downloader.playlist_id = PLAYLIST_ID
        playlist = video_downloader.get_playlist()

        playlist = Playlist(PLAYLIST_ID, "important videos", playlist)

        with open(TEST_PLAYLIST_DATA, encoding="utf-8") as test_file:
            json_data = json.loads(test_file.read())

        Playlist.from_json(json_data)
        self.assertEqual(json.dumps(playlist.to_dict()), json.dumps(json_data))

    def test_for_object_exceptions(self: Self) -> None:
        """Test exceptions if there are missing keys or values.

        Args:
            self (Self): The test object to test
            exceptions in 'video_downloader'.
        """
        dict_to_video_data = {"Title": "Testing 123"}
        dict_to_playlist_data = {"PlaylistId": "ABC1DEF2GHI3JKL4MNO5"}

        with self.assertRaises(ValueError):
            Video.from_json(dict_to_video_data)

        with self.assertRaises(ValueError):
            Playlist.from_json(dict_to_playlist_data)
