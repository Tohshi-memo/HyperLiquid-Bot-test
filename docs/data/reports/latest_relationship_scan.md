# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T08:52:25.385265+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2964`

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

- `news_risk_high->unknown_1h` score `3224.8921` n `31` status `ready` deltaP `1.6322` edge `268.7477` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.751` n `31` status `ready` deltaP `3.7864` edge `265.293` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.1028` n `31` status `ready` deltaP `30.0347` edge `1.475` maxDD `0.0`
- `news_risk_high->equity_24h` score `18.0223` n `31` status `ready` deltaP `29.5139` edge `1.3051` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.0449` n `31` status `ready` deltaP `29.1667` edge `1.0593` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.8094` n `31` status `ready` deltaP `21.5775` edge `0.6773` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.6041` n `31` status `ready` deltaP `30.9747` edge `0.3919` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.5909` n `31` status `ready` deltaP `14.4915` edge `0.7619` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.1451` n `31` status `ready` deltaP `17.4508` edge `0.3399` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6322` n `31` status `ready` deltaP `38.5865` edge `0.1416` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.2445` n `31` status `ready` deltaP `31.0764` edge `0.0632` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5944` n `31` status `ready` deltaP `30.2125` edge `0.0408` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5897` n `31` status `ready` deltaP `16.2449` edge `0.1262` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3978` n `31` status `ready` deltaP `28.9985` edge `0.015` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0223` n `31` status `ready` deltaP `6.2681` edge `0.2636` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8442` n `31` status `ready` deltaP `9.5615` edge `0.2084` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1403` n `31` status `ready` deltaP `24.7923` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3987` n `31` status `ready` deltaP `12.0525` edge `0.0265` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0957` n `31` status `ready` deltaP `5.6255` edge `-0.01` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6983` n `31` status `ready` deltaP `-5.2057` edge `0.0027` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
