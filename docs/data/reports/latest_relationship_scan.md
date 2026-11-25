# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T07:22:23.435151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4104`

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

- `market_context_high->unknown_1h` score `32237.6953` n `45` status `ready` deltaP `2.1656` edge `2686.4696` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21978.1225` n `45` status `ready` deltaP `3.1776` edge `1831.5029` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1002.7403` n `31` status `ready` deltaP `2.3807` edge `83.5634` maxDD `-0.7395`
- `news_risk_high->unknown_24h` score `848.1623` n `31` status `ready` deltaP `5.7292` edge `70.642` maxDD `0.0`
- `news_risk_high->unknown_4h` score `725.175` n `31` status `ready` deltaP `4.3962` edge `60.4076` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `40.7849` n `31` status `ready` deltaP `45.4861` edge `3.0955` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.7067` n `31` status `ready` deltaP `50.1736` edge `2.9744` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.3786` n `31` status `ready` deltaP `50.3472` edge `2.6959` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.881` n `31` status `ready` deltaP `27.8275` edge `0.8916` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.3786` n `31` status `ready` deltaP `41.2355` edge `0.7008` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1329` n `31` status `ready` deltaP `37.5295` edge `0.7256` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5657` n `31` status `ready` deltaP `18.9123` edge `0.9856` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.296` n `31` status `ready` deltaP `46.1806` edge `0.2168` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1519` n `31` status `ready` deltaP `43.4476` edge `0.1525` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.9174` n `31` status `ready` deltaP `20.4365` edge `0.2089` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3602` n `31` status `ready` deltaP `36.0051` edge `0.066` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7619` n `31` status `ready` deltaP `12.4058` edge `0.3175` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6734` n `31` status `ready` deltaP `31.5434` edge `0.021` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5944` n `45` status `ready` deltaP `31.7649` edge `0.0329` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.361` n `31` status `ready` deltaP `12.4058` edge `0.2557` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
