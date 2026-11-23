# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T05:22:30.044835+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5298`

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

- `market_context_high->unknown_1h` score `16015.8184` n `84` status `ready` deltaP `1.8463` edge `1334.6554` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10762.9357` n `82` status `ready` deltaP `3.5061` edge `896.9018` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1337.449` n `31` status `ready` deltaP `3.728` edge `111.4468` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1177.8805` n `31` status `ready` deltaP `3.9388` edge `98.1361` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.3521` n `31` status `ready` deltaP `36.9198` edge `0.7481` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.8139` n `31` status `ready` deltaP `24.7787` edge `0.823` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.512` n `31` status `ready` deltaP `13.4244` edge `0.8871` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.8623` n `31` status `ready` deltaP `19.2389` edge `0.2123` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4346` n `31` status `ready` deltaP `36.0051` edge `0.0722` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6795` n `31` status `ready` deltaP `31.3937` edge `0.0225` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4268` n `31` status `ready` deltaP `9.5615` edge `0.2935` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0409` n `31` status `ready` deltaP `8.2142` edge `0.2426` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5267` n `31` status `ready` deltaP `28.9839` edge `0.0304` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4986` n `31` status `ready` deltaP `20.5891` edge `0.1106` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8485` n `31` status `ready` deltaP `18.2779` edge `0.0267` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.066` n `82` status `ready` deltaP `10.3658` edge `0.0126` maxDD `-0.5264`
- `news_risk_high->commodity_1h` score `-0.1016` n `31` status `ready` deltaP `0.932` edge `0.0115` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1242` n `84` status `ready` deltaP `3.5999` edge `0.0119` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1609` n `84` status `ready` deltaP `3.1295` edge `0.0041` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.0997` n `84` status `ready` deltaP `-4.598` edge `-0.0168` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
