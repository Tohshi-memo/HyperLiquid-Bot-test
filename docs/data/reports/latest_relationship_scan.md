# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T18:37:32.687048+00:00`
- Price records: `672`
- Market context records: `6842`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11802`

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

- `market_context_high->unknown_24h` score `1.0013` n `176` status `ready` deltaP `-1.5467` edge `0.5139` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.0849` n `176` status `ready` deltaP `8.3176` edge `0.1243` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2385` n `218` status `ready` deltaP `2.4337` edge `0.0017` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.5439` n `218` status `ready` deltaP `2.2496` edge `0.0161` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.5475` n `218` status `ready` deltaP `4.2342` edge `0.0163` maxDD `-4.2122`
- `market_context_high->index_1h` score `-0.8892` n `218` status `ready` deltaP `-2.7427` edge `-0.0046` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-1.0214` n `218` status `ready` deltaP `-6.4605` edge `-0.0111` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0346` n `208` status `ready` deltaP `10.2955` edge `0.0051` maxDD `-2.1765`
- `market_context_high->commodity_1h` score `-1.0532` n `218` status `ready` deltaP `-2.2647` edge `-0.0042` maxDD `-2.1443`
- `market_context_high->unknown_1h` score `-1.6947` n `218` status `ready` deltaP `-3.7082` edge `-0.0264` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9947` n `218` status `ready` deltaP `-0.2417` edge `-0.0361` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.2307` n `208` status `ready` deltaP `0.8678` edge `-0.0338` maxDD `-11.3047`
- `market_context_high->commodity_4h` score `-2.3602` n `208` status `ready` deltaP `-4.62` edge `-0.0169` maxDD `-5.5853`
- `market_context_high->metal_4h` score `-2.7035` n `208` status `ready` deltaP `-3.2364` edge `-0.0267` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9477` n `208` status `ready` deltaP `0.0469` edge `-0.0455` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1468` n `208` status `ready` deltaP `-0.2228` edge `-0.0436` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.3035` n `208` status `ready` deltaP `-9.9203` edge `0.0274` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.472` n `176` status `ready` deltaP `-9.7853` edge `-0.0038` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.9587` n `208` status `ready` deltaP `-1.63` edge `-0.2197` maxDD `-56.1828`
- `market_context_high->metal_24h` score `-9.2169` n `176` status `ready` deltaP `-18.8447` edge `-0.2075` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
