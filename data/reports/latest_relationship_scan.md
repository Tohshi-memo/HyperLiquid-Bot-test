# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T07:37:31.478100+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3225.3529` n `31` status `ready` deltaP `1.6322` edge `268.7861` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3181.2994` n `31` status `ready` deltaP `3.7864` edge `265.0887` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.2234` n `31` status `ready` deltaP `30.9028` edge `1.5626` maxDD `0.0`
- `news_risk_high->equity_24h` score `19.0362` n `31` status `ready` deltaP `30.3819` edge `1.3838` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0024` n `31` status `ready` deltaP `30.0347` edge `1.1333` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.0084` n `31` status `ready` deltaP `22.3397` edge `0.6888` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.8655` n `31` status `ready` deltaP `31.7369` edge `0.4086` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.7437` n `31` status `ready` deltaP `15.2537` edge `0.7764` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.3969` n `31` status `ready` deltaP `18.3188` edge `0.3551` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6358` n `31` status `ready` deltaP `38.5865` edge `0.1419` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.4064` n `31` status `ready` deltaP `31.9444` edge `0.0709` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.6904` n `31` status `ready` deltaP `16.5443` edge `0.1326` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.632` n `31` status `ready` deltaP `30.5173` edge `0.0419` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4278` n `31` status `ready` deltaP `29.2979` edge `0.0155` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0947` n `31` status `ready` deltaP `7.0166` edge `0.2679` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8746` n `31` status `ready` deltaP `9.8609` edge `0.2103` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1613` n `31` status `ready` deltaP `25.0917` edge `0.0095` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4482` n `31` status `ready` deltaP `12.5098` edge `0.0298` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.1194` n `31` status `ready` deltaP `5.3206` edge `-0.011` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6743` n `31` status `ready` deltaP `-5.056` edge `0.0037` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
