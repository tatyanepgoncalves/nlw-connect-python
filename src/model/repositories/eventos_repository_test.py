import pytest
from .eventos_repository import EventosRepository

@pytest.mark.skip("Insert in DB")
def test_insert_event():
  event_name = "eventosTeste2"
  event_repo = EventosRepository()

  event_repo.insert(event_name)

@pytest.mark.skip("Select in DB")
def test_select_event():
  event_name = "eventosTeste2"
  event_repo = EventosRepository()

  event = event_repo.select_event(event_name)