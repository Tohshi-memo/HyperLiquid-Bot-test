# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T04:37:14.947728+00:00`
- Price records: `672`
- Market context records: `1083`
- Flow alert records: `5024`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.5565` n `158` status `ready` deltaP `35.4236` edge `1.1899` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.8237` n `158` status `ready` deltaP `12.1657` edge `0.5276` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.4689` n `158` status `ready` deltaP `14.7752` edge `0.4069` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.5813` n `158` status `ready` deltaP `-2.5058` edge `0.5652` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.5157` n `158` status `ready` deltaP `14.8961` edge `0.3078` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5735` n `162` status `ready` deltaP `9.263` edge `0.1482` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.3832` n `162` status `ready` deltaP `13.0006` edge `0.1972` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.8963` n `162` status `ready` deltaP `7.7086` edge `0.0916` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6264` n `174` status `ready` deltaP `8.2937` edge `0.0286` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4582` n `174` status `ready` deltaP `2.7978` edge `0.0573` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1183` n `174` status `ready` deltaP `7.0996` edge `0.0391` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0429` n `174` status `ready` deltaP `7.177` edge `0.0013` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.0583` n `174` status `ready` deltaP `7.4816` edge `0.0063` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2819` n `174` status `ready` deltaP `2.908` edge `0.0414` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.333` n `162` status `ready` deltaP `7.5731` edge `0.1722` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6574` n `162` status `ready` deltaP `2.0495` edge `0.0017` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6955` n `174` status `ready` deltaP `-1.2269` edge `-0.0002` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.9762` n `162` status `ready` deltaP `4.2814` edge `-0.0865` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.0159` n `162` status `ready` deltaP `8.6645` edge `-0.1041` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.0959` n `158` status `ready` deltaP `4.9078` edge `-0.022` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
