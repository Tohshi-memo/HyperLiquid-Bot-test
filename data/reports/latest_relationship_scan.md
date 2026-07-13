# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T00:07:29.321911+00:00`
- Price records: `672`
- Market context records: `6553`
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

- `market_context_high->unknown_24h` score `6.4075` n `144` status `ready` deltaP `11.8934` edge `0.7847` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7747` n `206` status `ready` deltaP `-5.7162` edge `0.2761` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3315` n `144` status `ready` deltaP `12.9574` edge `0.2114` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.3748` n `196` status `ready` deltaP `11.548` edge `0.0257` maxDD `-0.7164`
- `market_context_high->crypto_alt_4h` score `-0.1339` n `196` status `ready` deltaP `8.7264` edge `0.1019` maxDD `-8.0324`
- `market_context_high->equity_4h` score `-0.3809` n `196` status `ready` deltaP `9.893` edge `0.0551` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4002` n `206` status `ready` deltaP `0.1221` edge `-0.0014` maxDD `-0.7249`
- `market_context_high->crypto_major_4h` score `-0.5294` n `196` status `ready` deltaP `11.1716` edge `0.0867` maxDD `-12.6576`
- `market_context_high->index_1h` score `-0.5774` n `206` status `ready` deltaP `-0.8212` edge `0.0034` maxDD `-0.7564`
- `market_context_high->crypto_major_1h` score `-0.5818` n `206` status `ready` deltaP `6.27` edge `0.0102` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.6104` n `206` status `ready` deltaP `5.9749` edge `0.0132` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.8975` n `206` status `ready` deltaP `-0.2674` edge `-0.0047` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-1.0136` n `196` status `ready` deltaP `-17.1603` edge `0.2705` maxDD `-10.5788`
- `market_context_high->equity_1h` score `-1.1878` n `206` status `ready` deltaP `1.8647` edge `-0.0004` maxDD `-4.2147`
- `market_context_high->metal_4h` score `-1.2207` n `196` status `ready` deltaP `0.6782` edge `0.0348` maxDD `-2.6662`
- `market_context_high->metal_1h` score `-1.2906` n `206` status `ready` deltaP `-3.7251` edge `-0.002` maxDD `-2.1239`
- `market_context_high->metal_24h` score `-1.9805` n `144` status `ready` deltaP `5.966` edge `0.0882` maxDD `-5.7746`
- `market_context_high->commodity_4h` score `-2.0359` n `196` status `ready` deltaP `-1.3471` edge `-0.0112` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-3.0384` n `196` status `ready` deltaP `-3.4781` edge `-0.0088` maxDD `-3.3635`
- `market_context_high->fx_24h` score `-3.8795` n `144` status `ready` deltaP `-5.3076` edge `-0.0085` maxDD `-9.2795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
