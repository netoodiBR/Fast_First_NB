from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_first.app import app


def test_read_root_deve_retornar_ok_e_batata_frita_com_cheddar_e_bacon_e_uma_delicia():
    client = TestClient(
        app
    )  # arrange/organização. Aqui, ajeitamos para começar o teste

    response = client.get("/")  # fase act, a que executa

    assert (
        response.status_code == HTTPStatus.OK
    )  # ASSERT/VALIDAÇÃO. aq, diz: o statuscode que retorna é ok? (200)
    assert response.json() == {
        "message": "Batata frita com cheddar e bacon é uma delicia"
    }
