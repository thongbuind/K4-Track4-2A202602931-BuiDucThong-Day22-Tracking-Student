"""Kiểm tra chuẩn bị chấm chỉ video luyện bằng dữ liệu giả."""

from pathlib import Path

import pytest

from evaluate_practice import stage


def test_stage_respects_requested_split(tmp_path: Path) -> None:
    lab = tmp_path / "lab"
    practice = lab / "video_1"
    (practice / "gt").mkdir(parents=True)
    (practice / "gt" / "gt.txt").write_text("1,1,0,0,10,10,1,1,1\n")
    (practice / "seqinfo.ini").write_text("[Sequence]\nseqLength=1\n")
    submission = tmp_path / "video_1.txt"
    submission.write_text("1,1,0,0,10,10,1,-1,-1,-1\n")
    root = tmp_path / "cham"
    stage(root, lab, submission, "lan_thu", "LAB", split="test")
    assert (root / "data/gt/mot_challenge/LAB-test/video_1/gt/gt.txt").exists()
    assert (root / "data/trackers/mot_challenge/LAB-test/lan_thu/data/video_1.txt").read_text() == submission.read_text()
    assert not (root / "data/gt/mot_challenge/LAB-train").exists()
    assert not (root / "data/gt/mot_challenge/LAB-test/video_2").exists()


def test_stage_rejects_missing_practice_metadata(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="thiếu gt hoặc seqinfo"):
        stage(tmp_path / "cham", tmp_path / "lab", tmp_path / "video_1.txt", "lan_thu", "LAB")
