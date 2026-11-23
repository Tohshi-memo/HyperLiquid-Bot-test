# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T03:07:37.029479+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `15789.1061` n `85` status `ready` deltaP `1.2169` edge `1315.7669` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10264.6945` n `85` status `ready` deltaP `2.3063` edge `855.3897` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1337.8365` n `31` status `ready` deltaP `4.1771` edge `111.4761` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1187.0879` n `31` status `ready` deltaP `3.7864` edge `98.9044` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.6731` n `31` status `ready` deltaP `38.2917` edge `0.7657` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.1265` n `31` status `ready` deltaP `26.1506` edge `0.8399` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6869` n `31` status `ready` deltaP `14.644` edge `0.9014` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0685` n `31` status `ready` deltaP `20.2868` edge `0.2225` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4552` n `31` status `ready` deltaP `36.1576` edge `0.0729` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7489` n `31` status `ready` deltaP `32.1422` edge `0.0233` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5413` n `31` status `ready` deltaP `10.31` edge `0.3032` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1633` n `31` status `ready` deltaP `9.1124` edge `0.2523` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5703` n `31` status `ready` deltaP `29.5827` edge `0.032` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5215` n `31` status `ready` deltaP `20.894` edge `0.1115` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8368` n `31` status `ready` deltaP `18.2779` edge `0.0252` maxDD `-0.5151`
- `market_context_high->fx_4h` score `-0.0735` n `85` status `ready` deltaP `9.801` edge `0.0127` maxDD `-0.6635`
- `news_risk_high->commodity_1h` score `-0.0801` n `31` status `ready` deltaP `1.2314` edge `0.0113` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3577` n `85` status `ready` deltaP `2.448` edge `0.0057` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.4636` n `85` status `ready` deltaP `0.9088` edge `0.0009` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.1762` n `85` status `ready` deltaP `-5.9792` edge `-0.0174` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
