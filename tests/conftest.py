import os
import tempfile
import shutil
import pytest
from pathlib import Path


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_dataset_dir(temp_dir):
    """Create a sample dataset directory structure for testing."""
    dataset_path = os.path.join(temp_dir, "dataset")
    os.makedirs(dataset_path)
    
    # Create train, test, validation subdirs
    for subdir in ["train", "test", "validation"]:
        subdir_path = os.path.join(dataset_path, subdir)
        os.makedirs(subdir_path)
        # Create a dummy file in each subdir
        dummy_file = os.path.join(subdir_path, "sample.txt")
        with open(dummy_file, "w") as f:
            f.write(f"Sample data for {subdir}")
    
    return dataset_path


@pytest.fixture
def sample_output_dir(temp_dir):
    """Create a sample output directory for testing."""
    output_path = os.path.join(temp_dir, "output")
    return output_path


@pytest.fixture
def mock_args():
    """Mock command line arguments."""
    class MockArgs:
        def __init__(self):
            self.command = "create"
            self.output_folder = None
            self.dataset_folder = None
    
    return MockArgs()


@pytest.fixture
def sample_files():
    """List of expected files to be created."""
    return ["main.py", "model.py", "utils.py", "train.py", "test.py", "test_notebook.ipynb"]


@pytest.fixture
def sample_folders():
    """List of expected folders to be created."""
    return ["Data", "Data/train", "Data/test", "Data/validation"]


@pytest.fixture
def cleanup_test_files():
    """Cleanup any test files created during testing."""
    created_files = []
    created_dirs = []
    
    def track_file(file_path):
        created_files.append(file_path)
        
    def track_dir(dir_path):
        created_dirs.append(dir_path)
    
    yield track_file, track_dir
    
    # Cleanup
    for file_path in created_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            
    for dir_path in reversed(created_dirs):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)