# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T17:07:32.418821+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7338`

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

- `market_context_high->unknown_24h` score `1381.235` n `40` status `ready` deltaP `-20.3125` edge `115.2747` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `51.0523` n `77` status `ready` deltaP `-7.1389` edge `4.36` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `10.9957` n `89` status `ready` deltaP `-3.3102` edge `0.972` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.814` n `40` status `ready` deltaP `27.6736` edge `0.5929` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3856` n `40` status `ready` deltaP `52.4306` edge `0.1826` maxDD `0.0`
- `market_context_high->fx_24h` score `3.3482` n `40` status `ready` deltaP `37.8125` edge `0.0399` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.6645` n `40` status `ready` deltaP `-20.5903` edge `0.5908` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7826` n `77` status `ready` deltaP `12.8069` edge `0.0082` maxDD `-0.2692`
- `market_context_high->crypto_alt_1h` score `0.7247` n `89` status `ready` deltaP `7.3068` edge `0.1151` maxDD `-4.9401`
- `market_context_high->commodity_4h` score `0.4944` n `77` status `ready` deltaP `12.0506` edge `0.0142` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `-0.0171` n `89` status `ready` deltaP `3.2615` edge `0.0052` maxDD `-0.6025`
- `market_context_high->crypto_major_1h` score `-0.051` n `89` status `ready` deltaP `1.4617` edge `0.0726` maxDD `-3.7778`
- `market_context_high->fx_1h` score `-0.1651` n `89` status `ready` deltaP `1.3894` edge `0.0012` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.1785` n `89` status `ready` deltaP `6.0318` edge `0.0038` maxDD `-0.7107`
- `market_context_high->metal_4h` score `-0.2632` n `77` status `ready` deltaP `2.8687` edge `0.0194` maxDD `-1.1153`
- `market_context_high->index_1h` score `-0.645` n `89` status `ready` deltaP `-2.3582` edge `-0.0019` maxDD `-0.5392`
- `market_context_high->index_4h` score `-0.897` n `77` status `ready` deltaP `-6.9845` edge `0.0016` maxDD `-0.9364`
- `market_context_high->crypto_major_4h` score `-0.9175` n `77` status `ready` deltaP `-3.7892` edge `0.1182` maxDD `-11.1784`
- `market_context_high->equity_1h` score `-0.9822` n `89` status `ready` deltaP `-6.025` edge `0.0012` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-2.053` n `77` status `ready` deltaP `-7.131` edge `0.1323` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
