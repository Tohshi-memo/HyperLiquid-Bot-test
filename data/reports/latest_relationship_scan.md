# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T21:22:26.712483+00:00`
- Price records: `672`
- Market context records: `7292`
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

- `market_context_high->fx_1h` score `-0.1737` n `131` status `ready` deltaP `3.7606` edge `0.0016` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.711` n `131` status `ready` deltaP `-2.0207` edge `-0.0156` maxDD `-1.9668`
- `market_context_high->fx_4h` score `-0.777` n `129` status `ready` deltaP `6.8203` edge `0.0149` maxDD `-1.4649`
- `market_context_high->crypto_alt_1h` score `-0.7957` n `131` status `ready` deltaP `-1.4593` edge `0.0116` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.8972` n `131` status `ready` deltaP `2.2375` edge `0.0111` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.9859` n `125` status `ready` deltaP `-0.6609` edge `0.0008` maxDD `-2.1564`
- `market_context_high->unknown_1h` score `-1.1428` n `131` status `ready` deltaP `1.2502` edge `-0.0925` maxDD `-1.3212`
- `market_context_high->commodity_4h` score `-1.2444` n `129` status `ready` deltaP `1.1165` edge `-0.0143` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-1.3485` n `129` status `ready` deltaP `5.9238` edge `0.084` maxDD `-6.2026`
- `market_context_high->index_1h` score `-1.4823` n `131` status `ready` deltaP `-6.8897` edge `-0.0104` maxDD `-2.3756`
- `market_context_high->metal_1h` score `-2.348` n `131` status `ready` deltaP `-10.8436` edge `-0.0076` maxDD `-1.9289`
- `market_context_high->metal_4h` score `-2.5597` n `129` status `ready` deltaP `-10.6081` edge `-0.0119` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-2.9166` n `125` status `ready` deltaP `-5.3217` edge `-0.1278` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-3.802` n `129` status `ready` deltaP `-0.3521` edge `-0.0219` maxDD `-16.7399`
- `market_context_high->equity_1h` score `-4.7384` n `131` status `ready` deltaP `-10.5563` edge `-0.072` maxDD `-15.5328`
- `market_context_high->crypto_major_4h` score `-5.0205` n `129` status `ready` deltaP `-0.2612` edge `-0.0272` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.3446` n `129` status `ready` deltaP `-15.0807` edge `-0.0646` maxDD `-12.0863`
- `market_context_high->unknown_24h` score `-5.813` n `126` status `ready` deltaP `-10.7391` edge `-0.0554` maxDD `-16.594`
- `market_context_high->metal_24h` score `-11.6607` n `126` status `ready` deltaP `-29.365` edge `-0.1382` maxDD `-24.3539`
- `market_context_high->index_24h` score `-14.0512` n `125` status `ready` deltaP `-29.6` edge `-0.1769` maxDD `-37.7363`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
