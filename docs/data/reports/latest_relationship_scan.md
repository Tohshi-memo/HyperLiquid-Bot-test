# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T05:37:28.228547+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11538`

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

- `market_context_high->unknown_4h` score `37.9549` n `88` status `ready` deltaP `7.6774` edge `3.1565` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.2079` n `82` status `ready` deltaP `31.9673` edge `2.878` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.44` n `82` status `ready` deltaP `25.5739` edge `0.3291` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `3.3008` n `82` status `ready` deltaP `20.4464` edge `0.7963` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1695` n `82` status `ready` deltaP `15.8368` edge `-0.0644` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.4707` n `88` status `ready` deltaP `2.7491` edge `0.0101` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.486` n `88` status `ready` deltaP `0.7417` edge `0.001` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6221` n `88` status `ready` deltaP `0.8176` edge `0.0254` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8272` n `88` status `ready` deltaP `0.3464` edge `-0.0106` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0937` n `88` status `ready` deltaP `-9.1521` edge `0.0039` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2486` n `88` status `ready` deltaP `-2.8825` edge `-0.0025` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3701` n `88` status `ready` deltaP `-15.1061` edge `-0.0065` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8216` n `88` status `ready` deltaP `-9.3018` edge `0.0131` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9763` n `88` status `ready` deltaP `0.3334` edge `-0.0577` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1959` n `88` status `ready` deltaP `-7.8298` edge `-0.0112` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.8927` n `82` status `ready` deltaP `-7.1987` edge `-0.0331` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.2095` n `88` status `ready` deltaP `-5.4096` edge `-0.1131` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-5.432` n `82` status `ready` deltaP `-22.4099` edge `-0.0573` maxDD `-22.5102`
- `market_context_high->equity_4h` score `-7.5379` n `88` status `ready` deltaP `-2.7439` edge `-0.2287` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.203` n `88` status `ready` deltaP `1.6353` edge `-0.266` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
