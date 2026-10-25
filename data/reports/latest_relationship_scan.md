# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T09:07:27.750266+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7910`

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

- `market_context_high->unknown_4h` score `38.8945` n `108` status `ready` deltaP `-0.9993` edge `3.2814` maxDD `-1.016`
- `market_context_high->unknown_1h` score `4.0296` n `114` status `ready` deltaP `4.3334` edge `0.3558` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `2.3326` n `43` status `ready` deltaP `16.8524` edge `0.3675` maxDD `-11.7971`
- `market_context_high->commodity_24h` score `0.9103` n `43` status `ready` deltaP `18.0313` edge `0.0874` maxDD `-3.6055`
- `market_context_high->crypto_major_24h` score `0.8911` n `43` status `ready` deltaP `8.624` edge `0.1227` maxDD `-5.8084`
- `market_context_high->fx_4h` score `0.0098` n `108` status `ready` deltaP `7.8308` edge `0.0089` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0814` n `114` status `ready` deltaP `3.2514` edge `0.0028` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.4978` n `114` status `ready` deltaP `-0.063` edge `0.009` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.582` n `114` status `ready` deltaP `5.2185` edge `-0.0041` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.637` n `114` status `ready` deltaP `-1.6914` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-0.6899` n `43` status `ready` deltaP `2.1762` edge `0.0064` maxDD `-1.0823`
- `market_context_high->commodity_4h` score `-0.8445` n `108` status `ready` deltaP `-2.5463` edge `0.0316` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3577` n `114` status `ready` deltaP `1.8621` edge `-0.0284` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8316` n `108` status `ready` deltaP `5.5612` edge `-0.0187` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.0952` n `108` status `ready` deltaP `-6.6565` edge `-0.0368` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.9177` n `43` status `ready` deltaP `-6.9161` edge `-0.0173` maxDD `-6.7121`
- `market_context_high->crypto_alt_1h` score `-3.0327` n `114` status `ready` deltaP `-1.8201` edge `-0.0532` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7468` n `114` status `ready` deltaP `0.105` edge `-0.0856` maxDD `-12.1865`
- `market_context_high->index_24h` score `-5.4235` n `43` status `ready` deltaP `-21.7822` edge `-0.1766` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-6.2064` n `108` status `ready` deltaP `-11.145` edge `-0.2217` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
