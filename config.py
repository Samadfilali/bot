#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    #APP_ID = os.environ.get("MicrosoftAppId", "668362ba-3d44-45d7-8b9b-d57cf2508863")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "@1f4gtyu56dfg58s")
    LUIS_APP_ID = os.environ.get("LuisAppId", "a1f4103a-c1b2-40e6-8869-d59442f12961")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "2b6287bd2d8b42edac4abc7204db22d5")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "81b6bd8a-b535-4846-b8ef-d2423aa43358"
    )
    
    #insightfly  5a09aee4-1814-4536-961f-aaee91ac016