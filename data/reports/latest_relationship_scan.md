# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T22:22:30.276333+00:00`
- Price records: `672`
- Market context records: `7296`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.086` n `127` status `ready` deltaP `5.3415` edge `0.0023` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.582` n `127` status `ready` deltaP `-0.7342` edge `-0.0125` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.5898` n `127` status `ready` deltaP `-0.0943` edge `0.0289` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6849` n `127` status `ready` deltaP `3.7708` edge `0.0281` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.8645` n `125` status `ready` deltaP `5.2575` edge `0.0141` maxDD `-1.4649`
- `market_context_high->fx_24h` score `-0.9321` n `121` status `ready` deltaP `0.2832` edge `0.0014` maxDD `-2.1564`
- `market_context_high->commodity_4h` score `-1.0918` n `125` status `ready` deltaP `2.5431` edge `-0.0111` maxDD `-2.4139`
- `market_context_high->unknown_1h` score `-1.2703` n `127` status `ready` deltaP `-0.0613` edge `-0.1001` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-1.3394` n `125` status `ready` deltaP `5.7378` edge `0.086` maxDD `-6.2031`
- `market_context_high->index_1h` score `-1.3675` n `127` status `ready` deltaP `-6.0119` edge `-0.0095` maxDD `-2.1503`
- `market_context_high->metal_1h` score `-2.1492` n `127` status `ready` deltaP `-9.7376` edge `-0.0038` maxDD `-1.4971`
- `market_context_high->metal_4h` score `-2.4668` n `125` status `ready` deltaP `-9.6159` edge `-0.0066` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-3.0943` n `121` status `ready` deltaP `-6.0582` edge `-0.1377` maxDD `-2.3815`
- `market_context_high->crypto_major_4h` score `-3.1469` n `125` status `ready` deltaP `0.972` edge `-0.0205` maxDD `-23.4879`
- `market_context_high->crypto_alt_4h` score `-3.4068` n `125` status `ready` deltaP `0.5549` edge `-0.0133` maxDD `-15.2776`
- `market_context_high->equity_1h` score `-4.5394` n `127` status `ready` deltaP `-9.9489` edge `-0.0704` maxDD `-14.6578`
- `market_context_high->index_4h` score `-5.124` n `125` status `ready` deltaP `-14.8489` edge `-0.061` maxDD `-11.0273`
- `market_context_high->unknown_24h` score `-5.4021` n `122` status `ready` deltaP `-9.5856` edge `-0.0481` maxDD `-15.0539`
- `market_context_high->metal_24h` score `-11.2174` n `122` status `ready` deltaP `-29.0443` edge `-0.1302` maxDD `-22.2099`
- `market_context_high->index_24h` score `-13.3708` n `121` status `ready` deltaP `-29.8685` edge `-0.169` maxDD `-35.0222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
