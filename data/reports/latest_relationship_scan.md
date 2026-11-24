# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T21:22:41.491551+00:00`
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

- `market_context_high->unknown_1h` score `32267.7866` n `45` status `ready` deltaP `1.4171` edge `2688.9822` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22039.5337` n `45` status `ready` deltaP `3.1776` edge `1836.6205` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1032.8317` n `31` status `ready` deltaP `1.6322` edge `86.076` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `786.5862` n `31` status `ready` deltaP `4.3962` edge `65.5252` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.6171` n `31` status `ready` deltaP `50.1736` edge `2.8836` maxDD `0.0`
- `news_risk_high->equity_24h` score `37.2015` n `31` status `ready` deltaP `43.9236` edge `2.8073` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.2131` n `31` status `ready` deltaP `48.9583` edge `2.5247` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8019` n `31` status `ready` deltaP `26.9128` edge `0.8911` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1014` n `31` status `ready` deltaP `41.2355` edge `0.6777` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.456` n `31` status `ready` deltaP `34.6332` edge `0.6885` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.326` n `31` status `ready` deltaP `17.6927` edge `0.963` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.9546` n `31` status `ready` deltaP `50.392` edge `0.1731` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5732` n `31` status `ready` deltaP `41.8403` edge `0.1855` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.602` n `31` status `ready` deltaP `18.9395` edge `0.1926` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0707` n `31` status `ready` deltaP `32.9564` edge `0.0622` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7367` n `45` status `ready` deltaP `33.2893` edge `0.0346` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6987` n `31` status `ready` deltaP `12.4058` edge `0.3094` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5596` n `31` status `ready` deltaP `30.3458` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3611` n `31` status `ready` deltaP `12.1064` edge `0.2577` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6529` n `31` status `ready` deltaP `30.93` edge `0.0336` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
