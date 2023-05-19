"""Unit test for uptime."""

import time
import unittest

from unittest import mock

import uptime


class TestUptime(unittest.TestCase):
    @mock.patch.object(time, "perf_counter")
    def test_uptime(self, mock_perf_counter):
        mock_perf_counter.return_value = 1000.0

        begin_time = time.perf_counter()

        self.assertEqual("16 minutes, 40 seconds",
                         uptime.uptime(begin_time - 1000))

        self.assertEqual("2 hours, 46 minutes, 40 seconds",
                         uptime.uptime(begin_time - 10000))

        self.assertEqual("342238375 months, 3 weeks, 5 days, 14 hours, 7 minutes, 30 seconds",
                         uptime.uptime(begin_time - 900000000000000))
