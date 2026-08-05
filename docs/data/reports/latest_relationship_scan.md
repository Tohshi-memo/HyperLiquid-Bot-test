# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T20:00:23.557481+00:00`
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

- `market_context_high->unknown_24h` score `12.9172` n `90` status `ready` deltaP `4.4445` edge `1.0511` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `3.2214` n `105` status `ready` deltaP `-1.8902` edge `0.3806` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4603` n `105` status `ready` deltaP `16.1731` edge `0.0985` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.911` n `90` status `ready` deltaP `2.0139` edge `0.2202` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.888` n `90` status `ready` deltaP `24.7223` edge `0.0696` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4311` n `109` status `ready` deltaP `7.7597` edge `0.0258` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0428` n `109` status `ready` deltaP `6.1322` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0285` n `105` status `ready` deltaP `11.0308` edge `0.0088` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5121` n `109` status `ready` deltaP `-1.2608` edge `-0.0078` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7625` n `105` status `ready` deltaP `2.9863` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.8249` n `109` status `ready` deltaP `-4.5542` edge `-0.022` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.4734` n `90` status `ready` deltaP `0.5555` edge `-0.0483` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.6069` n `109` status `ready` deltaP `-5.2876` edge `-0.0276` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.6704` n `105` status `ready` deltaP `-0.7448` edge `-0.0702` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.943` n `109` status `ready` deltaP `0.3709` edge `-0.098` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.2285` n `105` status `ready` deltaP `-14.004` edge `-0.0669` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.3691` n `90` status `ready` deltaP `-9.8612` edge `-0.0185` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4794` n `109` status `ready` deltaP `-12.0475` edge `-0.0723` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6437` n `109` status `ready` deltaP `1.7332` edge `-0.2705` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0421` n `90` status `ready` deltaP `10.8334` edge `-0.0254` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
