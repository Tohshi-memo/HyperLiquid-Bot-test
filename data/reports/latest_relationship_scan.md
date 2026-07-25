# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T15:16:46.647340+00:00`
- Price records: `672`
- Market context records: `7890`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14713`

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

- `market_context_high->equity_24h` score `14.2923` n `107` status `ready` deltaP `30.0459` edge `1.1249` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.9255` n `108` status `ready` deltaP `15.2361` edge `0.4065` maxDD `-5.1426`
- `market_context_high->metal_24h` score `4.7558` n `107` status `ready` deltaP `23.662` edge `0.317` maxDD `-0.608`
- `market_context_high->commodity_24h` score `1.7796` n `107` status `ready` deltaP `21.9375` edge `0.1604` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.6904` n `108` status `ready` deltaP `14.1425` edge `0.1583` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.5707` n `108` status `ready` deltaP `15.8549` edge `0.197` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.2511` n `107` status `ready` deltaP `33.099` edge `0.0485` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1867` n `113` status `ready` deltaP `13.2677` edge `0.0513` maxDD `-1.6021`
- `market_context_high->index_4h` score `0.9278` n `108` status `ready` deltaP `15.5414` edge `0.0607` maxDD `-0.9597`
- `market_context_high->equity_1h` score `0.8594` n `113` status `ready` deltaP `11.915` edge `0.1125` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.74` n `108` status `ready` deltaP `10.8184` edge `0.0489` maxDD `-1.0817`
- `market_context_high->metal_4h` score `0.7253` n `108` status `ready` deltaP `10.0964` edge `0.1012` maxDD `-0.979`
- `market_context_high->index_1h` score `0.5801` n `113` status `ready` deltaP `10.9278` edge `0.0185` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.4389` n `113` status `ready` deltaP `5.3296` edge `0.0443` maxDD `-1.4603`
- `market_context_high->index_24h` score `0.0919` n `107` status `ready` deltaP `1.2229` edge `0.122` maxDD `-1.4662`
- `market_context_high->metal_1h` score `-0.0814` n `113` status `ready` deltaP `3.5729` edge `0.0239` maxDD `-0.6936`
- `market_context_high->commodity_1h` score `-0.2499` n `113` status `ready` deltaP `3.3179` edge `0.0027` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.4633` n `113` status `ready` deltaP `0.0399` edge `-0.0004` maxDD `-0.4112`
- `market_context_high->fx_4h` score `-0.5744` n `108` status `ready` deltaP `2.0017` edge `0.0012` maxDD `-1.3885`
- `market_context_high->crypto_alt_24h` score `-1.7124` n `107` status `ready` deltaP `11.6095` edge `0.2326` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
