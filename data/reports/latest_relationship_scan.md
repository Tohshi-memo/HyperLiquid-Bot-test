# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T20:37:24.890558+00:00`
- Price records: `672`
- Market context records: `7288`
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

- `market_context_high->fx_1h` score `-0.1698` n `130` status `ready` deltaP `3.8646` edge `0.0014` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.7262` n `130` status `ready` deltaP `-2.2523` edge `-0.016` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.8032` n `130` status `ready` deltaP `-1.5592` edge `0.0113` maxDD `-5.9775`
- `market_context_high->fx_4h` score `-0.8042` n `127` status `ready` deltaP `6.357` edge `0.0145` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-0.8933` n `130` status `ready` deltaP `2.3284` edge `0.011` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.9502` n `125` status `ready` deltaP `-0.1391` edge `0.0019` maxDD `-2.1564`
- `market_context_high->unknown_1h` score `-1.1726` n `130` status `ready` deltaP `0.707` edge `-0.0927` maxDD `-1.3212`
- `market_context_high->commodity_4h` score `-1.1943` n `127` status `ready` deltaP `1.5627` edge `-0.0131` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-1.2712` n `127` status `ready` deltaP `6.6197` edge `0.0858` maxDD `-6.2026`
- `market_context_high->index_1h` score `-1.4872` n `130` status `ready` deltaP `-6.9207` edge `-0.0106` maxDD `-2.3756`
- `market_context_high->metal_1h` score `-2.3384` n `130` status `ready` deltaP `-10.7232` edge `-0.0076` maxDD `-1.9289`
- `market_context_high->metal_4h` score `-2.6004` n `127` status `ready` deltaP `-11.3897` edge `-0.0119` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-2.9713` n `125` status `ready` deltaP `-5.4957` edge `-0.1312` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-3.8774` n `127` status `ready` deltaP `-0.9506` edge `-0.0242` maxDD `-16.7399`
- `market_context_high->equity_1h` score `-4.7565` n `130` status `ready` deltaP `-10.6168` edge `-0.0731` maxDD `-15.5328`
- `market_context_high->crypto_major_4h` score `-5.1025` n `127` status `ready` deltaP `-0.9266` edge `-0.0296` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.4223` n `127` status `ready` deltaP `-15.7817` edge `-0.0664` maxDD `-12.0863`
- `market_context_high->unknown_24h` score `-5.7649` n `126` status `ready` deltaP `-10.3919` edge `-0.0537` maxDD `-16.594`
- `market_context_high->metal_24h` score `-11.6271` n `126` status `ready` deltaP `-29.365` edge `-0.1354` maxDD `-24.3539`
- `market_context_high->index_24h` score `-14.0104` n `125` status `ready` deltaP `-29.6` edge `-0.1735` maxDD `-37.7363`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
