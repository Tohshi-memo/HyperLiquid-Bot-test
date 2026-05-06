# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T17:07:30.963382+00:00`
- Price records: `472`
- Market context records: `563`
- Flow alert records: `1590`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.916` n `142` status `ready` deltaP `7.5405` edge `0.3642` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0169` n `142` status `ready` deltaP `9.9004` edge `0.2188` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.015` n `146` status `ready` deltaP `9.7679` edge `0.0201` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3309` n `146` status `ready` deltaP `1.6769` edge `0.0042` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5334` n `146` status `ready` deltaP `2.04` edge `0.0394` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6239` n `146` status `ready` deltaP `1.0451` edge `-0.0016` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1864` n `146` status `ready` deltaP `-1.3256` edge `-0.009` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2203` n `146` status `ready` deltaP `-4.1037` edge `-0.014` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3747` n `146` status `ready` deltaP `4.1272` edge `-0.0106` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.8069` n `142` status `ready` deltaP `-5.7549` edge `0.0873` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-2.0074` n `146` status `ready` deltaP `3.3924` edge `-0.0176` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.0146` n `146` status `ready` deltaP `1.5729` edge `-0.0261` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.2538` n `146` status `ready` deltaP `2.6196` edge `0.0517` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.0272` n `146` status `ready` deltaP `-2.4094` edge `-0.021` maxDD `-10.5498`
- `market_context_high->crypto_major_4h` score `-3.2519` n `146` status `ready` deltaP `9.8564` edge `0.0339` maxDD `-22.648`
- `market_context_high->metal_1h` score `-3.2868` n `146` status `ready` deltaP `-4.5253` edge `-0.0478` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5631` n `146` status `ready` deltaP `-6.0189` edge `0.0933` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.6917` n `142` status `ready` deltaP `-10.0295` edge `0.0197` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.4428` n `142` status `ready` deltaP `-5.3687` edge `-0.0402` maxDD `-19.1542`
- `market_context_high->unknown_4h` score `-5.3724` n `146` status `ready` deltaP `-0.1172` edge `-0.2591` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
