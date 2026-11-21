# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T09:37:29.852705+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2680`

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

- `market_context_high->unknown_1h` score `10038.3773` n `126` status `ready` deltaP `1.0146` edge `836.5445` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6119.0745` n `126` status `ready` deltaP `-0.3145` edge `509.9555` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1657` n `126` status `ready` deltaP `4.5504` edge `0.0149` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2991` n `126` status `ready` deltaP `2.8585` edge `0.0038` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5131` n `126` status `ready` deltaP `11.7958` edge `0.0362` maxDD `-10.1161`
- `market_context_high->crypto_major_24h` score `-1.0341` n `112` status `ready` deltaP `24.38` edge `0.8743` maxDD `-85.5531`
- `market_context_high->fx_1h` score `-1.3998` n `126` status `ready` deltaP `-8.9559` edge `-0.001` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.8` n `126` status `ready` deltaP `6.1377` edge `0.015` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.882` n `126` status `ready` deltaP `-6.2693` edge `0.0021` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2032` n `126` status `ready` deltaP `-7.3235` edge `-0.0216` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.4079` n `126` status `ready` deltaP `-3.4891` edge `-0.0141` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.5531` n `126` status `ready` deltaP `2.5591` edge `0.002` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.265` n `126` status `ready` deltaP `-4.194` edge `-0.0164` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.4008` n `126` status `ready` deltaP `-1.2607` edge `0.1371` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-6.2576` n `112` status `ready` deltaP `11.4832` edge `0.1148` maxDD `-47.026`
- `market_context_high->fx_24h` score `-6.3703` n `112` status `ready` deltaP `-14.3601` edge `-0.006` maxDD `-5.663`
- `market_context_high->commodity_4h` score `-6.8078` n `126` status `ready` deltaP `-17.9007` edge `-0.0787` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.6447` n `126` status `ready` deltaP `-2.0229` edge `0.0577` maxDD `-46.5016`
- `market_context_high->crypto_alt_24h` score `-8.2999` n `112` status `ready` deltaP `11.9792` edge `0.5442` maxDD `-97.2579`
- `market_context_high->index_24h` score `-13.2247` n `112` status `ready` deltaP `-26.5873` edge `-0.1169` maxDD `-33.9664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
