# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T08:22:34.094252+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10712`

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

- `market_context_high->commodity_4h` score `1.1336` n `169` status `ready` deltaP `13.7589` edge `0.0742` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.8421` n `136` status `ready` deltaP `18.9367` edge `0.0247` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.8087` n `169` status `ready` deltaP `10.7687` edge `0.0299` maxDD `-0.7439`
- `market_context_high->fx_4h` score `0.0943` n `169` status `ready` deltaP `8.7055` edge `0.0098` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1249` n `169` status `ready` deltaP `4.2669` edge `0.0007` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.6111` n `136` status `ready` deltaP `1.6528` edge `0.0912` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.8158` n `169` status `ready` deltaP `-2.7265` edge `-0.0021` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.8381` n `169` status `ready` deltaP `-5.1075` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.08` n `169` status `ready` deltaP `-0.5773` edge `-0.0079` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.2486` n `136` status `ready` deltaP `-2.7742` edge `0.0426` maxDD `-2.9193`
- `market_context_high->equity_1h` score `-1.2508` n `169` status `ready` deltaP `-2.0559` edge `-0.0035` maxDD `-4.6286`
- `market_context_high->equity_24h` score `-1.3246` n `136` status `ready` deltaP `-0.9099` edge `0.21` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5661` n `169` status `ready` deltaP `-8.9785` edge `-0.0388` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9168` n `169` status `ready` deltaP `-5.7524` edge `-0.031` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.0652` n `169` status `ready` deltaP `-10.2483` edge `-0.1121` maxDD `-8.0039`
- `market_context_high->crypto_major_1h` score `-3.6402` n `169` status `ready` deltaP `-10.5401` edge `-0.0597` maxDD `-10.5372`
- `market_context_high->crypto_alt_4h` score `-3.9101` n `169` status `ready` deltaP `-11.6011` edge `-0.1482` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.4471` n `136` status `ready` deltaP `-11.9075` edge `-0.1469` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.8059` n `136` status `ready` deltaP `-2.8902` edge `-0.1318` maxDD `-14.2873`
- `market_context_high->commodity_24h` score `-8.5674` n `136` status `ready` deltaP `-5.3752` edge `-0.191` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
