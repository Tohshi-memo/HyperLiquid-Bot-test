# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T10:37:01.818806+00:00`
- Price records: `542`
- Market context records: `638`
- Flow alert records: `1807`
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

- `market_context_high->crypto_major_24h` score `6.2833` n `146` status `ready` deltaP `17.5656` edge `0.4399` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.6511` n `146` status `ready` deltaP `8.0595` edge `0.422` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.1` n `146` status `ready` deltaP `8.7939` edge `0.0157` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.344` n `146` status `ready` deltaP `1.6059` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.52` n `146` status `ready` deltaP `1.8778` edge `0.0416` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6747` n `146` status `ready` deltaP `0.0975` edge `-0.0018` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.149` n `146` status `ready` deltaP `-4.2165` edge `-0.0073` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.1669` n `146` status `ready` deltaP `6.0193` edge `-0.0059` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3207` n `146` status `ready` deltaP `-2.5242` edge `-0.0122` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6759` n `146` status `ready` deltaP `5.8715` edge `-0.0065` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1152` n `146` status `ready` deltaP `3.857` edge `0.055` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3552` n `146` status `ready` deltaP `-1.215` edge `-0.0359` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5426` n `146` status `ready` deltaP `13.1726` edge `0.0709` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0326` n `146` status `ready` deltaP `-8.6252` edge `0.0043` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.3417` n `146` status `ready` deltaP `-5.217` edge `0.1064` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.447` n `146` status `ready` deltaP `-5.2529` edge `-0.0563` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.479` n `146` status `ready` deltaP `-4.4717` edge `-0.0449` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.3773` n `146` status `ready` deltaP `-3.8121` edge `-0.0186` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.8093` n `146` status `ready` deltaP `1.3412` edge `-0.2219` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.8682` n `146` status `ready` deltaP `-11.7616` edge `-0.0668` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
