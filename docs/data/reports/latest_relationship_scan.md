# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T05:22:24.645374+00:00`
- Price records: `672`
- Market context records: `6573`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9904`

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

- `market_context_high->unknown_24h` score `6.2126` n `144` status `ready` deltaP `11.032` edge `0.7742` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7604` n `210` status `ready` deltaP `-5.2794` edge `0.272` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4157` n `144` status `ready` deltaP `13.3492` edge `0.2158` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.337` n `210` status `ready` deltaP `1.1577` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.362` n `210` status `ready` deltaP `7.4964` edge `0.0302` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4713` n `210` status `ready` deltaP `6.4899` edge `0.0276` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5537` n `210` status `ready` deltaP `-0.3807` edge `0.0035` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5962` n `210` status `ready` deltaP `-0.5589` edge `-0.0044` maxDD `-2.1314`
- `market_context_high->index_4h` score `-1.0054` n `210` status `ready` deltaP `7.7812` edge `0.0072` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1837` n `210` status `ready` deltaP `1.9319` edge `-0.0005` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2536` n `210` status `ready` deltaP `-3.4274` edge `-0.0009` maxDD `-2.1239`
- `market_context_high->commodity_4h` score `-1.3604` n `210` status `ready` deltaP `-2.0162` edge `-0.0115` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.5115` n `210` status `ready` deltaP `-15.7041` edge `0.2193` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7191` n `210` status `ready` deltaP `7.8825` edge `0.0585` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.7546` n `210` status `ready` deltaP `-0.0811` edge `-0.0032` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.899` n `210` status `ready` deltaP `5.2381` edge `0.0618` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-1.9369` n `144` status `ready` deltaP `6.0917` edge `0.091` maxDD `-5.7746`
- `market_context_high->metal_4h` score `-2.1406` n `210` status `ready` deltaP `-1.3779` edge `0.0208` maxDD `-5.2172`
- `market_context_high->index_24h` score `-3.7197` n `144` status `ready` deltaP `1.4429` edge `0.0025` maxDD `-10.7676`
- `market_context_high->fx_24h` score `-3.8289` n `144` status `ready` deltaP `-4.8143` edge `-0.0053` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
