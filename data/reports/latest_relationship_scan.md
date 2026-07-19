# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T17:52:28.078358+00:00`
- Price records: `672`
- Market context records: `7275`
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

- `market_context_high->fx_1h` score `-0.2529` n `138` status `ready` deltaP `2.4481` edge `0.0002` maxDD `-0.5817`
- `market_context_high->crypto_alt_1h` score `-0.7313` n `138` status `ready` deltaP `-0.5511` edge `0.0138` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9005` n `138` status `ready` deltaP `1.8745` edge `0.0131` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.9635` n `136` status `ready` deltaP `3.9688` edge `0.01` maxDD `-1.4649`
- `market_context_high->commodity_1h` score `-1.1557` n `138` status `ready` deltaP `-2.8529` edge `-0.0152` maxDD `-1.9668`
- `market_context_high->unknown_4h` score `-1.2102` n `136` status `ready` deltaP `7.5771` edge `0.0845` maxDD `-6.2026`
- `market_context_high->unknown_1h` score `-1.2951` n `138` status `ready` deltaP `-1.0783` edge `-0.0965` maxDD `-1.3212`
- `market_context_high->index_1h` score `-1.4046` n `138` status `ready` deltaP `-6.0125` edge `-0.0097` maxDD `-2.3816`
- `market_context_high->commodity_4h` score `-1.5315` n `136` status `ready` deltaP `-0.5982` edge `-0.0201` maxDD `-2.9494`
- `market_context_high->fx_24h` score `-2.0841` n `126` status `ready` deltaP `-5.7626` edge `-0.0083` maxDD `-2.1564`
- `market_context_high->commodity_24h` score `-2.1997` n `126` status `ready` deltaP `-1.0711` edge `-0.0964` maxDD `-2.3815`
- `market_context_high->metal_1h` score `-2.2392` n `138` status `ready` deltaP `-9.5765` edge `-0.0069` maxDD `-1.9351`
- `market_context_high->metal_4h` score `-4.2057` n `136` status `ready` deltaP `-12.5807` edge `-0.0191` maxDD `-4.8006`
- `market_context_high->equity_1h` score `-4.461` n `138` status `ready` deltaP `-8.1865` edge `-0.0645` maxDD `-15.5469`
- `market_context_high->index_4h` score `-5.5926` n `136` status `ready` deltaP `-17.1434` edge `-0.064` maxDD `-12.6876`
- `market_context_high->crypto_alt_4h` score `-5.8032` n `136` status `ready` deltaP `-3.5599` edge `-0.0616` maxDD `-23.8617`
- `market_context_high->crypto_major_4h` score `-6.0854` n `136` status `ready` deltaP `-3.9007` edge `-0.0685` maxDD `-25.0091`
- `market_context_high->unknown_24h` score `-6.605` n `127` status `ready` deltaP `-14.0461` edge `-0.0685` maxDD `-19.0622`
- `market_context_high->metal_24h` score `-13.1463` n `127` status `ready` deltaP `-33.4331` edge `-0.1684` maxDD `-30.0054`
- `market_context_high->index_24h` score `-15.7496` n `126` status `ready` deltaP `-29.619` edge `-0.2055` maxDD `-43.4272`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
