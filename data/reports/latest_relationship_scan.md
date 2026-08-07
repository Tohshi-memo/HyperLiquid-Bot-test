# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T15:52:27.470108+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11757`

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

- `market_context_high->metal_24h` score `2.0519` n `106` status `ready` deltaP `7.7826` edge `0.1767` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.7483` n `121` status `ready` deltaP `10.9294` edge `0.0311` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4723` n `106` status `ready` deltaP `20.1321` edge `0.0445` maxDD `-4.1196`
- `market_context_high->commodity_4h` score `0.3569` n `109` status `ready` deltaP `10.2428` edge `0.0621` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.0197` n `121` status `ready` deltaP `7.8512` edge `-0.0041` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.2172` n `109` status `ready` deltaP `7.0163` edge `0.0007` maxDD `-1.6928`
- `market_context_high->index_24h` score `-0.3524` n `106` status `ready` deltaP `2.421` edge `0.1058` maxDD `-5.7715`
- `market_context_high->metal_1h` score `-0.476` n `121` status `ready` deltaP `-2.1972` edge `-0.0071` maxDD `-1.1422`
- `market_context_high->metal_4h` score `-0.741` n `109` status `ready` deltaP `2.1748` edge `0.004` maxDD `-1.4197`
- `market_context_high->crypto_alt_1h` score `-0.9076` n `121` status `ready` deltaP `-5.8866` edge `-0.0142` maxDD `-2.3669`
- `market_context_high->index_1h` score `-0.9836` n `121` status `ready` deltaP `-2.5746` edge `-0.0114` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.3011` n `121` status `ready` deltaP `3.5941` edge `-0.0343` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.8329` n `109` status `ready` deltaP `1.3874` edge `-0.023` maxDD `-5.7857`
- `market_context_high->index_4h` score `-1.9765` n `109` status `ready` deltaP `-3.9648` edge `-0.0261` maxDD `-3.9739`
- `market_context_high->crypto_major_1h` score `-2.6081` n `121` status `ready` deltaP `-6.7254` edge `-0.0428` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-3.9767` n `106` status `ready` deltaP `-11.7727` edge `-0.1086` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.8483` n `109` status `ready` deltaP `-7.6485` edge `-0.1822` maxDD `-24.7379`
- `market_context_high->crypto_major_24h` score `-5.454` n `106` status `ready` deltaP `-4.077` edge `-0.262` maxDD `-24.1374`
- `market_context_high->equity_24h` score `-6.3014` n `106` status `ready` deltaP `-9.1368` edge `0.1761` maxDD `-42.5578`
- `market_context_high->equity_4h` score `-8.0559` n `109` status `ready` deltaP `2.4656` edge `-0.2352` maxDD `-31.2053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
