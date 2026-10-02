# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T07:22:31.520869+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5024`

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

- `market_context_high->unknown_1h` score `340.7628` n `50` status `ready` deltaP `9.6766` edge `28.3373` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.4293` n `50` status `ready` deltaP `8.8415` edge `23.8935` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.6159` n `61` status `ready` deltaP `39.256` edge `0.8939` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0543` n `50` status `ready` deltaP `36.1667` edge `0.8217` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.1384` n `61` status `ready` deltaP `36.6917` edge `0.5654` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.8089` n `50` status `ready` deltaP `16.5347` edge `0.7948` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.8629` n `50` status `ready` deltaP `17.5427` edge `0.5253` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8665` n `50` status `ready` deltaP `15.5793` edge `0.431` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.7212` n `90` status `ready` deltaP `14.4682` edge `0.348` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.0768` n `50` status `ready` deltaP `14.5278` edge `0.4838` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9105` n `50` status `ready` deltaP `32.689` edge `0.0381` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8582` n `50` status `ready` deltaP `13.7545` edge `0.2128` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8177` n `50` status `ready` deltaP `13.7006` edge `0.1885` maxDD `-2.2692`
- `market_context_high->fx_1h` score `1.4627` n `50` status `ready` deltaP `20.491` edge `0.0117` maxDD `-0.113`
- `news_risk_high->equity_4h` score `1.309` n `90` status `ready` deltaP `22.1578` edge `0.0897` maxDD `-2.9013`
- `market_context_high->index_24h` score `1.0178` n `50` status `ready` deltaP `16.1806` edge `0.0797` maxDD `-1.2338`
- `news_risk_high->commodity_24h` score `0.8672` n `61` status `ready` deltaP `17.1761` edge `0.1127` maxDD `-4.2822`
- `news_risk_high->crypto_alt_1h` score `0.6472` n `102` status `ready` deltaP `4.6172` edge `0.0794` maxDD `-2.4998`
- `news_risk_high->metal_24h` score `0.642` n `61` status `ready` deltaP `1.2295` edge `0.1727` maxDD `-2.192`
- `market_context_high->fx_24h` score `0.5063` n `50` status `ready` deltaP `14.4306` edge `0.0705` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
