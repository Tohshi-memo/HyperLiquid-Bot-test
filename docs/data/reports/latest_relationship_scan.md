# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T00:52:27.001245+00:00`
- Price records: `672`
- Market context records: `5303`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `21.0584` n `153` status `ready` deltaP `24.9081` edge `1.5978` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5836` n `153` status `ready` deltaP `25.7353` edge `0.8754` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.069` n `153` status `ready` deltaP `19.9653` edge `0.8522` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `3.5786` n `189` status `ready` deltaP `13.7696` edge `0.3705` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.4368` n `189` status `ready` deltaP `14.1373` edge `0.4214` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.8658` n `189` status `ready` deltaP `11.2418` edge `0.2444` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5409` n `153` status `ready` deltaP `13.3068` edge `0.0459` maxDD `-0.8294`
- `market_context_high->index_24h` score `0.3122` n `153` status `ready` deltaP `20.8231` edge `0.0647` maxDD `-7.413`
- `market_context_high->crypto_alt_1h` score `0.276` n `194` status `ready` deltaP `3.4431` edge `0.0962` maxDD `-5.0257`
- `market_context_high->unknown_4h` score `0.2291` n `189` status `ready` deltaP `12.8114` edge `0.0359` maxDD `-5.5109`
- `market_context_high->equity_1h` score `0.2027` n `194` status `ready` deltaP `8.3123` edge `0.058` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.1785` n `194` status `ready` deltaP `5.5389` edge `0.1025` maxDD `-6.9639`
- `market_context_high->index_1h` score `0.013` n `194` status `ready` deltaP `6.0683` edge `0.011` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.3311` n `194` status `ready` deltaP `2.5449` edge `0.0081` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4178` n `194` status `ready` deltaP `-0.6327` edge `-0.0004` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4426` n `189` status `ready` deltaP `4.7845` edge `0.0231` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.696` n `189` status `ready` deltaP `1.7091` edge `0.0023` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4467` n `194` status `ready` deltaP `-3.3258` edge `-0.0066` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.1358` n `189` status `ready` deltaP `-6.3541` edge `-0.008` maxDD `-11.2101`
- `market_context_high->crypto_alt_24h` score `-2.9405` n `153` status `ready` deltaP `13.3476` edge `0.375` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
