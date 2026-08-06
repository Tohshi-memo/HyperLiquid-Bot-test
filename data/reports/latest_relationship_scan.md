# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T02:37:24.867309+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11685`

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

- `market_context_high->unknown_24h` score `12.4852` n `90` status `ready` deltaP `4.4445` edge `1.0151` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.9258` n `109` status `ready` deltaP `-1.9551` edge `0.3564` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.2288` n `109` status `ready` deltaP `14.209` edge `0.0923` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.7815` n `90` status `ready` deltaP `2.0139` edge `0.2036` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.7701` n `90` status `ready` deltaP `24.375` edge `0.0568` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3832` n `109` status `ready` deltaP `7.4603` edge `0.0238` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0715` n `109` status `ready` deltaP `6.4316` edge `-0.0019` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1383` n `109` status `ready` deltaP `9.0093` edge `0.0082` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5674` n `109` status `ready` deltaP `-2.159` edge `-0.0089` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7237` n `109` status `ready` deltaP `-3.0572` edge `-0.019` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9334` n `109` status `ready` deltaP `1.2601` edge `-0.0046` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.271` n `90` status `ready` deltaP `0.7291` edge `-0.0235` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.421` n `109` status `ready` deltaP `-4.5391` edge `-0.0171` maxDD `-3.0178`
- `market_context_high->index_24h` score `-1.7194` n `90` status `ready` deltaP `-5.3473` edge `0.0347` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8074` n `109` status `ready` deltaP `1.4188` edge `-0.0876` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1635` n `109` status `ready` deltaP `-13.43` edge `-0.0624` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1673` n `109` status `ready` deltaP `0.9272` edge `-0.0478` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.2659` n `109` status `ready` deltaP `-11.1493` edge `-0.0605` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.2897` n `109` status `ready` deltaP `1.8829` edge `-0.242` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.1039` n `90` status `ready` deltaP `10.1389` edge `-0.0287` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
