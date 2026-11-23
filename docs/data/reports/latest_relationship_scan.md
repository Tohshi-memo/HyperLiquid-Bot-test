# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T05:52:22.891411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5298`

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

- `market_context_high->unknown_1h` score `16015.2497` n `84` status `ready` deltaP `1.6966` edge `1334.609` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10756.9057` n `82` status `ready` deltaP `3.5061` edge `896.3993` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1336.8802` n `31` status `ready` deltaP `3.5783` edge `111.4004` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1171.8505` n `31` status `ready` deltaP `3.9388` edge `97.6336` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.2869` n `31` status `ready` deltaP `36.6149` edge `0.7447` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.7235` n `31` status `ready` deltaP `24.4738` edge `0.8175` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.4564` n `31` status `ready` deltaP `13.1196` edge `0.882` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.8023` n `31` status `ready` deltaP `18.9395` edge `0.2093` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.448` n `31` status `ready` deltaP `36.1576` edge `0.0723` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6519` n `31` status `ready` deltaP `31.0943` edge `0.0222` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3909` n `31` status `ready` deltaP `9.2621` edge `0.2909` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0035` n `31` status `ready` deltaP `7.9148` edge `0.2398` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5142` n `31` status `ready` deltaP `28.8342` edge `0.0298` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4773` n `31` status `ready` deltaP `20.2842` edge `0.1099` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.839` n `31` status `ready` deltaP `18.1255` edge `0.0265` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.0486` n `82` status `ready` deltaP `10.0609` edge `0.0124` maxDD `-0.5264`
- `news_risk_high->commodity_1h` score `-0.1016` n `31` status `ready` deltaP `0.932` edge `0.0115` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1367` n `84` status `ready` deltaP `3.4502` edge `0.0113` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1788` n `84` status `ready` deltaP `2.8301` edge `0.0038` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.0997` n `84` status `ready` deltaP `-4.598` edge `-0.0168` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
