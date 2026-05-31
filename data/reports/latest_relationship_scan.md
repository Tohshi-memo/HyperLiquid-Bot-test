# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T12:07:23.280325+00:00`
- Price records: `672`
- Market context records: `2455`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `20.3212` n `40` status `ready` deltaP `45.7639` edge `1.4472` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.9264` n `40` status `ready` deltaP `55.1389` edge `1.3369` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.7728` n `40` status `ready` deltaP `29.6181` edge `1.1484` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.2226` n `40` status `ready` deltaP `19.0278` edge `0.7831` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.4946` n `40` status `ready` deltaP `24.7569` edge `0.4821` maxDD `-1.4744`
- `news_risk_high->index_24h` score `6.1931` n `40` status `ready` deltaP `14.8611` edge `0.4464` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.7891` n `110` status `ready` deltaP `21.8024` edge `0.3699` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.3895` n `131` status `ready` deltaP `20.3837` edge `0.4109` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.2545` n `131` status `ready` deltaP `20.9912` edge `0.4825` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.4855` n `40` status `ready` deltaP `36.3194` edge `0.0668` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1355` n `40` status `ready` deltaP `27.2561` edge `0.2874` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.4899` n `110` status `ready` deltaP `11.9823` edge `0.6286` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.0566` n `40` status `ready` deltaP `26.0366` edge `0.0162` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `2.003` n `40` status `ready` deltaP `23.3533` edge `0.0544` maxDD `-1.4536`
- `news_risk_high->unknown_4h` score `1.7402` n `40` status `ready` deltaP `15.3963` edge `0.1147` maxDD `-2.7857`
- `market_context_high->unknown_4h` score `1.6602` n `131` status `ready` deltaP `10.1482` edge `0.1629` maxDD `-2.7098`
- `market_context_high->index_24h` score `1.2305` n `110` status `ready` deltaP `6.2247` edge `0.1075` maxDD `-0.7163`
- `market_context_high->crypto_major_1h` score `0.8657` n `136` status `ready` deltaP `9.233` edge `0.13` maxDD `-4.2199`
- `news_risk_high->fx_1h` score `0.7571` n `40` status `ready` deltaP `11.6018` edge `0.0114` maxDD `-0.0524`
- `market_context_high->crypto_alt_1h` score `0.6996` n `136` status `ready` deltaP `7.6259` edge `0.1262` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
