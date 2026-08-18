# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T11:52:29.653353+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2479` n `84` status `ready` deltaP `7.8918` edge `0.2555` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.507` n `84` status `ready` deltaP `16.6254` edge `0.2657` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0161` n `96` status `ready` deltaP `9.163` edge `0.054` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.8015` n `96` status `ready` deltaP `15.0406` edge `0.0241` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.7172` n `96` status `ready` deltaP `9.3242` edge `0.0997` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.6467` n `96` status `ready` deltaP `12.7682` edge `0.0075` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5424` n `96` status `ready` deltaP `9.3563` edge `0.0055` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.5346` n `96` status `ready` deltaP `10.6707` edge `0.1004` maxDD `-5.4926`
- `market_context_high->equity_4h` score `0.0079` n `96` status `ready` deltaP `2.312` edge `0.0757` maxDD `-2.5696`
- `market_context_high->unknown_24h` score `-0.0115` n `84` status `ready` deltaP `14.3105` edge `-0.0786` maxDD `-0.0875`
- `market_context_high->metal_1h` score `-0.0417` n `96` status `ready` deltaP `4.0232` edge `0.0084` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2242` n `96` status `ready` deltaP `3.2266` edge `0.0` maxDD `-0.3539`
- `market_context_high->crypto_alt_1h` score `-0.3644` n `96` status `ready` deltaP `2.2268` edge `0.0186` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.3749` n `96` status `ready` deltaP `4.0905` edge `0.0097` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4475` n `96` status `ready` deltaP `-3.4182` edge `0.0013` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4702` n `96` status `ready` deltaP `1.4845` edge `0.0143` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5665` n `96` status `ready` deltaP `1.0924` edge `0.011` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8565` n `96` status `ready` deltaP `-7.142` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9314` n `84` status `ready` deltaP `-6.462` edge `0.0201` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.3654` n `84` status `ready` deltaP `-14.3064` edge `-0.176` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
