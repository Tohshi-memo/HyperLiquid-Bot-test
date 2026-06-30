# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T20:07:30.071254+00:00`
- Price records: `672`
- Market context records: `5281`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `25.02` n `153` status `ready` deltaP `28.0331` edge `1.9071` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.4984` n `153` status `ready` deltaP `25.7353` edge `0.8683` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.2575` n `175` status `ready` deltaP `16.2116` edge `0.4108` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.931` n `175` status `ready` deltaP `15.8302` edge `0.4513` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.797` n `153` status `ready` deltaP `19.9653` edge `0.7462` maxDD `-40.0306`
- `market_context_high->equity_4h` score `0.9796` n `175` status `ready` deltaP `9.9591` edge `0.1791` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.7319` n `175` status `ready` deltaP `14.4921` edge `0.0666` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5685` n `153` status `ready` deltaP `13.3068` edge `0.0482` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5239` n `182` status `ready` deltaP `5.1918` edge `0.1052` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3202` n `182` status `ready` deltaP `6.1394` edge `0.1103` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2319` n `153` status `ready` deltaP `20.8231` edge `0.0544` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.1123` n `182` status `ready` deltaP `7.1972` edge `0.0579` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0125` n `182` status `ready` deltaP `6.0473` edge `0.0111` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2662` n `175` status `ready` deltaP `7.6368` edge `0.0267` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.337` n `182` status `ready` deltaP `3.045` edge `0.0108` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3471` n `182` status `ready` deltaP `0.6515` edge `0.0001` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.734` n `175` status `ready` deltaP `1.0819` edge `0.0016` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3624` n `182` status `ready` deltaP `-2.3475` edge `-0.0061` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.6758` n `175` status `ready` deltaP `-3.1795` edge `0.0067` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.5687` n `182` status `ready` deltaP `6.5984` edge `-0.1939` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
