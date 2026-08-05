# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T19:22:35.830410+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `12.9767` n `90` status `ready` deltaP `4.6181` edge `1.0549` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.5386` n `103` status `ready` deltaP `-1.0301` edge `0.4013` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5126` n `103` status `ready` deltaP `16.5566` edge `0.1003` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9211` n `90` status `ready` deltaP `2.0139` edge `0.2215` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.902` n `90` status `ready` deltaP `24.7223` edge `0.0714` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.418` n `109` status `ready` deltaP `7.61` edge `0.0257` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0308` n `109` status `ready` deltaP `5.9825` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0335` n `103` status `ready` deltaP `10.98` edge `0.0085` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5074` n `109` status `ready` deltaP `-1.2608` edge `-0.0072` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7439` n `103` status `ready` deltaP `3.2545` edge `0.0064` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.8078` n `109` status `ready` deltaP `-4.4045` edge `-0.0208` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.4828` n `90` status `ready` deltaP `0.5555` edge `-0.0495` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5673` n `109` status `ready` deltaP `-5.2876` edge `-0.0243` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.7264` n `103` status `ready` deltaP `-1.3275` edge `-0.0735` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8931` n `109` status `ready` deltaP `0.5206` edge `-0.0926` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1823` n `103` status `ready` deltaP `-13.2504` edge `-0.066` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.425` n `90` status `ready` deltaP `-10.382` edge `-0.0222` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4338` n `109` status `ready` deltaP `-11.7481` edge `-0.0705` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6413` n `109` status `ready` deltaP `1.7332` edge `-0.2703` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.039` n `90` status `ready` deltaP `10.8334` edge `-0.025` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
