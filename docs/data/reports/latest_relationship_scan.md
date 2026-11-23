# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T05:37:24.377625+00:00`
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

- `market_context_high->unknown_1h` score `16015.6097` n `84` status `ready` deltaP `1.6966` edge `1334.639` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10759.9225` n `82` status `ready` deltaP `3.5061` edge `896.6507` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1337.2402` n `31` status `ready` deltaP `3.5783` edge `111.4304` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1174.8673` n `31` status `ready` deltaP `3.9388` edge `97.885` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.3195` n `31` status `ready` deltaP `36.7673` edge `0.7464` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.7681` n `31` status `ready` deltaP `24.6262` edge `0.8202` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.4846` n `31` status `ready` deltaP `13.272` edge `0.8846` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.8335` n `31` status `ready` deltaP `19.0892` edge `0.2109` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4358` n `31` status `ready` deltaP `36.0051` edge `0.0723` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6651` n `31` status `ready` deltaP `31.244` edge `0.0223` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4096` n `31` status `ready` deltaP `9.4118` edge `0.2923` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0222` n `31` status `ready` deltaP `8.0645` edge `0.2412` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5252` n `31` status `ready` deltaP `28.9839` edge `0.0302` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4876` n `31` status `ready` deltaP `20.4366` edge `0.1102` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8485` n `31` status `ready` deltaP `18.2779` edge `0.0267` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.0573` n `82` status `ready` deltaP `10.2134` edge `0.0125` maxDD `-0.5264`
- `news_risk_high->commodity_1h` score `-0.1028` n `31` status `ready` deltaP `0.932` edge `0.0114` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1258` n `84` status `ready` deltaP `3.5999` edge `0.0117` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1702` n `84` status `ready` deltaP `2.9798` edge `0.0039` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.1005` n `84` status `ready` deltaP `-4.598` edge `-0.0169` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
