# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T18:22:30.555448+00:00`
- Price records: `672`
- Market context records: `7277`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13791`

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

- `market_context_high->fx_1h` score `-0.2003` n `137` status `ready` deltaP `3.414` edge `0.0005` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.7074` n `137` status `ready` deltaP `-0.1967` edge `0.0145` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.8815` n `137` status `ready` deltaP `2.2553` edge `0.013` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.9379` n `134` status `ready` deltaP `4.3543` edge `0.0107` maxDD `-1.4649`
- `market_context_high->unknown_4h` score `-1.124` n `134` status `ready` deltaP `8.2795` edge `0.087` maxDD `-6.2026`
- `market_context_high->commodity_1h` score `-1.18` n `137` status `ready` deltaP `-3.0677` edge `-0.0158` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-1.3077` n `137` status `ready` deltaP `-1.32` edge `-0.0965` maxDD `-1.3212`
- `market_context_high->index_1h` score `-1.3933` n `137` status `ready` deltaP `-5.8876` edge `-0.0096` maxDD `-2.3805`
- `market_context_high->commodity_4h` score `-1.5627` n `134` status `ready` deltaP `-0.9289` edge `-0.0205` maxDD `-2.9494`
- `market_context_high->fx_24h` score `-1.9121` n `126` status `ready` deltaP `-4.5231` edge `-0.0064` maxDD `-2.1564`
- `market_context_high->metal_1h` score `-2.2764` n `137` status `ready` deltaP `-10.042` edge `-0.0069` maxDD `-1.9351`
- `market_context_high->commodity_24h` score `-2.2997` n `126` status `ready` deltaP `-1.6908` edge `-0.1006` maxDD `-2.3815`
- `market_context_high->metal_4h` score `-4.2021` n `134` status `ready` deltaP `-12.4796` edge `-0.0196` maxDD `-4.79`
- `market_context_high->equity_1h` score `-4.4474` n `137` status `ready` deltaP `-7.9273` edge `-0.0651` maxDD `-15.5469`
- `market_context_high->crypto_alt_4h` score `-5.5352` n `134` status `ready` deltaP `-2.9783` edge `-0.0587` maxDD `-23.2839`
- `market_context_high->index_4h` score `-5.5703` n `134` status `ready` deltaP `-16.7922` edge `-0.065` maxDD `-12.646`
- `market_context_high->crypto_major_4h` score `-5.8597` n `134` status `ready` deltaP `-3.2422` edge `-0.0655` maxDD `-24.4291`
- `market_context_high->unknown_24h` score `-6.536` n `127` status `ready` deltaP `-14.0461` edge `-0.0666` maxDD `-18.7542`
- `market_context_high->metal_24h` score `-12.906` n `127` status `ready` deltaP `-32.8194` edge `-0.1616` maxDD `-28.9418`
- `market_context_high->index_24h` score `-15.4175` n `126` status `ready` deltaP `-29.619` edge `-0.199` maxDD `-42.3996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
