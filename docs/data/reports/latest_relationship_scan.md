# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T10:07:26.912508+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9300`

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

- `news_risk_high->crypto_major_24h` score `31.3484` n `89` status `ready` deltaP `11.8212` edge `2.936` maxDD `-26.5286`
- `news_risk_high->crypto_alt_24h` score `30.0392` n `89` status `ready` deltaP `20.8197` edge `2.5642` maxDD `-12.645`
- `market_context_high->unknown_4h` score `14.6871` n `65` status `ready` deltaP `1.787` edge `1.227` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `6.2929` n `98` status `ready` deltaP `23.7524` edge `0.487` maxDD `-7.675`
- `market_context_high->commodity_24h` score `6.2731` n `62` status `ready` deltaP `33.1766` edge `0.3541` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.6604` n `98` status `ready` deltaP `22.8378` edge `0.3619` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0394` n `65` status `ready` deltaP `35.3916` edge `0.114` maxDD `-0.0659`
- `news_risk_high->equity_24h` score `3.391` n `89` status `ready` deltaP `24.6196` edge `0.1913` maxDD `-2.4942`
- `news_risk_high->crypto_alt_1h` score `3.0102` n `101` status `ready` deltaP `16.3811` edge `0.1882` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2422` n `65` status `ready` deltaP `29.294` edge `0.0089` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2176` n `101` status `ready` deltaP `18.3272` edge `0.1149` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.5451` n `72` status `ready` deltaP `18.2884` edge `0.0362` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.3343` n `62` status `ready` deltaP `16.9635` edge `0.0023` maxDD `-0.0027`
- `news_risk_high->metal_24h` score `0.7874` n `89` status `ready` deltaP `21.8809` edge `0.0395` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.7335` n `98` status `ready` deltaP `18.2149` edge `0.0451` maxDD `-2.0994`
- `news_risk_high->commodity_24h` score `0.7033` n `89` status `ready` deltaP `20.0921` edge `0.0868` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6161` n `101` status `ready` deltaP `14.4483` edge `0.0152` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4569` n `72` status `ready` deltaP `8.9488` edge `0.0042` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.2783` n `101` status `ready` deltaP `5.9628` edge `0.024` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0671` n `98` status `ready` deltaP `5.3851` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
