# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T23:37:28.220914+00:00`
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

- `news_risk_high->unknown_1h` score `3211.476` n `31` status `ready` deltaP `2.0813` edge `267.6267` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3188.1114` n `31` status `ready` deltaP `4.3962` edge `265.6523` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `27.3384` n `31` status `ready` deltaP `36.2847` edge `2.0363` maxDD `0.0`
- `news_risk_high->equity_24h` score `24.3745` n `31` status `ready` deltaP `35.4167` edge `1.7951` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.2` n `31` status `ready` deltaP `35.5903` edge `1.5294` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.7412` n `31` status `ready` deltaP `23.864` edge `0.7397` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.3819` n `31` status `ready` deltaP `35.243` edge `0.5116` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.3405` n `31` status `ready` deltaP `22.6591` edge `0.4048` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.305` n `31` status `ready` deltaP `16.7781` edge `0.8382` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.0068` n `31` status `ready` deltaP `42.5795` edge `0.1462` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.3016` n `31` status `ready` deltaP `36.8056` edge `0.1131` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1797` n `31` status `ready` deltaP `18.6401` edge `0.1594` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9681` n `31` status `ready` deltaP `33.4137` edge `0.0506` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5728` n `31` status `ready` deltaP `30.7949` edge `0.0176` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3153` n `31` status `ready` deltaP `8.3639` edge `0.2872` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0928` n `31` status `ready` deltaP `11.3579` edge `0.2283` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3576` n `31` status `ready` deltaP `27.4869` edge `0.0187` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.664` n `31` status `ready` deltaP `13.1196` edge `0.0534` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2234` n `31` status `ready` deltaP `9.4365` edge `0.0055` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4455` n `31` status `ready` deltaP `-2.6608` edge `0.0068` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
