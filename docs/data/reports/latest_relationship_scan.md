# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T10:52:25.558900+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8030`

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

- `market_context_high->crypto_major_24h` score `23.2224` n `43` status `ready` deltaP `33.7936` edge `1.8227` maxDD `-5.3566`
- `market_context_high->crypto_alt_24h` score `22.7925` n `43` status `ready` deltaP `22.1617` edge `1.9003` maxDD `-8.2269`
- `market_context_high->unknown_4h` score `15.9856` n `110` status `ready` deltaP `-3.6946` edge `1.4214` maxDD `-1.8373`
- `risk_on_high->crypto_alt_4h` score `3.7908` n `48` status `ready` deltaP `18.1911` edge `0.2394` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.7908` n `48` status `ready` deltaP `18.1911` edge `0.2394` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.4418` n `48` status `ready` deltaP `32.6728` edge `0.3087` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.4418` n `48` status `ready` deltaP `32.6728` edge `0.3087` maxDD `-4.1548`
- `market_context_high->unknown_1h` score `3.0903` n `110` status `ready` deltaP `-3.5765` edge `0.315` maxDD `-1.024`
- `market_context_high->equity_24h` score `2.4893` n `43` status `ready` deltaP `1.0255` edge `0.4526` maxDD `-7.5571`
- `market_context_high->crypto_major_4h` score `1.8263` n `110` status `ready` deltaP `13.5061` edge `0.2539` maxDD `-9.6732`
- `market_context_high->index_24h` score `1.6823` n `43` status `ready` deltaP `24.2127` edge `0.1103` maxDD `-0.4833`
- `market_context_high->metal_24h` score `1.5203` n `43` status `ready` deltaP `17.4742` edge `0.0699` maxDD `-1.4428`
- `market_context_high->crypto_alt_4h` score `1.2031` n `110` status `ready` deltaP `7.0926` edge `0.263` maxDD `-12.1357`
- `market_context_high->crypto_alt_1h` score `1.0853` n `110` status `ready` deltaP `9.1236` edge `0.1247` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.8052` n `48` status `ready` deltaP `5.6387` edge `0.0892` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8052` n `48` status `ready` deltaP `5.6387` edge `0.0892` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `0.3228` n `48` status `ready` deltaP `4.4661` edge `0.0769` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3228` n `48` status `ready` deltaP `4.4661` edge `0.0769` maxDD `-3.2233`
- `market_context_high->crypto_major_1h` score `0.2189` n `110` status `ready` deltaP `3.0267` edge `0.0842` maxDD `-3.4384`
- `market_context_high->metal_1h` score `-0.213` n `110` status `ready` deltaP `4.1072` edge `0.0014` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
