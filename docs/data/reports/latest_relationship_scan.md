# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T01:22:38.877119+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4068`

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

- `market_context_high->unknown_1h` score `32254.7426` n `45` status `ready` deltaP `1.8662` edge `2687.8922` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21997.0405` n `45` status `ready` deltaP `3.1776` edge `1833.0794` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1019.7876` n `31` status `ready` deltaP `2.0813` edge `84.986` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `744.093` n `31` status `ready` deltaP `4.3962` edge `61.9841` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.7611` n `31` status `ready` deltaP `50.1736` edge `2.8956` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.1351` n `31` status `ready` deltaP `43.9236` edge `2.8851` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.7795` n `31` status `ready` deltaP `48.9583` edge `2.5719` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7127` n `31` status `ready` deltaP `26.6079` edge `0.8857` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1471` n `31` status `ready` deltaP `41.2355` edge `0.6815` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1722` n `31` status `ready` deltaP `34.1759` edge `0.6679` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.2161` n `31` status `ready` deltaP `16.9305` edge `0.954` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.6778` n `31` status `ready` deltaP `42.1875` edge `0.1919` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.6112` n `31` status `ready` deltaP `47.6143` edge `0.163` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6464` n `31` status `ready` deltaP `18.9395` edge `0.1963` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0297` n `31` status `ready` deltaP `32.8039` edge `0.0598` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7135` n `31` status `ready` deltaP `12.4058` edge `0.3113` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.6504` n `45` status `ready` deltaP `32.3746` edge `0.0335` maxDD `-0.2774`
- `news_risk_high->index_1h` score `2.5716` n `31` status `ready` deltaP `30.4955` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.386` n `31` status `ready` deltaP `12.4058` edge `0.2589` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6248` n `31` status `ready` deltaP `30.6306` edge `0.032` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
