"""Dutique Core Engine"""
###############################################################################
# Imports

import asyncio
import logging

from core.base_module import BaseModule
from core.log import LogFormatter


###############################################################################
# Engine
class Engine:
    """Dutique Engine"""
    def __init__(self):
        self.modules: list[BaseModule] = []
        self.module_names = set()
        self.state = {}
        self.loglevel = logging.DEBUG

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.loglevel)

        self.logging_stream = logging.StreamHandler()
        self.logging_stream.setLevel(self.loglevel)
        self.logging_stream.setFormatter(LogFormatter())


    def register_module(self, module: BaseModule):
        """Register a module"""
        name = module.name
        hard = module.depends_on

        missing_hard = [dep for dep in hard if dep not in self.module_names]

        if missing_hard:
            self.logger.error("Skipping %s: missing required dependencies %s", name, missing_hard)
            return

        self.modules.append(module)
        self.module_names.add(name)
        logger = logging.getLogger("modules."+name)
        logger.setLevel(self.loglevel)
        logger.addHandler(self.logging_stream)

        self.logger.info("Succesfully Registered: %s", name)

    async def _run_all(self):
        self.state["available_modules"] = self.module_names.copy()
        for mod in self.modules:
            mod.set_available_modules(self.module_names)
            mod.init(self.state)

        for mod in self.modules:
            asyncio.create_task(self._module_loop(mod))

        await asyncio.Event().wait()

    async def _module_loop(self, module: BaseModule):
        """Interne Endlosschleife pro Modul"""
        while True:
            try:
                await module.update(self.state)
            except Exception as e:
                self.logger.error("error in %s", module.name, exc_info=e)
            await asyncio.sleep(getattr(module, "tick_interval", 1))

    def run(self):
        """Public API: single entry point"""
        asyncio.run(self._run_all())
