# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T13:22:19.490126+00:00`
- Price records: `672`
- Market context records: `2461`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9224`

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

- `news_risk_high->crypto_alt_24h` score `21.3498` n `35` status `ready` deltaP `45.4068` edge `1.5353` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `21.0352` n `35` status `ready` deltaP `55.6498` edge `1.4259` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `17.9702` n `35` status `ready` deltaP `29.261` edge `1.3339` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8101` n `35` status `ready` deltaP `20.4663` edge `0.9058` maxDD `-3.3119`
- `news_risk_high->index_24h` score `8.251` n `35` status `ready` deltaP `24.3204` edge `0.5465` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.3412` n `35` status `ready` deltaP `24.3998` edge `0.4717` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8386` n `111` status `ready` deltaP `21.8515` edge `0.3737` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.0221` n `136` status `ready` deltaP `20.7406` edge `0.4648` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `4.0096` n `35` status `ready` deltaP `24.399` edge `0.2386` maxDD `-3.0367`
- `market_context_high->crypto_major_4h` score `3.9743` n `136` status `ready` deltaP `18.3285` edge `0.39` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.6607` n `35` status `ready` deltaP `37.0238` edge `0.0767` maxDD `-0.1442`
- `market_context_high->crypto_major_24h` score `2.4498` n `111` status `ready` deltaP `11.9464` edge `0.6237` maxDD `-25.1408`
- `news_risk_high->metal_4h` score `2.0221` n `35` status `ready` deltaP `9.7735` edge `0.3073` maxDD `-5.0567`
- `news_risk_high->fx_4h` score `1.8878` n `35` status `ready` deltaP `23.9417` edge `0.0161` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `1.6464` n `35` status `ready` deltaP `20.3807` edge `0.0445` maxDD `-1.4536`
- `market_context_high->unknown_4h` score `1.4105` n `136` status `ready` deltaP `9.3885` edge `0.157` maxDD `-3.4972`
- `news_risk_high->equity_4h` score `1.2372` n `35` status `ready` deltaP `-12.3693` edge `0.3385` maxDD `-3.7939`
- `market_context_high->index_24h` score `1.0691` n `111` status `ready` deltaP `5.7104` edge `0.1042` maxDD `-0.9209`
- `market_context_high->crypto_major_1h` score `0.8441` n `136` status `ready` deltaP `9.0833` edge `0.1292` maxDD `-4.2199`
- `news_risk_high->fx_1h` score `0.8032` n `35` status `ready` deltaP `11.9589` edge `0.0128` maxDD `-0.0473`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
