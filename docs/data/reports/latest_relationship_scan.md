# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T04:52:29.042548+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5284`

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

- `market_context_high->unknown_1h` score `16012.7656` n `84` status `ready` deltaP `1.8463` edge `1334.401` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10771.0273` n `82` status `ready` deltaP `3.5061` edge `897.5761` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1334.3962` n `31` status `ready` deltaP `3.728` edge `111.1924` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1185.9721` n `31` status `ready` deltaP `3.9388` edge `98.8104` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.4137` n `31` status `ready` deltaP `37.2247` edge `0.7512` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.8923` n `31` status `ready` deltaP `25.0836` edge `0.8275` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.5559` n `31` status `ready` deltaP `13.7293` edge `0.8907` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.8826` n `31` status `ready` deltaP `19.3886` edge `0.213` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4212` n `31` status `ready` deltaP `35.8527` edge `0.0721` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7046` n `31` status `ready` deltaP `31.6931` edge `0.0226` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4369` n `31` status `ready` deltaP `9.7112` edge `0.2938` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0619` n `31` status `ready` deltaP `8.5136` edge `0.2433` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5353` n `31` status `ready` deltaP `29.1336` edge `0.0305` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5081` n `31` status `ready` deltaP `20.7415` edge `0.1108` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8485` n `31` status `ready` deltaP `18.2779` edge `0.0267` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.0842` n `82` status `ready` deltaP `10.6707` edge `0.0129` maxDD `-0.5264`
- `news_risk_high->commodity_1h` score `-0.1004` n `31` status `ready` deltaP `0.932` edge `0.0116` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1157` n `84` status `ready` deltaP `3.7496` edge `0.012` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1445` n `84` status `ready` deltaP `3.4289` edge `0.0042` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.0989` n `84` status `ready` deltaP `-4.598` edge `-0.0167` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
