# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T19:37:30.025755+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7679`

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

- `market_context_high->unknown_24h` score `3065.5314` n `96` status `ready` deltaP `-9.8958` edge `255.5699` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `101.1677` n `96` status `ready` deltaP `0.6351` edge `8.4397` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.7376` n `108` status `ready` deltaP `-5.0454` edge `6.5404` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.5424` n `72` status `ready` deltaP `45.8333` edge `1.3281` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7569` n `96` status `ready` deltaP `25.1736` edge `1.0043` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1771` n `108` status `ready` deltaP `19.3598` edge `0.441` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8471` n `96` status `ready` deltaP `43.0556` edge `0.1352` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6028` n `96` status `ready` deltaP `19.8679` edge `0.0436` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.7761` n `108` status `ready` deltaP `8.5773` edge `0.1029` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7676` n `96` status `ready` deltaP `11.1714` edge `0.0185` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.6521` n `96` status `ready` deltaP `4.4461` edge `0.1933` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.4135` n `96` status `ready` deltaP `6.1003` edge `0.0999` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.3663` n `96` status `ready` deltaP `14.126` edge `0.0595` maxDD `-0.8703`
- `market_context_high->fx_4h` score `0.3476` n `96` status `ready` deltaP `10.061` edge `0.001` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.2672` n `96` status `ready` deltaP `9.2128` edge `-0.0004` maxDD `-0.1407`
- `market_context_high->crypto_major_1h` score `0.2534` n `96` status `ready` deltaP `8.0339` edge `0.0817` maxDD `-5.2213`
- `market_context_high->metal_24h` score `-0.1214` n `96` status `ready` deltaP `11.2847` edge `0.1739` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.2681` n `96` status `ready` deltaP `15.3963` edge `0.137` maxDD `-14.5879`
- `market_context_high->commodity_1h` score `-0.3373` n `96` status `ready` deltaP `-0.8733` edge `0.014` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.3955` n `96` status `ready` deltaP `3.1188` edge `0.0021` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
