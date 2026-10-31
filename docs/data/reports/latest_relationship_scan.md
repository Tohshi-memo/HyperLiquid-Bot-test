# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T20:22:27.096229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7703`

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

- `market_context_high->unknown_24h` score `3066.0906` n `96` status `ready` deltaP `-9.8958` edge `255.6165` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `101.1485` n `96` status `ready` deltaP `0.6351` edge `8.4381` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.6657` n `108` status `ready` deltaP `-5.3448` edge `6.5364` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.4138` n `75` status `ready` deltaP `45.7708` edge `1.3178` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7761` n `96` status `ready` deltaP `25.1736` edge `1.0059` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.3037` n `108` status `ready` deltaP `19.8171` edge `0.4485` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9008` n `96` status `ready` deltaP `43.5764` edge `0.1362` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6406` n `96` status `ready` deltaP `20.3252` edge `0.0437` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.8301` n `108` status `ready` deltaP `8.8767` edge `0.1054` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7915` n `96` status `ready` deltaP `11.4708` edge `0.0185` maxDD `-0.3209`
- `market_context_high->equity_4h` score `0.6553` n `96` status `ready` deltaP `4.4461` edge `0.1937` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.4306` n `96` status `ready` deltaP `6.3997` edge `0.1001` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.3584` n `96` status `ready` deltaP `13.9735` edge `0.0595` maxDD `-0.8703`
- `market_context_high->fx_4h` score `0.3476` n `96` status `ready` deltaP `10.061` edge `0.001` maxDD `-0.1285`
- `market_context_high->crypto_major_1h` score `0.276` n `96` status `ready` deltaP `8.3333` edge `0.0826` maxDD `-5.2213`
- `market_context_high->fx_1h` score `0.2672` n `96` status `ready` deltaP `9.2128` edge `-0.0004` maxDD `-0.1407`
- `market_context_high->metal_24h` score `-0.1085` n `96` status `ready` deltaP `11.4583` edge `0.1744` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.2447` n `96` status `ready` deltaP `15.3963` edge `0.14` maxDD `-14.5879`
- `market_context_high->commodity_1h` score `-0.3124` n `96` status `ready` deltaP `-0.4242` edge `0.0142` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.3967` n `96` status `ready` deltaP `3.1188` edge `0.002` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
