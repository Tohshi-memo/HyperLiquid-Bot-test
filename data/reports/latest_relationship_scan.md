# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T17:37:46.233896+00:00`
- Price records: `672`
- Market context records: `4643`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9996`

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

- `market_context_high->unknown_1h` score `70.1207` n `146` status `ready` deltaP `8.9082` edge `5.8299` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.9017` n `146` status `ready` deltaP `10.038` edge `0.4626` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `-0.1549` n `146` status `ready` deltaP `5.8695` edge `0.0403` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3497` n `146` status `ready` deltaP `2.9489` edge `0.0308` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5816` n `146` status `ready` deltaP `-2.2496` edge `-0.0041` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.6994` n `146` status `ready` deltaP `2.5163` edge `0.0018` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.7292` n `146` status `ready` deltaP `-1.0479` edge `0.0122` maxDD `-5.5624`
- `market_context_high->index_4h` score `-0.7934` n `146` status `ready` deltaP `2.9632` edge `-0.0092` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1085` n `146` status `ready` deltaP `5.4961` edge `0.032` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2173` n `146` status `ready` deltaP `0.9835` edge `0.0143` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.7059` n `146` status `ready` deltaP `-4.3639` edge `-0.0122` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.926` n `146` status `ready` deltaP `-4.0911` edge `-0.0827` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-4.9905` n `146` status `ready` deltaP `-8.5117` edge `-0.0079` maxDD `-6.0982`
- `market_context_high->commodity_24h` score `-5.1745` n `146` status `ready` deltaP `11.2847` edge `0.044` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.2321` n `146` status `ready` deltaP `-1.3473` edge `-0.0983` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.4722` n `146` status `ready` deltaP `-4.7945` edge `-0.1321` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.6854` n `146` status `ready` deltaP `-7.0895` edge `-0.0557` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.3388` n `146` status `ready` deltaP `-1.5244` edge `-0.1932` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.8833` n `146` status `ready` deltaP `-4.8613` edge `-0.3133` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-11.4599` n `146` status `ready` deltaP `-3.5771` edge `-0.351` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
