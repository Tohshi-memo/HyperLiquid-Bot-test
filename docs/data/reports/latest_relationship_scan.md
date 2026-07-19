# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T20:22:25.419536+00:00`
- Price records: `672`
- Market context records: `7287`
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

- `market_context_high->fx_1h` score `-0.1827` n `129` status `ready` deltaP `3.663` edge `0.0011` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.7495` n `129` status `ready` deltaP `-2.6399` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->fx_4h` score `-0.7954` n `127` status `ready` deltaP `6.5099` edge `0.0146` maxDD `-1.4649`
- `market_context_high->crypto_alt_1h` score `-0.8251` n `129` status `ready` deltaP `-1.815` edge `0.0102` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9122` n `129` status `ready` deltaP `2.1144` edge `0.01` maxDD `-7.6171`
- `market_context_high->fx_24h` score `-0.9677` n `124` status `ready` deltaP `-0.3717` edge `0.0012` maxDD `-2.1564`
- `market_context_high->unknown_1h` score `-1.1593` n `129` status `ready` deltaP `0.933` edge `-0.0925` maxDD `-1.3212`
- `market_context_high->commodity_4h` score `-1.1919` n `127` status `ready` deltaP `1.5627` edge `-0.0129` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-1.2906` n `127` status `ready` deltaP `6.4673` edge `0.0852` maxDD `-6.2026`
- `market_context_high->index_1h` score `-1.5167` n `129` status `ready` deltaP `-7.2596` edge `-0.0108` maxDD `-2.3756`
- `market_context_high->metal_1h` score `-2.3164` n `129` status `ready` deltaP `-10.4489` edge `-0.0076` maxDD `-1.9289`
- `market_context_high->metal_4h` score `-2.5893` n `127` status `ready` deltaP `-11.2372` edge `-0.0115` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-2.9864` n `124` status `ready` deltaP `-5.7602` edge `-0.1307` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-3.8472` n `127` status `ready` deltaP `-0.7982` edge `-0.0227` maxDD `-16.7399`
- `market_context_high->equity_1h` score `-4.8004` n `129` status `ready` deltaP `-10.9854` edge `-0.0743` maxDD `-15.5328`
- `market_context_high->crypto_major_4h` score `-5.0723` n `127` status `ready` deltaP `-0.7742` edge `-0.0281` maxDD `-23.4879`
- `market_context_high->index_4h` score `-5.4076` n `127` status `ready` deltaP `-15.6288` edge `-0.0662` maxDD `-12.0863`
- `market_context_high->unknown_24h` score `-5.7951` n `125` status `ready` deltaP `-10.6944` edge `-0.0542` maxDD `-16.594`
- `market_context_high->metal_24h` score `-11.6759` n `125` status `ready` deltaP `-29.8708` edge `-0.1361` maxDD `-24.3539`
- `market_context_high->index_24h` score `-14.0181` n `124` status `ready` deltaP `-29.5806` edge `-0.1746` maxDD `-37.7097`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
