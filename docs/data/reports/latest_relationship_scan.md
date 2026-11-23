# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T06:52:28.970845+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5232`

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

- `market_context_high->unknown_1h` score `16716.0254` n `81` status `ready` deltaP `2.3231` edge `1393.0028` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10926.4731` n `81` status `ready` deltaP `3.6134` edge `910.5292` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1323.4007` n `31` status `ready` deltaP `3.2789` edge `110.2791` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1169.8371` n `31` status `ready` deltaP `4.0913` edge `97.4648` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.1181` n `31` status `ready` deltaP `36.0051` edge `0.7347` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.5164` n `31` status `ready` deltaP `23.864` edge `0.8043` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3271` n `31` status `ready` deltaP `12.5098` edge `0.8695` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7567` n `31` status `ready` deltaP `18.7898` edge `0.2065` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4602` n `31` status `ready` deltaP `36.31` edge `0.0723` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6519` n `31` status `ready` deltaP `31.0943` edge `0.0222` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3792` n `31` status `ready` deltaP `9.2621` edge `0.2894` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9747` n `31` status `ready` deltaP `7.7651` edge `0.2371` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.501` n `31` status `ready` deltaP `28.6845` edge `0.0291` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4332` n `31` status `ready` deltaP `19.8269` edge `0.1073` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8343` n `31` status `ready` deltaP `18.1255` edge `0.0259` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.2996` n `81` status `ready` deltaP `12.5979` edge `0.0142` maxDD `-0.4483`
- `news_risk_high->commodity_1h` score `-0.0345` n `31` status `ready` deltaP `1.5308` edge `0.0131` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1045` n `81` status `ready` deltaP `3.8737` edge `0.0126` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1367` n `81` status `ready` deltaP `3.5355` edge `0.0045` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-0.8464` n `81` status `ready` deltaP `7.9193` edge `0.0171` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
