# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T20:37:31.289612+00:00`
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

- `market_context_high->unknown_24h` score `12.892` n `90` status `ready` deltaP `4.4445` edge `1.049` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `2.9245` n `107` status `ready` deltaP `-2.7069` edge `0.3613` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.3185` n `107` status `ready` deltaP `15.016` edge `0.0944` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9117` n `90` status `ready` deltaP `2.0139` edge `0.2203` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.8786` n `90` status `ready` deltaP `24.7223` edge `0.0684` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4587` n `109` status `ready` deltaP `8.0591` edge `0.0261` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0428` n `109` status `ready` deltaP `6.1322` edge `-0.0023` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0838` n `107` status `ready` deltaP `9.9983` edge `0.0086` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4934` n `109` status `ready` deltaP `-0.9614` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7227` n `107` status `ready` deltaP `3.6628` edge `0.0064` maxDD `-3.211`
- `market_context_high->index_1h` score `-0.8226` n `109` status `ready` deltaP `-4.5542` edge `-0.0217` maxDD `-1.6054`
- `market_context_high->crypto_alt_24h` score `-1.45` n `90` status `ready` deltaP `0.5555` edge `-0.0453` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5885` n `107` status `ready` deltaP `0.1097` edge `-0.0654` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.6381` n `109` status `ready` deltaP `-5.4373` edge `-0.0292` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.9359` n `109` status `ready` deltaP `0.3709` edge `-0.0971` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.2611` n `107` status `ready` deltaP `-14.5715` edge `-0.0673` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.3198` n `90` status `ready` deltaP `-9.5139` edge `-0.0145` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4854` n `109` status `ready` deltaP `-12.0475` edge `-0.0728` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.6652` n `109` status `ready` deltaP `1.5835` edge `-0.2713` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0452` n `90` status `ready` deltaP `10.8334` edge `-0.0258` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
