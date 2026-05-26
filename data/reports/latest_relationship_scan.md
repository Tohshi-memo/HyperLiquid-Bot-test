# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T09:37:17.848675+00:00`
- Price records: `672`
- Market context records: `1933`
- Flow alert records: `7464`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7540`

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

- `market_context_high->crypto_alt_4h` score `7.1342` n `212` status `ready` deltaP `22.6473` edge `0.558` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.5429` n `212` status `ready` deltaP `26.6165` edge `0.4924` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.2567` n `212` status `ready` deltaP `16.1671` edge `0.366` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0481` n `212` status `ready` deltaP `13.4434` edge `0.1905` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.7321` n `196` status `ready` deltaP `14.5125` edge `0.4963` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.555` n `224` status `ready` deltaP `7.4342` edge `0.0953` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4632` n `224` status `ready` deltaP `7.2712` edge `0.1015` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3162` n `196` status `ready` deltaP `12.2626` edge `0.1872` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1531` n `196` status `ready` deltaP `4.0497` edge `0.1086` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.0913` n `212` status `ready` deltaP `7.7111` edge `0.0651` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2063` n `224` status `ready` deltaP `4.5579` edge `0.0318` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2501` n `196` status `ready` deltaP `10.1793` edge `0.0162` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6287` n `224` status `ready` deltaP `-2.6812` edge `0.0005` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6881` n `224` status `ready` deltaP `-0.0401` edge `0.0061` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7448` n `224` status `ready` deltaP `3.7185` edge `0.0133` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.9343` n `212` status `ready` deltaP `-4.4639` edge `-0.0012` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.0993` n `196` status `ready` deltaP `7.8054` edge `0.3462` maxDD `-33.1875`
- `market_context_high->metal_4h` score `-1.2501` n `212` status `ready` deltaP `8.2662` edge `0.1099` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.4083` n `224` status `ready` deltaP `0.8742` edge `-0.028` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.9346` n `224` status `ready` deltaP `1.7804` edge `-0.0041` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
