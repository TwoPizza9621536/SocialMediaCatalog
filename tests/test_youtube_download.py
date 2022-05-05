# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Unit Test for downloading video metadata."""

from pytest import raises
import json

from social_media_catalog.youtube import get_youtube_credentials
from social_media_catalog.youtube import VideoDownloader
from social_media_catalog.youtube import Playlist
from social_media_catalog.youtube import Video

TEST_PLAYLIST_DATA = "playlist.json"
PLAYLIST_ID = "PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo"


class TestYoutubeDownload:
    """Unit tests to check if the downloader is working as intended."""

    def test_get_playlist(self) -> None:
        """Check if it can download an entire playlist and if the list is
        correct.

        Args:
            self: The test object to assert if the list is correct.
        """

        vd = VideoDownloader()
        vd.auth_credentials = get_youtube_credentials()
        vd.playlist_id = PLAYLIST_ID
        playlist = Playlist(PLAYLIST_ID, "important videos", vd.get_playlist())

        with open(TEST_PLAYLIST_DATA, encoding="utf-8") as test_file:
            json_data = json.loads(test_file.read())

        Playlist.from_json(json_data)
        assert json.dumps(playlist.to_dict()), json.dumps(json_data)

    def test_object_exceptions(self) -> None:
        """Test exceptions if there are missing keys or values.

        Args:
            self: The test object to test exceptions in 'video_downloader'.
        """
        dict_to_video_data = {"title": "Testing 123"}
        dict_to_playlist_data = {"playlistId": "ABC1DEF2GHI3JKL4MNO5"}

        with raises(ValueError):
            Video.from_json(dict_to_video_data)

        with raises(ValueError):
            Playlist.from_json(dict_to_playlist_data)
