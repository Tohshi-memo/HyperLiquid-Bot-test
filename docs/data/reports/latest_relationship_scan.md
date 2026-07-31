# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T13:07:31.512689+00:00`
- Price records: `672`
- Market context records: `8517`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6277.9353` n `52` status `ready` deltaP `44.7383` edge `522.9051` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.535` n `64` status `ready` deltaP `21.1128` edge `0.3802` maxDD `-3.4427`
- `market_context_high->equity_4h` score `2.8651` n `33` status `ready` deltaP `27.8363` edge `0.0951` maxDD `-2.0202`
- `news_risk_high->index_4h` score `1.9855` n `64` status `ready` deltaP `16.5015` edge `0.0745` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7685` n `64` status `ready` deltaP `16.1022` edge `0.0877` maxDD `-2.4803`
- `market_context_high->crypto_major_4h` score `1.0742` n `33` status `ready` deltaP `8.472` edge `0.1546` maxDD `-2.8692`
- `market_context_high->crypto_alt_4h` score `1.0544` n `33` status `ready` deltaP `12.2829` edge `0.1281` maxDD `-3.9846`
- `news_risk_high->crypto_major_4h` score `0.8361` n `64` status `ready` deltaP `5.6784` edge `0.1469` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7701` n `64` status `ready` deltaP `14.1768` edge `0.1434` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5396` n `64` status `ready` deltaP `9.1598` edge `0.0608` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3096` n `64` status `ready` deltaP `6.4652` edge `0.0478` maxDD `-2.0972`
- `market_context_high->fx_4h` score `0.1874` n `33` status `ready` deltaP `8.0885` edge `0.0196` maxDD `-0.2932`
- `market_context_high->metal_4h` score `0.1642` n `33` status `ready` deltaP `13.7519` edge `-0.0121` maxDD `-1.3493`
- `market_context_high->index_4h` score `0.1414` n `33` status `ready` deltaP `6.6057` edge `0.0085` maxDD `-0.4196`
- `news_risk_high->fx_1h` score `0.0768` n `64` status `ready` deltaP `5.1366` edge `0.0037` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0652` n `64` status `ready` deltaP `4.6688` edge `0.0089` maxDD `-0.5338`
- `market_context_high->commodity_1h` score `0.0262` n `45` status `ready` deltaP `7.8011` edge `0.0139` maxDD `-2.0038`
- `news_risk_high->fx_4h` score `-0.0098` n `64` status `ready` deltaP `11.1662` edge `0.0205` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.0145` n `64` status `ready` deltaP `1.8674` edge `0.0333` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1311` n `64` status `ready` deltaP `3.256` edge `0.0077` maxDD `-0.5599`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
