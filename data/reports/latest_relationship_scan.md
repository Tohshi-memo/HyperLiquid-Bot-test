# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T04:37:22.864066+00:00`
- Price records: `672`
- Market context records: `2629`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.5282` n `146` status `ready` deltaP `18.2958` edge `0.5382` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.1515` n `146` status `ready` deltaP `25.3488` edge `0.5282` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.3471` n `146` status `ready` deltaP `14.7636` edge `0.3615` maxDD `-10.1468`
- `market_context_high->index_24h` score `1.4005` n `146` status `ready` deltaP `11.2324` edge `0.1399` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.1829` n `146` status `ready` deltaP `10.6821` edge `0.1461` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `0.9951` n `146` status `ready` deltaP `7.3797` edge `0.1387` maxDD `-3.7312`
- `market_context_high->crypto_alt_24h` score `0.6919` n `146` status `ready` deltaP `2.7588` edge `0.6771` maxDD `-39.0265`
- `market_context_high->crypto_major_1h` score `0.6369` n `146` status `ready` deltaP `8.5637` edge `0.1154` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.3946` n `146` status `ready` deltaP `9.8898` edge `0.0511` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0868` n `146` status `ready` deltaP `4.3905` edge `0.0129` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.2804` n `146` status `ready` deltaP `6.4002` edge `0.0218` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4236` n `146` status `ready` deltaP `1.9502` edge `0.018` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.7556` n `146` status `ready` deltaP `0.6624` edge `0.0074` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7575` n `146` status `ready` deltaP `-1.8825` edge `0.0029` maxDD `-0.278`
- `market_context_high->commodity_4h` score `-0.8365` n `146` status `ready` deltaP `5.778` edge `0.0485` maxDD `-10.2078`
- `market_context_high->equity_1h` score `-0.9211` n `146` status `ready` deltaP `-1.1258` edge `0.0146` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-1.0881` n `146` status `ready` deltaP `1.9786` edge `-0.0045` maxDD `-1.6157`
- `market_context_high->metal_4h` score `-1.1119` n `146` status `ready` deltaP `2.368` edge `0.0303` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-1.1137` n `146` status `ready` deltaP `-2.3597` edge `0.0087` maxDD `-0.8621`
- `market_context_high->equity_4h` score `-1.3458` n `146` status `ready` deltaP `1.6497` edge `0.0173` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
