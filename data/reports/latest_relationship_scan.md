# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T18:22:34.485392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4200`

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

- `market_context_high->unknown_1h` score `32284.1642` n `45` status `ready` deltaP `1.4171` edge `2690.347` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22090.4099` n `45` status `ready` deltaP `3.0251` edge `1840.8612` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1049.2093` n `31` status `ready` deltaP `1.6322` edge `87.4408` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `837.4624` n `31` status `ready` deltaP `4.2437` edge `69.7659` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.0013` n `31` status `ready` deltaP `49.8264` edge `2.8346` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.0625` n `31` status `ready` deltaP `42.3611` edge `2.7228` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.3204` n `31` status `ready` deltaP `48.0903` edge `2.4561` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.3705` n `31` status `ready` deltaP `25.5409` edge `0.8643` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1014` n `31` status `ready` deltaP `41.2355` edge `0.6777` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `9.8324` n `31` status `ready` deltaP `34.0234` edge `0.6406` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.06` n `31` status `ready` deltaP `16.7781` edge `0.935` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.2257` n `31` status `ready` deltaP `52.4754` edge `0.1818` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.3611` n `31` status `ready` deltaP `40.1042` edge `0.1794` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4677` n `31` status `ready` deltaP `18.6401` edge `0.1834` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9995` n `31` status `ready` deltaP `32.6515` edge `0.0583` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.8183` n `45` status `ready` deltaP `34.2039` edge `0.0353` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.5872` n `31` status `ready` deltaP `11.5076` edge `0.3011` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5249` n `31` status `ready` deltaP `30.0464` edge `0.0186` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2177` n `31` status `ready` deltaP `10.9088` edge `0.2473` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6435` n `31` status `ready` deltaP `30.7803` edge `0.0334` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
