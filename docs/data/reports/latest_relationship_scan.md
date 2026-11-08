# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T10:52:26.458543+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4713`

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

- `market_context_high->unknown_4h` score `104.0542` n `37` status `ready` deltaP `-3.9387` edge `8.7422` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.2565` n `35` status `ready` deltaP `12.6339` edge `0.7833` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.2808` n `37` status `ready` deltaP `10.6571` edge `0.2483` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1205` n `37` status `ready` deltaP `33.619` edge `0.0449` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.4248` n `40` status `ready` deltaP `29.0244` edge `0.0171` maxDD `-0.016`
- `market_context_high->index_4h` score `2.056` n `37` status `ready` deltaP `26.8128` edge `0.0396` maxDD `-2.4279`
- `market_context_high->crypto_major_1h` score `0.8598` n `37` status `ready` deltaP `10.3496` edge `0.0612` maxDD `-3.0172`
- `news_risk_high->fx_24h` score `0.8387` n `37` status `ready` deltaP `2.8341` edge `0.0731` maxDD `-0.1014`
- `market_context_high->index_24h` score `0.7049` n `35` status `ready` deltaP `8.6904` edge `0.0955` maxDD `-2.7123`
- `market_context_high->commodity_24h` score `0.6132` n `35` status `ready` deltaP `5.3422` edge `0.1625` maxDD `-6.5601`
- `market_context_high->crypto_alt_1h` score `0.5714` n `37` status `ready` deltaP `12.4454` edge `0.0718` maxDD `-3.1881`
- `market_context_high->fx_24h` score `0.5581` n `35` status `ready` deltaP `9.8611` edge `-0.0104` maxDD `-0.0397`
- `news_risk_high->fx_1h` score `0.4961` n `40` status `ready` deltaP `11.8114` edge `0.0064` maxDD `-0.0567`
- `market_context_high->fx_1h` score `0.3727` n `37` status `ready` deltaP `6.4736` edge `0.015` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.3105` n `37` status `ready` deltaP `2.0999` edge `0.0389` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1109` n `37` status `ready` deltaP `8.8688` edge `0.0097` maxDD `-1.7019`
- `news_risk_high->index_1h` score `0.0941` n `40` status `ready` deltaP `8.2485` edge `0.0024` maxDD `-0.2931`
- `news_risk_high->index_4h` score `-0.0495` n `40` status `ready` deltaP `3.2317` edge `0.02` maxDD `-0.4975`
- `market_context_high->metal_1h` score `-0.0552` n `37` status `ready` deltaP `1.3514` edge `0.0167` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.0607` n `37` status `ready` deltaP `2.2248` edge `0.0228` maxDD `-1.633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
