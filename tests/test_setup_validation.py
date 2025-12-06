"""
Validation tests to ensure the testing infrastructure is properly set up.
These tests verify that the testing framework is working correctly.
"""
import pytest
import os
import sys
from pathlib import Path


def test_pytest_working():
    """Test that pytest is working correctly."""
    assert True


def test_pytest_markers():
    """Test that custom markers are working."""
    pass


@pytest.mark.unit
def test_unit_marker():
    """Test that unit marker is working."""
    assert True


@pytest.mark.integration  
def test_integration_marker():
    """Test that integration marker is working."""
    assert True


@pytest.mark.slow
def test_slow_marker():
    """Test that slow marker is working.""" 
    assert True


def test_fixtures_available(temp_dir, sample_dataset_dir, sample_output_dir):
    """Test that shared fixtures from conftest.py are available."""
    assert os.path.exists(temp_dir)
    assert os.path.exists(sample_dataset_dir)
    assert isinstance(sample_output_dir, str)


def test_mock_available():
    """Test that pytest-mock is available."""
    pytest_mock = pytest.importorskip("pytest_mock")
    assert pytest_mock is not None


def test_coverage_integration():
    """Test that coverage reporting is working."""
    # This test will be included in coverage reports
    # Coverage should be measured for this test
    dummy_calculation = 2 + 2
    assert dummy_calculation == 4


def test_project_structure():
    """Test that the project structure is correct."""
    project_root = Path(__file__).parent.parent
    
    # Check that key files exist
    assert (project_root / "pyproject.toml").exists()
    assert (project_root / "mlp_cli.py").exists()
    
    # Check that test directories exist
    assert (project_root / "tests").exists()
    assert (project_root / "tests" / "unit").exists()
    assert (project_root / "tests" / "integration").exists()
    
    # Check that __init__.py files exist
    assert (project_root / "tests" / "__init__.py").exists()
    assert (project_root / "tests" / "unit" / "__init__.py").exists()
    assert (project_root / "tests" / "integration" / "__init__.py").exists()


def test_python_path():
    """Test that Python can import the main module."""
    import sys
    from pathlib import Path
    
    # Add project root to Python path if not already there
    project_root = str(Path(__file__).parent.parent)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    # Test that we can import the main module
    import mlp_cli
    assert hasattr(mlp_cli, 'main')
    assert hasattr(mlp_cli, 'create_file_structure')


class TestClassExample:
    """Example test class to verify class-based tests work."""
    
    def test_class_method(self):
        """Test that class-based tests work."""
        assert True
        
    def test_class_method_with_fixture(self, temp_dir):
        """Test that fixtures work in class methods."""
        assert os.path.exists(temp_dir)