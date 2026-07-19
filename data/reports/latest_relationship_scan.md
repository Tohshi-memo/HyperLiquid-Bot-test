# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T18:42:38.288109+00:00`
- Price records: `672`
- Market context records: `7279`
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

- `market_context_high->fx_1h` score `-0.175` n `136` status `ready` deltaP `3.8112` edge `0.0011` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.7184` n `136` status `ready` deltaP `-0.4227` edge `0.0146` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.8911` n `136` status `ready` deltaP `2.0562` edge `0.0131` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.9197` n `133` status `ready` deltaP `4.5549` edge `0.0117` maxDD `-1.4649`
- `market_context_high->unknown_4h` score `-1.0845` n `133` status `ready` deltaP `8.6386` edge `0.0879` maxDD `-6.2026`
- `market_context_high->commodity_1h` score `-1.2001` n `136` status `ready` deltaP `-3.2879` edge `-0.016` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-1.2862` n `136` status `ready` deltaP `-0.9819` edge `-0.096` maxDD `-1.3212`
- `market_context_high->index_1h` score `-1.371` n `136` status `ready` deltaP `-5.6085` edge `-0.0096` maxDD `-2.3805`
- `market_context_high->commodity_4h` score `-1.5729` n `133` status `ready` deltaP `-1.1014` edge `-0.0202` maxDD `-2.9494`
- `market_context_high->fx_24h` score `-1.8433` n `126` status `ready` deltaP `-3.9034` edge `-0.0048` maxDD `-2.1564`
- `market_context_high->metal_1h` score `-2.2565` n `136` status `ready` deltaP `-9.779` edge `-0.007` maxDD `-1.9343`
- `market_context_high->commodity_24h` score `-2.3889` n `126` status `ready` deltaP `-2.3105` edge `-0.1039` maxDD `-2.3815`
- `market_context_high->metal_4h` score `-4.1833` n `133` status `ready` deltaP `-12.272` edge `-0.0197` maxDD `-4.7674`
- `market_context_high->equity_1h` score `-4.4828` n `136` status `ready` deltaP `-8.2494` edge `-0.0659` maxDD `-15.5469`
- `market_context_high->crypto_alt_4h` score `-5.4011` n `133` status `ready` deltaP `-2.6809` edge `-0.0573` maxDD `-22.9937`
- `market_context_high->index_4h` score `-5.5578` n `133` status `ready` deltaP `-16.6126` edge `-0.0654` maxDD `-12.6266`
- `market_context_high->crypto_major_4h` score `-5.7526` n `133` status `ready` deltaP `-2.9055` edge `-0.0634` maxDD `-24.0621`
- `market_context_high->unknown_24h` score `-6.4897` n `127` status `ready` deltaP `-14.0461` edge `-0.0654` maxDD `-18.5414`
- `market_context_high->metal_24h` score `-12.7718` n `127` status `ready` deltaP `-32.8194` edge `-0.1579` maxDD `-28.3428`
- `market_context_high->index_24h` score `-15.2386` n `126` status `ready` deltaP `-29.619` edge `-0.1955` maxDD `-41.8204`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
