# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T14:07:44.625485+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3804`

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

- `market_context_high->unknown_1h` score `32207.3821` n `45` status `ready` deltaP `2.1656` edge `2683.9435` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21930.4609` n `45` status `ready` deltaP `3.1776` edge `1827.5311` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `972.4271` n `31` status `ready` deltaP `2.3807` edge `81.0373` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `677.5134` n `31` status `ready` deltaP `4.3962` edge `56.4358` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `532.9007` n `31` status `ready` deltaP `5.7292` edge `44.3702` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.4059` n `31` status `ready` deltaP `50.1736` edge `3.366` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.4469` n `31` status `ready` deltaP `51.7361` edge `3.109` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.1272` n `31` status `ready` deltaP `54.3403` edge `2.815` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8553` n `31` status `ready` deltaP `27.3701` edge `0.8925` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.8191` n `31` status `ready` deltaP `41.2355` edge `0.7375` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1595` n `31` status `ready` deltaP `37.682` edge `0.7268` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.4541` n `31` status `ready` deltaP `18.9123` edge `0.9713` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.0646` n `31` status `ready` deltaP `50.8681` edge `0.2496` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2865` n `31` status `ready` deltaP `45.0101` edge `0.1533` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.981` n `31` status `ready` deltaP `20.7359` edge `0.2122` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3892` n `31` status `ready` deltaP `36.1576` edge `0.0674` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7565` n `31` status `ready` deltaP `11.807` edge `0.3208` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.719` n `31` status `ready` deltaP `31.9925` edge `0.0218` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.509` n `45` status `ready` deltaP `30.6978` edge `0.0329` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4998` n `31` status `ready` deltaP `13.6034` edge `0.2655` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
