# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T00:22:27.493541+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_4h` score `35.4969` n `88` status `ready` deltaP `7.3725` edge `2.9537` maxDD `-0.9153`
- `market_context_high->equity_24h` score `19.3054` n `61` status `ready` deltaP `28.0961` edge `2.5282` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.2969` n `61` status `ready` deltaP `23.1355` edge `0.3147` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `1.5155` n `61` status `ready` deltaP `12.0635` edge `0.6233` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.3103` n `61` status `ready` deltaP `12.3391` edge `-0.0011` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3748` n `88` status `ready` deltaP `3.6473` edge `0.0121` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5576` n `88` status `ready` deltaP `-0.3062` edge `-0.0012` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8374` n `88` status `ready` deltaP `0.194` edge `-0.0109` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8711` n `88` status `ready` deltaP `-2.2311` edge `0.0138` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.0773` n `88` status `ready` deltaP `-8.8527` edge `0.004` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1475` n `88` status `ready` deltaP `-2.2727` edge `0.0064` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3522` n `88` status `ready` deltaP `-14.8067` edge `-0.0062` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7679` n `88` status `ready` deltaP `-8.4036` edge `0.014` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.935` n `88` status `ready` deltaP `0.6328` edge `-0.0544` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1541` n `88` status `ready` deltaP `-7.2201` edge `-0.0099` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.3937` n `61` status `ready` deltaP `-14.5694` edge `-0.051` maxDD `-3.3667`
- `market_context_high->commodity_24h` score `-2.4424` n `61` status `ready` deltaP `-16.3395` edge `0.0412` maxDD `-9.965`
- `market_context_high->crypto_major_1h` score `-3.2383` n `88` status `ready` deltaP `-5.709` edge `-0.1148` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.3887` n `88` status `ready` deltaP `-2.439` edge `-0.2183` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1014` n `88` status `ready` deltaP `2.245` edge `-0.2616` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
