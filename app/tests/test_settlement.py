"""Tests for the settlement service."""

from app.services.settlement_service import settle


def test_settle_runs():
    settle(1)  # TODO: assert the settlement row once the partner stub lands
