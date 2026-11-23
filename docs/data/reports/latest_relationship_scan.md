# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T09:07:36.058636+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->unknown_1h` score `19153.4717` n `72` status `ready` deltaP `1.5469` edge `1596.1285` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `12685.1426` n `72` status `ready` deltaP `3.9126` edge `1057.083` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1308.2231` n `31` status `ready` deltaP `3.4286` edge `109.0133` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1163.2296` n `31` status `ready` deltaP `4.8535` edge `96.9091` maxDD `-0.119`
- `news_risk_high->equity_4h` score `10.8514` n `31` status `ready` deltaP `34.7856` edge `0.7206` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.31` n `31` status `ready` deltaP `22.9494` edge `0.7932` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.2707` n `31` status `ready` deltaP `12.2049` edge `0.8643` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7399` n `31` status `ready` deltaP `18.7898` edge `0.2051` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4456` n `31` status `ready` deltaP `36.1576` edge `0.0721` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6771` n `31` status `ready` deltaP `31.3937` edge `0.0223` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3519` n `31` status `ready` deltaP `8.9627` edge `0.2879` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9411` n `31` status `ready` deltaP `7.4657` edge `0.2348` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5213` n `31` status `ready` deltaP `28.9839` edge `0.0297` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.408` n `31` status `ready` deltaP `19.522` edge `0.1061` maxDD `-0.7918`
- `market_context_high->fx_4h` score `1.0272` n `72` status `ready` deltaP `18.9363` edge `0.0181` maxDD `-0.3661`
- `news_risk_high->commodity_4h` score `0.8468` n `31` status `ready` deltaP `18.1255` edge `0.0275` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0273` n `31` status `ready` deltaP `1.5308` edge `0.0137` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3205` n `72` status `ready` deltaP `2.0126` edge `0.0117` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.3502` n `72` status `ready` deltaP `-0.6404` edge `0.0008` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-0.9122` n `72` status `ready` deltaP `-2.4119` edge `-0.0157` maxDD `-2.4807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
