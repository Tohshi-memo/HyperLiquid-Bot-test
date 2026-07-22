# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T11:22:26.129356+00:00`
- Price records: `672`
- Market context records: `7559`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `market_context_high->index_1h` score `-0.1413` n `178` status `ready` deltaP `5.1389` edge `0.0072` maxDD `-1.7657`
- `market_context_high->commodity_4h` score `-0.1484` n `178` status `ready` deltaP `6.6058` edge `0.0196` maxDD `-2.4139`
- `market_context_high->fx_1h` score `-0.2753` n `178` status `ready` deltaP `3.8989` edge `0.001` maxDD `-0.6615`
- `market_context_high->unknown_4h` score `-0.31` n `178` status `ready` deltaP `12.9351` edge `0.1099` maxDD `-6.2031`
- `market_context_high->unknown_1h` score `-0.3328` n `178` status `ready` deltaP `3.4078` edge `0.0119` maxDD `-1.3217`
- `market_context_high->commodity_1h` score `-0.4719` n `178` status `ready` deltaP `2.6538` edge `0.0002` maxDD `-1.5775`
- `market_context_high->fx_24h` score `-0.5938` n `155` status `ready` deltaP `11.6466` edge `0.0169` maxDD `-3.8554`
- `market_context_high->crypto_alt_1h` score `-0.6118` n `178` status `ready` deltaP `0.7115` edge `0.0207` maxDD `-5.9775`
- `market_context_high->commodity_24h` score `-0.6567` n `155` status `ready` deltaP `9.8888` edge `0.0377` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `-0.9838` n `178` status `ready` deltaP `5.0192` edge `0.0256` maxDD `-7.6171`
- `market_context_high->metal_1h` score `-1.0363` n `178` status `ready` deltaP `1.4583` edge `0.0143` maxDD `-1.4971`
- `market_context_high->index_4h` score `-1.0429` n `178` status `ready` deltaP `8.6761` edge `0.0184` maxDD `-6.4627`
- `market_context_high->fx_4h` score `-1.194` n `178` status `ready` deltaP `1.4689` edge `0.0056` maxDD `-2.1439`
- `market_context_high->metal_4h` score `-1.4095` n `178` status `ready` deltaP `2.487` edge `0.0509` maxDD `-4.8549`
- `market_context_high->equity_1h` score `-1.4996` n `178` status `ready` deltaP `3.6036` edge `0.0248` maxDD `-14.6193`
- `market_context_high->crypto_alt_4h` score `-1.638` n `178` status `ready` deltaP `2.0862` edge `0.0504` maxDD `-15.2776`
- `market_context_high->unknown_24h` score `-1.7995` n `156` status `ready` deltaP `3.0582` edge `0.0238` maxDD `-9.9917`
- `market_context_high->crypto_major_4h` score `-2.2007` n `178` status `ready` deltaP `5.8184` edge `0.0685` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-4.5687` n `178` status `ready` deltaP `0.8607` edge `0.1127` maxDD `-43.3339`
- `market_context_high->metal_24h` score `-4.6779` n `156` status `ready` deltaP `-9.8691` edge `0.0305` maxDD `-18.4879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
