# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T01:07:25.610758+00:00`
- Price records: `672`
- Market context records: `5722`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8892`

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

- `market_context_high->equity_24h` score `1.003` n `218` status `ready` deltaP `16.9183` edge `0.5237` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.9289` n `272` status `ready` deltaP `9.4243` edge `0.1923` maxDD `-9.2176`
- `market_context_high->equity_4h` score `0.2278` n `272` status `ready` deltaP `7.7924` edge `0.1309` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2033` n `284` status `ready` deltaP `3.1247` edge `0.0012` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4529` n `284` status `ready` deltaP `1.5223` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->crypto_alt_4h` score `-0.6042` n `272` status `ready` deltaP `6.9495` edge `0.1367` maxDD `-11.6704`
- `market_context_high->equity_1h` score `-0.6046` n `284` status `ready` deltaP `3.4221` edge `0.0275` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6153` n `284` status `ready` deltaP `0.6241` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7396` n `284` status `ready` deltaP `2.8169` edge `0.0326` maxDD `-5.0409`
- `market_context_high->commodity_1h` score `-0.7439` n `284` status `ready` deltaP `-1.478` edge `-0.0048` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.9581` n `284` status `ready` deltaP `0.9235` edge `0.0286` maxDD `-5.1678`
- `market_context_high->fx_24h` score `-1.1121` n `218` status `ready` deltaP `11.0347` edge `0.0422` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1589` n `272` status `ready` deltaP `1.372` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2584` n `272` status `ready` deltaP `2.6094` edge `0.0058` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.579` n `272` status `ready` deltaP `-6.5369` edge `-0.0495` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8758` n `218` status `ready` deltaP `2.4417` edge `0.0295` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.852` n `272` status `ready` deltaP `-3.7572` edge `-0.0284` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3413` n `218` status `ready` deltaP `7.0225` edge `0.0371` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.5422` n `218` status `ready` deltaP `-6.0397` edge `-0.2382` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.3289` n `218` status `ready` deltaP `-9.3591` edge `-0.0677` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
