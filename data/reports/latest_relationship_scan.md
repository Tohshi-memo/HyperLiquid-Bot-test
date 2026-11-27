# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T00:37:23.371296+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3540`

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

- `news_risk_high->unknown_1h` score `3209.3904` n `31` status `ready` deltaP `1.9316` edge `267.4539` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3180.1206` n `31` status `ready` deltaP `4.3962` edge `264.9864` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `26.7987` n `31` status `ready` deltaP `35.7639` edge `1.9948` maxDD `0.0`
- `news_risk_high->equity_24h` score `23.8692` n `31` status `ready` deltaP `35.0694` edge `1.7553` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.6585` n `31` status `ready` deltaP `34.8958` edge `1.4889` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.6296` n `31` status `ready` deltaP `23.864` edge `0.7304` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.3351` n `31` status `ready` deltaP `35.243` edge `0.5077` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.2877` n `31` status `ready` deltaP `22.6591` edge `0.4004` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.2769` n `31` status `ready` deltaP `16.7781` edge `0.8346` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9604` n `31` status `ready` deltaP `42.0587` edge `0.1458` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.2199` n `31` status `ready` deltaP `36.4583` edge `0.1086` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1257` n `31` status `ready` deltaP `18.3407` edge `0.1569` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9475` n `31` status `ready` deltaP `33.2612` edge `0.0499` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.568` n `31` status `ready` deltaP `30.7949` edge `0.0172` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2912` n `31` status `ready` deltaP `8.0645` edge `0.2861` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0593` n `31` status `ready` deltaP `11.0585` edge `0.226` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3233` n `31` status `ready` deltaP `27.0378` edge `0.0173` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.6352` n `31` status `ready` deltaP `13.1196` edge `0.0497` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2044` n `31` status `ready` deltaP `9.1316` edge `0.0051` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4994` n `31` status `ready` deltaP `-3.2596` edge `0.0063` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
