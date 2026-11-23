# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T04:07:39.180449+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5306`

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

- `market_context_high->unknown_1h` score `16013.2072` n `84` status `ready` deltaP `2.2954` edge `1334.4348` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10769.1985` n `82` status `ready` deltaP `3.5061` edge `897.4237` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1334.8377` n `31` status `ready` deltaP `4.1771` edge `111.2262` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1184.1433` n `31` status `ready` deltaP `3.9388` edge `98.658` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.5055` n `31` status `ready` deltaP `37.682` edge `0.7558` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.9829` n `31` status `ready` deltaP `25.5409` edge `0.832` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.596` n `31` status `ready` deltaP `14.0342` edge `0.8938` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9162` n `31` status `ready` deltaP `19.688` edge `0.2138` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4212` n `31` status `ready` deltaP `35.8527` edge `0.0721` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6914` n `31` status `ready` deltaP `31.5434` edge `0.0225` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4345` n `31` status `ready` deltaP `9.7112` edge `0.2935` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0697` n `31` status `ready` deltaP `8.6633` edge `0.2433` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5353` n `31` status `ready` deltaP `29.1336` edge `0.0305` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5199` n `31` status `ready` deltaP `20.894` edge `0.1113` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8461` n `31` status `ready` deltaP `18.2779` edge `0.0264` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.115` n `82` status `ready` deltaP `11.128` edge `0.0138` maxDD `-0.5264`
- `news_risk_high->commodity_1h` score `-0.104` n `31` status `ready` deltaP `0.932` edge `0.0113` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1157` n `84` status `ready` deltaP `3.7496` edge `0.012` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1531` n `84` status `ready` deltaP `3.2792` edge `0.0041` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-1.0895` n `82` status `ready` deltaP `5.9452` edge `0.01` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
