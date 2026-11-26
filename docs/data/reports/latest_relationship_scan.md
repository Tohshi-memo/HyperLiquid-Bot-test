# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T06:52:25.516982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4007`

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

- `news_risk_high->unknown_4h` score `3225.9859` n `31` status `ready` deltaP `3.4815` edge `268.8146` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3223.9465` n `31` status `ready` deltaP `1.6322` edge `268.6689` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `93.6546` n `31` status `ready` deltaP `1.6322` edge `7.8031` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `40.7515` n `31` status `ready` deltaP `47.0486` edge `3.0823` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `38.9093` n `31` status `ready` deltaP `47.9167` edge `2.923` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.3362` n `31` status `ready` deltaP `47.2222` edge `2.4632` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8875` n `31` status `ready` deltaP `26.9128` edge `0.8149` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4771` n `31` status `ready` deltaP `37.9869` edge `0.6679` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.8315` n `31` status `ready` deltaP `33.5966` edge `0.6228` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8448` n `31` status `ready` deltaP `17.8452` edge `0.9003` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.6902` n `31` status `ready` deltaP `48.4375` edge `0.2346` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.771` n `31` status `ready` deltaP `20.5862` edge `0.1957` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4286` n `31` status `ready` deltaP `36.9198` edge `0.0656` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7201` n `31` status `ready` deltaP `32.1422` edge `0.0209` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5086` n `31` status `ready` deltaP `10.31` edge `0.299` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2838` n `31` status `ready` deltaP `13.1543` edge `0.2408` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1092` n `31` status `ready` deltaP `26.8096` edge `0.0255` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5181` n `31` status `ready` deltaP `29.5827` edge `0.0253` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1047` n `31` status `ready` deltaP `16.7781` edge `0.0855` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
