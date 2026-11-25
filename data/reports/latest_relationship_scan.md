# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T17:07:30.104930+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32183.3713` n `45` status `ready` deltaP `2.1656` edge `2681.9426` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21873.4387` n `45` status `ready` deltaP `2.7202` edge `1822.7823` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `948.4163` n `31` status `ready` deltaP `2.3807` edge `79.0364` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `620.4912` n `31` status `ready` deltaP `3.9388` edge `51.687` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `372.5399` n `31` status `ready` deltaP `5.7292` edge `31.0068` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.2303` n `31` status `ready` deltaP `52.0833` edge `3.5053` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.4229` n `31` status `ready` deltaP `53.6458` edge `3.1776` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.7941` n `31` status `ready` deltaP `56.0764` edge `2.859` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0442` n `31` status `ready` deltaP `27.8275` edge `0.9052` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `12.0326` n `31` status `ready` deltaP `41.2355` edge `0.7553` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.6588` n `31` status `ready` deltaP `38.749` edge `0.7613` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5252` n `31` status `ready` deltaP `19.0647` edge `0.9794` maxDD `-7.6714`
- `news_risk_high->index_24h` score `7.4034` n `31` status `ready` deltaP `52.7778` edge `0.2651` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.4573` n `31` status `ready` deltaP `46.9198` edge `0.1548` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0817` n `31` status `ready` deltaP `20.8856` edge `0.2196` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.53` n `31` status `ready` deltaP `37.3771` edge `0.071` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7393` n `31` status `ready` deltaP `32.1422` edge `0.0225` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.6847` n `31` status `ready` deltaP `11.5076` edge `0.3136` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4676` n `45` status `ready` deltaP `30.2405` edge `0.0325` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4491` n `31` status `ready` deltaP `13.4537` edge `0.26` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
