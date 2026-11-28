# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T01:07:23.217534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3222`

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

- `news_risk_high->unknown_1h` score `3307.3945` n `31` status `ready` deltaP `1.6322` edge `275.6229` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3168.6487` n `31` status `ready` deltaP `3.4815` edge `264.0365` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.6006` n `31` status `ready` deltaP `27.9029` edge `1.2807` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.2816` n `31` status `ready` deltaP `26.1698` edge `0.849` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.5301` n `31` status `ready` deltaP `23.9168` edge `0.8014` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.5791` n `31` status `ready` deltaP `19.4433` edge `0.589` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2625` n `31` status `ready` deltaP `29.1454` edge `0.2923` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8069` n `31` status `ready` deltaP `14.3391` edge `0.6624` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.703` n `31` status `ready` deltaP `38.6762` edge `0.1469` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.4004` n `31` status `ready` deltaP `12.1877` edge `0.2296` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.2641` n `31` status `ready` deltaP `28.0783` edge `0.0275` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2636` n `31` status `ready` deltaP `27.8009` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2502` n `31` status `ready` deltaP `15.197` edge `0.1049` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.1668` n `31` status `ready` deltaP `24.6101` edge `0.0165` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.8586` n `31` status `ready` deltaP `5.3699` edge `0.2486` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6455` n `31` status `ready` deltaP `8.0645` edge `0.1929` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1333` n `31` status `ready` deltaP `24.6426` edge `0.0089` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3469` n `31` status `ready` deltaP `8.8267` edge `0.0254` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2727` n `31` status `ready` deltaP `10.5281` edge `0.0205` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3687` n `31` status `ready` deltaP `-2.5111` edge `0.0122` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
