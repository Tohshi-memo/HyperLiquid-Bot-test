# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T08:07:29.252921+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4872`

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

- `market_context_high->unknown_1h` score `340.7051` n `50` status `ready` deltaP `9.8263` edge `28.3315` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.2493` n `50` status `ready` deltaP `8.8415` edge `23.8785` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.9786` n `64` status `ready` deltaP `39.4097` edge `0.9231` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.9955` n `50` status `ready` deltaP `36.1667` edge `0.8168` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.4252` n `64` status `ready` deltaP `36.6319` edge `0.5897` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.9505` n `50` status `ready` deltaP `16.5347` edge `0.8066` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9325` n `50` status `ready` deltaP `17.5427` edge `0.5311` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9325` n `50` status `ready` deltaP `15.5793` edge `0.4365` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.1435` n `93` status `ready` deltaP `15.4718` edge `0.3765` maxDD `-6.4152`
- `market_context_high->equity_24h` score `2.9873` n `50` status `ready` deltaP `14.0069` edge `0.4758` maxDD `-11.8957`
- `market_context_high->crypto_alt_1h` score `2.9253` n `50` status `ready` deltaP `13.9042` edge `0.2174` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9153` n `50` status `ready` deltaP `32.689` edge `0.0385` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8848` n `50` status `ready` deltaP `14.0` edge `0.1921` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.1878` n `93` status `ready` deltaP `22.9822` edge `0.0987` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4651` n `50` status `ready` deltaP `20.491` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.0314` n `64` status `ready` deltaP `4.6875` edge `0.1821` maxDD `-2.192`
- `market_context_high->index_24h` score `1.0115` n `50` status `ready` deltaP `16.1806` edge `0.0789` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.7416` n `105` status `ready` deltaP `5.0471` edge `0.0844` maxDD `-2.4998`
- `market_context_high->fx_24h` score `0.518` n `50` status `ready` deltaP `14.4306` edge `0.072` maxDD `-1.8102`
- `news_risk_high->crypto_major_4h` score `0.5113` n `93` status `ready` deltaP `7.6072` edge `0.2458` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
