# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T04:52:29.286934+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6662`

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

- `market_context_high->unknown_1h` score `340.842` n `50` status `ready` deltaP `9.5269` edge `28.3449` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0775` n `50` status `ready` deltaP `8.9939` edge `23.9465` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.9312` n `67` status `ready` deltaP `39.2024` edge `1.0872` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0771` n `50` status `ready` deltaP `36.1667` edge `0.8236` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `8.1319` n `50` status `ready` deltaP `16.1875` edge `0.7407` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `7.0854` n `67` status `ready` deltaP `28.5137` edge `0.4901` maxDD `-3.8462`
- `market_context_high->crypto_major_4h` score `6.8821` n `50` status `ready` deltaP `17.5427` edge `0.5269` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7729` n `50` status `ready` deltaP `15.5793` edge `0.4232` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.5166` n `87` status `ready` deltaP `13.3954` edge `0.3381` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.2457` n `50` status `ready` deltaP `15.9167` edge `0.4962` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9021` n `50` status `ready` deltaP `32.689` edge `0.0374` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.7961` n `50` status `ready` deltaP `13.5509` edge `0.1877` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.7815` n `50` status `ready` deltaP `13.1557` edge `0.2104` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.0441` n `87` status `ready` deltaP `21.2766` edge `0.0981` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.2166` n `67` status `ready` deltaP `20.8463` edge `0.1294` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9323` n `50` status `ready` deltaP `14.7917` edge `0.078` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.836` n `99` status `ready` deltaP `6.7517` edge `0.0809` maxDD `-2.4998`
- `news_risk_high->metal_24h` score `0.8278` n `67` status `ready` deltaP `6.2733` edge `0.1917` maxDD `-2.192`
- `news_risk_high->index_24h` score `0.6803` n `67` status `ready` deltaP `11.9559` edge `0.0248` maxDD `-0.4916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
