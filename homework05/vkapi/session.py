import typing as tp

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Session:
    """
    Сессия.

    :param base_url: Базовый адрес, на который будут выполняться запросы.
    :param timeout: Максимальное время ожидания ответа от сервера.
    :param max_retries: Максимальное число повторных запросов.
    :param backoff_factor: Коэффициент экспоненциального нарастания задержки.
    """

    def __init__(
        self,
        base_url: str,
        timeout: float = 5.0,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
    ) -> None:
        self.base_url=base_url
        self.timeut=timeout
        self.request_session = requests.Session()

    def get(self, url, **kwargs: tp.Any) -> requests.Response:
        full_url = f"{self.base_url}/{url}"
        response=self.request_session.get(url=full_url,params=kwargs,timeout=self.timeut)
        return response

    def post(self, url, data=None, json=None, **kwargs: tp.Any) -> requests.Response:
        full_url = f"{self.base_url}/{url}"
        response=self.request_session.post(url=full_url,data=kwargs,timeout=self.timeut)
        return response
