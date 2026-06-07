# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-07T07:37:27.499435+00:00`
- Price records: `672`
- Market context records: `3157`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8852`

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

- `market_context_high->commodity_24h` score `14.0198` n `108` status `ready` deltaP `47.5115` edge `0.8944` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `12.131` n `108` status `ready` deltaP `14.8149` edge `2.4541` maxDD `-71.142`
- `market_context_high->unknown_24h` score `11.8454` n `108` status `ready` deltaP `21.9328` edge `0.8897` maxDD `-1.9039`
- `market_context_high->index_24h` score `6.5172` n `108` status `ready` deltaP `31.0185` edge `0.8842` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.9223` n `108` status `ready` deltaP `12.6736` edge `1.3882` maxDD `-53.663`
- `market_context_high->commodity_4h` score `2.9005` n `141` status `ready` deltaP `18.7813` edge `0.1623` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.1797` n `141` status `ready` deltaP `4.3105` edge `0.0285` maxDD `-1.7142`
- `market_context_high->fx_24h` score `0.1171` n `108` status `ready` deltaP `9.0278` edge `0.0015` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.4036` n `141` status `ready` deltaP `5.8075` edge `0.1225` maxDD `-14.7034`
- `market_context_high->index_1h` score `-0.5167` n `141` status `ready` deltaP `3.6799` edge `0.0155` maxDD `-4.5023`
- `market_context_high->equity_1h` score `-0.9381` n `141` status `ready` deltaP `2.3718` edge `0.0125` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.0552` n `141` status `ready` deltaP `2.3867` edge `0.0751` maxDD `-15.1032`
- `market_context_high->fx_1h` score `-1.0938` n `141` status `ready` deltaP `-10.0161` edge `-0.0052` maxDD `-0.7941`
- `market_context_high->index_4h` score `-1.1183` n `141` status `ready` deltaP `12.7097` edge `0.0628` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.1584` n `141` status `ready` deltaP `8.0836` edge `0.0718` maxDD `-14.7778`
- `market_context_high->fx_4h` score `-1.4301` n `141` status `ready` deltaP `-13.0611` edge `-0.0078` maxDD `-1.4115`
- `market_context_high->metal_1h` score `-2.1481` n `141` status `ready` deltaP `-4.9412` edge `-0.0067` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-2.9215` n `141` status `ready` deltaP `19.3835` edge `0.4318` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-2.923` n `141` status `ready` deltaP `13.1735` edge `0.068` maxDD `-36.7784`
- `market_context_high->unknown_1h` score `-3.2779` n `141` status `ready` deltaP `1.7975` edge `-0.0825` maxDD `-14.2111`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
