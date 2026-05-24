# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T12:52:15.996618+00:00`
- Price records: `672`
- Market context records: `1738`
- Flow alert records: `6907`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8838`

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

- `market_context_high->metal_24h` score `7.0251` n `154` status `ready` deltaP `25.9684` edge `0.6549` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.7867` n `196` status `ready` deltaP `20.3615` edge `0.5231` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `4.7906` n `154` status `ready` deltaP `16.0436` edge `0.8243` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.3263` n `154` status `ready` deltaP `18.4744` edge `0.3602` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.1697` n `196` status `ready` deltaP `21.5001` edge `0.4447` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.0855` n `196` status `ready` deltaP `13.6417` edge `0.3933` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9621` n `196` status `ready` deltaP `15.9594` edge `0.2499` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.6584` n `154` status `ready` deltaP `16.9169` edge `0.5986` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7501` n `196` status `ready` deltaP `7.4209` edge `0.1154` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.6697` n `196` status `ready` deltaP `10.0361` edge `0.0978` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.4495` n `154` status `ready` deltaP `20.4664` edge `0.7596` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.3444` n `154` status `ready` deltaP `21.6311` edge `1.0654` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.222` n `196` status `ready` deltaP `5.0471` edge `0.0922` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.049` n `196` status `ready` deltaP `4.9707` edge `0.0518` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3185` n `196` status `ready` deltaP `2.7191` edge `0.0185` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.329` n `196` status `ready` deltaP `11.9867` edge `0.1471` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5269` n `196` status `ready` deltaP `5.9453` edge `0.0264` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.656` n `196` status `ready` deltaP `-2.9665` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7016` n `154` status `ready` deltaP `6.0354` edge `0.0062` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.5803` n `196` status `ready` deltaP `0.7882` edge `0.01` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
