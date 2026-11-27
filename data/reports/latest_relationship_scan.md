# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T10:52:28.669035+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3243.9469` n `31` status `ready` deltaP `1.6322` edge `270.3356` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3192.3334` n `31` status `ready` deltaP `3.7864` edge `266.0082` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.4653` n `31` status `ready` deltaP `28.6458` edge `1.3478` maxDD `0.0`
- `news_risk_high->equity_24h` score `16.4616` n `31` status `ready` deltaP `28.125` edge `1.1843` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.6726` n `31` status `ready` deltaP `27.7778` edge `0.9542` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.5589` n `31` status `ready` deltaP `20.8153` edge `0.6615` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.4741` n `31` status `ready` deltaP `30.6698` edge `0.3831` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.4098` n `31` status `ready` deltaP `13.4244` edge `0.7458` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `4.7592` n `31` status `ready` deltaP `16.0619` edge `0.317` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6346` n `31` status `ready` deltaP `38.5865` edge `0.1418` maxDD `-0.0262`
- `news_risk_high->index_24h` score `2.9918` n `31` status `ready` deltaP `29.6875` edge `0.0514` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5884` n `31` status `ready` deltaP `30.2125` edge `0.0403` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5657` n `31` status `ready` deltaP `16.0952` edge `0.1252` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3835` n `31` status `ready` deltaP `28.8488` edge `0.0148` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0059` n `31` status `ready` deltaP `6.1184` edge `0.2625` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8278` n `31` status `ready` deltaP `9.5615` edge `0.2063` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1636` n `31` status `ready` deltaP `25.0917` edge `0.0098` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3428` n `31` status `ready` deltaP `11.4427` edge `0.0234` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0254` n `31` status `ready` deltaP `6.845` edge `-0.0026` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.612` n `31` status `ready` deltaP `-4.4572` edge `0.0049` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
