# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T17:37:27.794885+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7498`

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

- `news_risk_high->unknown_1h` score `3440.2883` n `31` status `ready` deltaP `2.3807` edge `286.6924` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3272.9085` n `31` status `ready` deltaP `3.634` edge `272.7238` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.1575` n `31` status `ready` deltaP `38.6482` edge `1.8388` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2821` n `31` status `ready` deltaP `36.7418` edge `1.3619` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.1348` n `31` status `ready` deltaP `29.2894` edge `0.8993` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.4927` n `31` status `ready` deltaP `24.7787` edge `0.7129` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.0174` n `31` status `ready` deltaP `33.871` edge `0.3237` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9885` n `31` status `ready` deltaP `18.9123` edge `0.7834` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.1653` n `31` status `ready` deltaP `42.8356` edge `0.1577` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9134` n `31` status `ready` deltaP `17.0403` edge `0.24` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.7351` n `31` status `ready` deltaP `33.2612` edge `0.0322` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.494` n `31` status `ready` deltaP `26.6898` edge `0.0299` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3774` n `31` status `ready` deltaP `29.1482` edge `0.0123` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2922` n `31` status `ready` deltaP `15.197` edge `0.1084` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0869` n `31` status `ready` deltaP `7.0166` edge `0.2669` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9938` n `31` status `ready` deltaP `11.0585` edge `0.2176` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1543` n `31` status `ready` deltaP `24.942` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5494` n `31` status `ready` deltaP `12.1804` edge `0.029` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.4757` n `31` status `ready` deltaP `13.5769` edge `0.0262` maxDD `-0.7918`
- `market_context_high->fx_1h` score `0.4484` n `65` status `ready` deltaP `11.6882` edge `0.0017` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
