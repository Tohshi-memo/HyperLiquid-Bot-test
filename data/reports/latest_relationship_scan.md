# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T14:37:30.426424+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `110.8682` n `139` status `ready` deltaP `-33.201` edge `9.7516` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8805` n `32` status `ready` deltaP `-45.1389` edge `4.5914` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8805` n `32` status `ready` deltaP `-45.1389` edge `4.5914` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5974` n `36` status `ready` deltaP `10.0694` edge `0.7706` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.143` n `36` status `ready` deltaP `37.9573` edge `0.3422` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.8191` n `32` status `ready` deltaP `32.6389` edge `0.184` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8191` n `32` status `ready` deltaP `32.6389` edge `0.184` maxDD `0.0`
- `market_context_high->commodity_24h` score `3.1864` n `139` status `ready` deltaP `22.567` edge `0.19` maxDD `-2.3266`
- `risk_on_high->commodity_4h` score `2.9418` n `32` status `ready` deltaP `20.503` edge `0.1267` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9418` n `32` status `ready` deltaP `20.503` edge `0.1267` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.0567` n `36` status `ready` deltaP `13.8889` edge `0.0788` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.0116` n `32` status `ready` deltaP `16.3194` edge `0.2647` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.0116` n `32` status `ready` deltaP `16.3194` edge `0.2647` maxDD `-6.2481`
- `news_risk_high->index_4h` score `1.6519` n `36` status `ready` deltaP `19.4613` edge `0.0211` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6206` n `36` status `ready` deltaP `8.2835` edge `0.1117` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2947` n `32` status `ready` deltaP `13.6602` edge `0.0401` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2947` n `32` status `ready` deltaP `13.6602` edge `0.0401` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2334` n `32` status `ready` deltaP `14.5833` edge `0.024` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2334` n `32` status `ready` deltaP `14.5833` edge `0.024` maxDD `-0.1418`
- `market_context_high->commodity_4h` score `1.2218` n `139` status `ready` deltaP `15.0399` edge `0.0654` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
