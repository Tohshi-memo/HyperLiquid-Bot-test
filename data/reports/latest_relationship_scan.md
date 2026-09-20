# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T20:22:30.577447+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10418`

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

- `news_risk_high->crypto_major_24h` score `24.0618` n `98` status `ready` deltaP `11.9225` edge `2.6115` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.4046` n `98` status `ready` deltaP `15.2671` edge `2.0867` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `13.9816` n `44` status `ready` deltaP `-0.4158` edge `1.1829` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.8234` n `101` status `ready` deltaP `21.358` edge `0.3805` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.146` n `44` status `ready` deltaP `38.1791` edge `0.1043` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `3.8041` n `101` status `ready` deltaP `20.4434` edge `0.3065` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.9105` n `101` status `ready` deltaP `16.8302` edge `0.1769` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1875` n `101` status `ready` deltaP `18.6266` edge `0.1104` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.5736` n `44` status `ready` deltaP `22.2422` edge `0.0091` maxDD `-0.0999`
- `news_risk_high->commodity_24h` score `1.0315` n `98` status `ready` deltaP `22.775` edge `0.111` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8877` n `55` status `ready` deltaP `12.9314` edge `0.0057` maxDD `-0.1012`
- `market_context_high->commodity_1h` score `0.757` n `55` status `ready` deltaP `13.6581` edge `0.0335` maxDD `-0.1998`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.613` n `101` status `ready` deltaP `17.0988` edge `0.0425` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.4978` n `98` status `ready` deltaP `16.3974` edge `0.0731` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2378` n `55` status `ready` deltaP `7.2836` edge `0.0061` maxDD `-0.4538`
- `news_risk_high->equity_1h` score `0.2304` n `101` status `ready` deltaP `5.364` edge `0.024` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.1749` n `101` status `ready` deltaP `8.3358` edge `0.0226` maxDD `-0.421`
- `news_risk_high->metal_24h` score `0.1191` n `98` status `ready` deltaP `14.9837` edge `-0.0002` maxDD `-2.4203`
- `news_risk_high->fx_1h` score `-0.2915` n `101` status `ready` deltaP `2.0943` edge `0.0061` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
