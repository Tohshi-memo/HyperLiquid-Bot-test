# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T00:07:28.460509+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_1h` score `2.3202` n `34` status `ready` deltaP `29.2005` edge `0.0105` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.8011` n `136` status `ready` deltaP `6.4064` edge `0.1301` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.7212` n `34` status `ready` deltaP `22.8778` edge `0.0079` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.3426` n `136` status `ready` deltaP `20.8035` edge `-0.0013` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.9441` n `34` status `ready` deltaP `20.3857` edge `0.0133` maxDD `-0.9204`
- `news_risk_high->commodity_1h` score `0.8469` n `34` status `ready` deltaP `20.236` edge `-0.008` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1468` n `136` status `ready` deltaP `8.9939` edge `0.0091` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0599` n `136` status `ready` deltaP `6.1818` edge `0.0042` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1258` n `136` status `ready` deltaP `2.2896` edge `0.0045` maxDD `-0.2043`
- `news_risk_high->metal_1h` score `-0.3011` n `34` status `ready` deltaP `-1.0479` edge `-0.0093` maxDD `-0.1184`
- `market_context_high->equity_1h` score `-0.3567` n `136` status `ready` deltaP `4.2092` edge `0.0332` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4362` n `136` status `ready` deltaP `6.3218` edge `-0.0169` maxDD `-1.5942`
- `news_risk_high->crypto_major_1h` score `-0.4993` n `34` status `ready` deltaP `9.713` edge `-0.041` maxDD `-5.0209`
- `market_context_high->metal_1h` score `-0.5849` n `136` status `ready` deltaP `-0.3126` edge `-0.0048` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.646` n `136` status `ready` deltaP `1.5513` edge `0.0104` maxDD `-2.618`
- `news_risk_high->index_1h` score `-0.7156` n `34` status `ready` deltaP `-8.5241` edge `0.0004` maxDD `-0.1583`
- `market_context_high->fx_24h` score `-0.8711` n `120` status `ready` deltaP `0.9722` edge `0.0082` maxDD `-2.1085`
- `market_context_high->commodity_4h` score `-1.0453` n `136` status `ready` deltaP `-7.048` edge `-0.002` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0792` n `136` status `ready` deltaP `-7.7052` edge `-0.0022` maxDD `-1.1164`
- `market_context_high->crypto_alt_4h` score `-1.2429` n `136` status `ready` deltaP `8.1062` edge `-0.0108` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
