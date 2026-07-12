# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T20:22:23.756472+00:00`
- Price records: `672`
- Market context records: `6536`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `news_risk_high->crypto_alt_24h` score `13.7819` n `32` status `ready` deltaP `37.2509` edge `0.9149` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6222` n `32` status `ready` deltaP `54.5927` edge `0.1879` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3283` n `144` status `ready` deltaP `11.8934` edge `0.7781` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `5.0293` n `32` status `ready` deltaP `21.9508` edge `0.5764` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7121` n `38` status `ready` deltaP `39.3213` edge `0.0518` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.0069` n `195` status `ready` deltaP `-6.5185` edge `0.3008` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `1.9243` n `32` status `ready` deltaP `21.81` edge `0.0355` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8035` n `38` status `ready` deltaP `22.6127` edge `0.0176` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.5052` n `144` status `ready` deltaP `13.8239` edge `0.2201` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6953` n `183` status `ready` deltaP `14.5467` edge `0.0286` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5987` n `38` status `ready` deltaP `5.4995` edge `0.0938` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3643` n `183` status `ready` deltaP `10.25` edge `0.1174` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.1038` n `38` status `ready` deltaP `1.8831` edge `0.0517` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.1825` n `32` status `ready` deltaP `8.5897` edge `0.0065` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.336` n `183` status `ready` deltaP `10.0201` edge `0.06` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.3702` n `183` status `ready` deltaP `13.198` edge `0.0936` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.4169` n `195` status `ready` deltaP `-0.1674` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4502` n `195` status `ready` deltaP `1.8141` edge `-0.0015` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5525` n `195` status `ready` deltaP `6.1746` edge `0.0193` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5588` n `195` status `ready` deltaP `6.0663` edge `0.0145` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
