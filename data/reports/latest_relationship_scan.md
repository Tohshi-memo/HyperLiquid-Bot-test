# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T12:37:21.147201+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9825`

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

- `market_context_high->equity_24h` score `4.0048` n `103` status `ready` deltaP `4.5729` edge `0.6193` maxDD `-21.9512`
- `market_context_high->metal_24h` score `3.5881` n `103` status `ready` deltaP `10.9965` edge `0.2986` maxDD `-3.4989`
- `market_context_high->commodity_4h` score `1.1697` n `143` status `ready` deltaP `14.2899` edge `0.0763` maxDD `-3.2603`
- `market_context_high->commodity_1h` score `0.8222` n `143` status `ready` deltaP `10.6916` edge `0.0334` maxDD `-0.8927`
- `market_context_high->fx_24h` score `0.7278` n `103` status `ready` deltaP `21.4013` edge `0.0373` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5304` n `103` status `ready` deltaP `8.0586` edge `0.1705` maxDD `-6.1647`
- `market_context_high->fx_1h` score `-0.3469` n `143` status `ready` deltaP `3.6965` edge `-0.004` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3552` n `143` status `ready` deltaP `-0.1957` edge `-0.0049` maxDD `-0.8134`
- `market_context_high->fx_4h` score `-0.5309` n `143` status `ready` deltaP `5.2182` edge `-0.0037` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7159` n `143` status `ready` deltaP `-3.9895` edge `-0.0091` maxDD `-1.4867`
- `market_context_high->index_4h` score `-0.7576` n `143` status `ready` deltaP `0.9136` edge `-0.0081` maxDD `-1.2232`
- `market_context_high->equity_1h` score `-0.9078` n `143` status `ready` deltaP `0.1121` edge `0.0086` maxDD `-4.8`
- `market_context_high->metal_4h` score `-1.1635` n `143` status `ready` deltaP `-0.5937` edge `-0.0259` maxDD `-4.2112`
- `market_context_high->crypto_alt_1h` score `-1.835` n `143` status `ready` deltaP `-9.5348` edge `-0.0249` maxDD `-2.4893`
- `market_context_high->equity_4h` score `-2.4105` n `143` status `ready` deltaP `0.4105` edge `-0.0662` maxDD `-7.9929`
- `market_context_high->crypto_major_1h` score `-3.3396` n `143` status `ready` deltaP `-10.2383` edge `-0.0649` maxDD `-8.2784`
- `market_context_high->crypto_alt_4h` score `-3.5562` n `143` status `ready` deltaP `-6.4473` edge `-0.087` maxDD `-6.6427`
- `market_context_high->crypto_major_24h` score `-4.2289` n `103` status `ready` deltaP `3.0947` edge `-0.0981` maxDD `-16.3283`
- `market_context_high->crypto_alt_24h` score `-5.8841` n `103` status `ready` deltaP `-16.2656` edge `-0.2371` maxDD `-4.5844`
- `market_context_high->unknown_1h` score `-7.589` n `143` status `ready` deltaP `-5.1956` edge `-0.5534` maxDD `-1.2171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
