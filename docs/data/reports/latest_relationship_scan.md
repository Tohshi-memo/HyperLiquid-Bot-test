# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T09:37:47.798966+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4584`

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

- `market_context_high->unknown_1h` score `32330.1747` n `45` status `ready` deltaP `1.4171` edge `2694.1812` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22189.4358` n `45` status `ready` deltaP `2.5678` edge `1849.1164` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1120.6453` n `31` status `ready` deltaP `1.6322` edge `93.3938` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `954.0827` n `31` status `ready` deltaP `3.7864` edge `79.4873` maxDD `-0.119`
- `news_risk_high->crypto_major_24h` score `35.488` n `31` status `ready` deltaP `47.5694` edge `2.6402` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.7354` n `31` status `ready` deltaP `41.4931` edge `2.618` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.6958` n `31` status `ready` deltaP `45.3125` edge `2.2559` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.3937` n `31` status `ready` deltaP `41.4091` edge `0.7009` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.5394` n `31` status `ready` deltaP `23.1018` edge `0.8113` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.9491` n `31` status `ready` deltaP `31.7369` edge `0.5824` maxDD `-2.1911`
- `news_risk_high->fx_24h` score `6.7023` n `31` status `ready` deltaP `56.4684` edge `0.1949` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.6469` n `31` status `ready` deltaP `14.3391` edge `0.8983` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.2346` n `31` status `ready` deltaP `39.0625` edge `0.1758` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2913` n `31` status `ready` deltaP `18.0413` edge `0.1727` maxDD `-0.163`
- `market_context_high->fx_4h` score `2.9763` n `45` status `ready` deltaP `35.7283` edge `0.0383` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.797` n `31` status `ready` deltaP `30.9747` edge `0.0526` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.5163` n `31` status `ready` deltaP `10.9088` edge `0.296` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4925` n `31` status `ready` deltaP `29.747` edge `0.0179` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.1358` n `31` status `ready` deltaP `10.4597` edge `0.2398` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.645` n `31` status `ready` deltaP `31.2294` edge `0.0306` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
