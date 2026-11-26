# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T10:22:30.861323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_4h` score `3246.4363` n `31` status `ready` deltaP `3.4815` edge `270.5188` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3233.1877` n `31` status `ready` deltaP `1.6322` edge `269.439` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `102.8958` n `31` status `ready` deltaP `1.6322` edge `8.5732` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `37.5342` n `31` status `ready` deltaP `44.6181` edge `2.8304` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `36.9293` n `31` status `ready` deltaP `45.4861` edge `2.7742` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.2673` n `31` status `ready` deltaP `44.7917` edge `2.307` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.046` n `31` status `ready` deltaP `27.9799` edge `0.821` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.8016` n `31` status `ready` deltaP `39.3588` edge `0.6858` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.0143` n `31` status `ready` deltaP `31.166` edge `0.5709` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0233` n `31` status `ready` deltaP `19.522` edge `0.912` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.2258` n `31` status `ready` deltaP `46.0069` edge `0.2121` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.143` n `31` status `ready` deltaP `43.6212` edge `0.1506` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.8357` n `31` status `ready` deltaP `21.0353` edge `0.1981` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5829` n `31` status `ready` deltaP `38.4442` edge `0.0683` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7764` n `31` status `ready` deltaP `32.741` edge `0.0216` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4657` n `31` status `ready` deltaP `9.7112` edge `0.2975` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2619` n `31` status `ready` deltaP `12.8549` edge `0.24` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.0556` n `31` status `ready` deltaP `26.1999` edge `0.0251` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.511` n `31` status `ready` deltaP `29.5827` edge `0.0244` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0865` n `31` status `ready` deltaP `16.4732` edge `0.0852` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
