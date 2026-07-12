# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T08:56:23.791957+00:00`
- Price records: `672`
- Market context records: `6482`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.5706` n `32` status `ready` deltaP `33.8542` edge `0.8366` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.6793` n `158` status `ready` deltaP `16.2205` edge `0.7785` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4493` n `32` status `ready` deltaP `53.6458` edge `0.1798` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3021` n `32` status `ready` deltaP `16.6667` edge `0.5184` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9654` n `38` status `ready` deltaP `42.2176` edge `0.0536` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.0627` n `32` status `ready` deltaP `28.6458` edge `0.0848` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.1352` n `179` status `ready` deltaP `-4.8397` edge `0.3003` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.8311` n `38` status `ready` deltaP `22.9121` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5528` n `38` status `ready` deltaP `4.751` edge `0.0929` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4477` n `172` status `ready` deltaP `11.4968` edge `0.0283` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.261` n `158` status `ready` deltaP `6.2961` edge `0.1666` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.25` n `172` status `ready` deltaP `8.5508` edge `0.1192` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.205` n `172` status `ready` deltaP `-15.6977` edge `0.3623` maxDD `-10.5788`
- `market_context_high->metal_4h` score `0.1847` n `172` status `ready` deltaP `12.0462` edge `0.0439` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0423` n `38` status `ready` deltaP `1.1346` edge `0.0488` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.4571` n `32` status `ready` deltaP `4.6875` edge `-0.0027` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4713` n `172` status `ready` deltaP `8.1395` edge `0.0552` maxDD `-8.2573`
- `market_context_high->metal_1h` score `-0.5396` n `179` status `ready` deltaP `1.1081` edge `0.0012` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5848` n `179` status `ready` deltaP `-0.5495` edge `-0.003` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5941` n `179` status `ready` deltaP `-1.2469` edge `0.0041` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
