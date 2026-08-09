# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T06:04:08.498567+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8827`

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

- `market_context_high->equity_24h` score `3.618` n `103` status `ready` deltaP `4.5729` edge `0.577` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7091` n `103` status `ready` deltaP `13.2535` edge `0.195` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3564` n `138` status `ready` deltaP `15.7542` edge `0.0753` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8948` n `143` status `ready` deltaP `11.2904` edge `0.0336` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8196` n `103` status `ready` deltaP `21.575` edge `0.0479` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5517` n `103` status `ready` deltaP `9.1002` edge `0.1632` maxDD `-5.9181`
- `market_context_high->fx_4h` score `-0.2922` n `138` status `ready` deltaP `7.9312` edge `-0.0019` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.293` n `143` status `ready` deltaP `4.2953` edge `-0.0035` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4789` n `143` status `ready` deltaP `-2.4412` edge `-0.0062` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.7111` n `143` status `ready` deltaP `-5.1871` edge `-0.007` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9721` n `143` status `ready` deltaP `-0.3371` edge `0.0041` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.9804` n `138` status `ready` deltaP `-1.5576` edge `-0.0108` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.0596` n `138` status `ready` deltaP `-2.4699` edge `-0.0185` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9636` n `143` status `ready` deltaP `-10.433` edge `-0.0299` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6633` n `138` status `ready` deltaP `-2.5075` edge `-0.0715` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1796` n `143` status `ready` deltaP `-10.5377` edge `-0.0625` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.2299` n `103` status `ready` deltaP `6.2197` edge `-0.0612` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.7921` n `138` status `ready` deltaP `-7.5844` edge `-0.0998` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.591` n `103` status `ready` deltaP `-12.4461` edge `-0.1553` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.0045` n `143` status `ready` deltaP `-6.0938` edge `-0.5817` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
