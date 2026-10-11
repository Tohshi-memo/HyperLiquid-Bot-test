# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T15:37:27.788337+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7312`

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

- `market_context_high->unknown_24h` score `1381.5097` n `40` status `ready` deltaP `-19.4444` edge `115.2918` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `54.2498` n `74` status `ready` deltaP `-7.7291` edge `4.6304` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `12.8038` n `83` status `ready` deltaP `-4.9347` edge `1.1335` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.8833` n `40` status `ready` deltaP `28.1944` edge `0.5952` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4297` n `40` status `ready` deltaP `52.9514` edge `0.1828` maxDD `0.0`
- `market_context_high->fx_24h` score `3.4471` n `40` status `ready` deltaP `38.8542` edge `0.0412` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6585` n `40` status `ready` deltaP `-20.5903` edge `0.5903` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.9734` n `74` status `ready` deltaP `15.0874` edge `0.0089` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.6304` n `74` status `ready` deltaP `13.3899` edge `0.0166` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `0.0717` n `83` status `ready` deltaP `4.8445` edge `0.0771` maxDD `-4.9401`
- `market_context_high->commodity_1h` score `-0.0437` n `83` status `ready` deltaP `3.0337` edge `0.0045` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.0545` n `83` status `ready` deltaP `2.7415` edge `0.0014` maxDD `-0.271`
- `market_context_high->metal_4h` score `-0.3235` n `74` status `ready` deltaP `1.6356` edge `0.0199` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.4105` n `83` status `ready` deltaP `3.3259` edge `0.0025` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.4755` n `83` status `ready` deltaP `-0.4455` edge `0.0309` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.9691` n `74` status `ready` deltaP `-8.2812` edge `0.001` maxDD `-0.9364`
- `market_context_high->equity_1h` score `-1.2336` n `83` status `ready` deltaP `-9.4491` edge `-0.0082` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.2417` n `83` status `ready` deltaP `-5.2648` edge `-0.0033` maxDD `-0.5392`
- `market_context_high->crypto_major_4h` score `-1.3211` n `74` status `ready` deltaP `-6.1058` edge `0.0819` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-1.8663` n `74` status `ready` deltaP `-8.7797` edge `0.0751` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
