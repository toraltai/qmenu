from .repository import TortoiseRepository


class CompanyService:
    def __init__(self, repo: TortoiseRepository):
        self.repo = repo

    async def test(self):
        return await self.repo.test()