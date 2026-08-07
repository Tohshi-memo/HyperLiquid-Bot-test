# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T13:37:30.623518+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11740`

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

- `market_context_high->commodity_4h` score `1.05` n `116` status `ready` deltaP `12.6788` edge `0.0876` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.7735` n `121` status `ready` deltaP `10.9294` edge `0.0332` maxDD `-1.3282`
- `market_context_high->metal_24h` score `0.7412` n `110` status `ready` deltaP `1.7939` edge `0.1449` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.5545` n `110` status `ready` deltaP `21.1018` edge `0.0495` maxDD `-4.1933`
- `market_context_high->fx_1h` score `0.0317` n `121` status `ready` deltaP `7.8512` edge `-0.0031` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.1753` n `116` status `ready` deltaP `8.8835` edge `0.0043` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4672` n `121` status `ready` deltaP `-1.5205` edge `-0.0057` maxDD `-1.5253`
- `market_context_high->index_1h` score `-0.58` n `121` status `ready` deltaP `-1.8978` edge `-0.0083` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.1302` n `121` status `ready` deltaP `4.2708` edge `-0.0169` maxDD `-10.5179`
- `market_context_high->index_24h` score `-1.3014` n `110` status `ready` deltaP `-0.3233` edge `0.0809` maxDD `-6.6423`
- `market_context_high->crypto_alt_1h` score `-1.4229` n `121` status `ready` deltaP `-4.5331` edge `-0.0173` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-1.4461` n `116` status `ready` deltaP `-1.6452` edge `-0.0097` maxDD `-2.654`
- `market_context_high->index_4h` score `-1.5706` n `116` status `ready` deltaP `-6.9018` edge `-0.0308` maxDD `-4.6306`
- `market_context_high->crypto_major_1h` score `-1.6089` n `121` status `ready` deltaP `-5.3719` edge `-0.0369` maxDD `-7.3514`
- `market_context_high->crypto_alt_4h` score `-2.1345` n `116` status `ready` deltaP `0.3469` edge `-0.0412` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-3.825` n `110` status `ready` deltaP `-10.821` edge `-0.1023` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.2021` n `116` status `ready` deltaP `-0.9252` edge `-0.2601` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.224` n `110` status `ready` deltaP `10.2853` edge `0.01` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.5773` n `116` status `ready` deltaP `-7.5536` edge `-0.1788` maxDD `-25.8493`
- `market_context_high->crypto_major_24h` score `-7.7597` n `110` status `ready` deltaP `-8.839` edge `-0.3512` maxDD `-35.1095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
