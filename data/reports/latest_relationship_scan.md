# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T00:07:20.501711+00:00`
- Price records: `672`
- Market context records: `1990`
- Flow alert records: `7618`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7585`

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

- `market_context_high->crypto_major_4h` score `7.9254` n `229` status `ready` deltaP `28.1613` edge `0.5426` maxDD `-2.2578`
- `market_context_high->crypto_alt_4h` score `7.7532` n `229` status `ready` deltaP `23.8151` edge `0.6018` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `3.5641` n `229` status `ready` deltaP `15.2546` edge `0.3464` maxDD `-7.4207`
- `market_context_high->equity_4h` score `2.3036` n `229` status `ready` deltaP `14.2527` edge `0.2064` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.0905` n `194` status `ready` deltaP `16.3871` edge `0.597` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.8633` n `194` status `ready` deltaP `16.8709` edge `0.2854` maxDD `-12.7414`
- `market_context_high->equity_24h` score `1.2634` n `194` status `ready` deltaP `15.3492` edge `0.4928` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.1606` n `229` status `ready` deltaP `10.3993` edge `0.126` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.9028` n `229` status `ready` deltaP `8.5656` edge `0.1295` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.635` n `194` status `ready` deltaP `20.1296` edge `0.7773` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.4556` n `229` status `ready` deltaP `7.7025` edge `0.0711` maxDD `-3.0921`
- `market_context_high->index_24h` score `0.3615` n `194` status `ready` deltaP `3.7001` edge `0.1283` maxDD `-4.1604`
- `market_context_high->fx_24h` score `0.3017` n `194` status `ready` deltaP `12.4276` edge `0.0239` maxDD `-1.1952`
- `market_context_high->equity_1h` score `-0.1918` n `229` status `ready` deltaP `4.0125` edge `0.0361` maxDD `-2.6402`
- `market_context_high->fx_1h` score `-0.645` n `229` status `ready` deltaP `-2.8757` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7152` n `229` status `ready` deltaP `-0.604` edge `0.0076` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.9534` n `229` status `ready` deltaP `1.6284` edge `0.0005` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.212` n `229` status `ready` deltaP `-9.3727` edge `-0.0042` maxDD `-1.0961`
- `market_context_high->unknown_1h` score `-1.3646` n `229` status `ready` deltaP `1.1421` edge `-0.0263` maxDD `-3.6022`
- `market_context_high->commodity_1h` score `-1.9058` n `229` status `ready` deltaP `1.6905` edge `0.0002` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
