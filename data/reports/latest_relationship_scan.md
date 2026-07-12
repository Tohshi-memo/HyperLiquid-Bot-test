# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T20:37:29.102524+00:00`
- Price records: `672`
- Market context records: `6537`
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

- `news_risk_high->crypto_alt_24h` score `13.6488` n `31` status `ready` deltaP `37.2226` edge `0.904` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6169` n `31` status `ready` deltaP `54.766` edge `0.1863` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3415` n `144` status `ready` deltaP `11.8934` edge `0.7792` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8199` n `31` status `ready` deltaP `21.0152` edge `0.5558` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7148` n `37` status `ready` deltaP `39.1892` edge `0.0529` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.3015` n `31` status `ready` deltaP `24.3585` edge `0.0438` maxDD `-0.1518`
- `market_context_high->unknown_1h` score `1.962` n `196` status `ready` deltaP `-6.599` edge `0.2976` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.9575` n `37` status `ready` deltaP `24.4619` edge `0.0181` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.4758` n `144` status `ready` deltaP `13.6506` edge `0.2188` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.698` n `37` status `ready` deltaP `7.0643` edge `0.0961` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.6757` n `184` status `ready` deltaP `14.316` edge `0.0285` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.3504` n `184` status `ready` deltaP `10.061` edge `0.1175` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0201` n `37` status `ready` deltaP `0.7526` edge `0.0485` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2679` n `31` status `ready` deltaP `7.3517` edge `0.0038` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3215` n `184` status `ready` deltaP `10.2399` edge `0.0604` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.3776` n `184` status `ready` deltaP `12.9971` edge `0.094` maxDD `-12.6576`
- `market_context_high->fx_1h` score `-0.4297` n `196` status `ready` deltaP `-0.4002` edge `-0.0017` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4427` n `196` status `ready` deltaP `1.8972` edge `-0.0011` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5598` n `196` status `ready` deltaP `6.0339` edge `0.0193` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5751` n `196` status `ready` deltaP `5.7681` edge `0.0144` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
