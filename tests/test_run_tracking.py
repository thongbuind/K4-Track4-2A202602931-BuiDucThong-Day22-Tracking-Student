"""Kiểm tra chạy tracking bằng mô hình giả, không dùng GPU hay dữ liệu lab."""

import argparse
import json

import numpy as np
import pytest
import torch

import run_tracking


def test_run_uses_selected_device_and_records_all_frames(tmp_path, monkeypatch):
    devices = []
    frames = [(i, np.zeros((8, 8, 3), dtype=np.uint8)) for i in range(3)]

    class FakeDetector:
        def __init__(self, weights):
            assert weights == "yolo26n.pt"

        def to(self, device):
            devices.append(device)

    class FakeTracker:
        def update(self, dets, frame):
            return np.array([[1, 2, 5, 7, 4, 0.9, 0]])

    def fake_create_tracker(**kwargs):
        assert kwargs["device"] == torch.device("cpu")
        return FakeTracker()

    monkeypatch.setattr(run_tracking, "YOLO", FakeDetector)
    monkeypatch.setattr(run_tracking, "create_tracker", fake_create_tracker)
    monkeypatch.setattr(run_tracking, "iter_frames", lambda source: iter(frames))
    monkeypatch.setattr(run_tracking, "detect", lambda *a, **k: np.empty((0, 6)))
    args = argparse.Namespace(
        source="thu_muc_gia", seq_name="video_1", tracker="bytetrack",
        conf=0.3, iou=0.5, device="cpu", out=str(tmp_path),
        save_video=False, fps=30, max_frames=0,
    )
    run_tracking.run(args)
    rows = (tmp_path / "video_1.txt").read_text().splitlines()
    assert [int(row.split(",")[0]) for row in rows] == [1, 2, 3]
    assert rows[0] == "1,4,1.00,2.00,4.00,5.00,0.9000,-1,-1,-1"
    meta = json.loads((tmp_path / "video_1_meta.json").read_text())
    assert meta["frames_processed"] == 3
    assert meta["max_frames"] == 0
    assert meta["imgsz"] == 640
    assert devices == ["cpu"]


def test_unreadable_frame_is_not_silently_skipped(tmp_path, monkeypatch):
    class FakeDetector:
        def __init__(self, weights):
            pass

        def to(self, device):
            pass

    monkeypatch.setattr(run_tracking, "YOLO", FakeDetector)
    monkeypatch.setattr(run_tracking, "create_tracker", lambda **kwargs: object())
    monkeypatch.setattr(run_tracking, "iter_frames", lambda source: iter([(0, None)]))
    args = argparse.Namespace(
        source="thu_muc_gia", seq_name="video_1", tracker="bytetrack",
        conf=0.3, iou=0.5, device="cpu", out=str(tmp_path),
        save_video=False, fps=30, max_frames=0,
    )
    with pytest.raises(ValueError, match="Không đọc được frame 1"):
        run_tracking.run(args)
