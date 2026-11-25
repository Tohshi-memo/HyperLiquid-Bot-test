# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T23:37:24.509532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3911`

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

- `market_context_high->unknown_1h` score `32148.6422` n `45` status `ready` deltaP `1.5668` edge `2679.0525` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21802.9234` n `45` status `ready` deltaP `1.958` edge `1816.9111` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `913.6872` n `31` status `ready` deltaP `1.7819` edge `76.1463` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `549.9759` n `31` status `ready` deltaP `3.1766` edge `45.8158` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `240.6385` n `31` status `ready` deltaP `6.0764` edge `20.0127` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.6879` n `31` status `ready` deltaP `52.0833` edge `3.4601` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.961` n `31` status `ready` deltaP `52.7778` edge `3.1449` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.3042` n `31` status `ready` deltaP `52.2569` edge `2.7603` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.4763` n `31` status `ready` deltaP `38.6313` edge `0.7263` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9255` n `31` status `ready` deltaP `26.6079` edge `0.8201` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4287` n `31` status `ready` deltaP `37.682` edge `0.6659` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4487` n `31` status `ready` deltaP `53.2986` edge `0.2654` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7048` n `31` status `ready` deltaP `17.3879` edge `0.8854` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2261` n `31` status `ready` deltaP `44.3157` edge `0.1529` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6775` n `31` status `ready` deltaP `19.9874` edge `0.1919` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.35` n `31` status `ready` deltaP `36.4625` edge `0.0621` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6746` n `31` status `ready` deltaP `31.6931` edge `0.0201` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.482` n `31` status `ready` deltaP `10.4597` edge `0.2946` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3291` n `45` status `ready` deltaP `28.8685` edge `0.0301` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2814` n `31` status `ready` deltaP `13.0046` edge `0.2415` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
