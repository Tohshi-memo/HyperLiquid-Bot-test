# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T18:22:43.457316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2638`

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

- `market_context_high->unknown_1h` score `12133.7331` n `107` status `ready` deltaP `0.5751` edge `1011.1604` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7635.4447` n `106` status `ready` deltaP `-0.0777` edge `636.316` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.5988` n `88` status `ready` deltaP `44.2392` edge `1.8143` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.8256` n `88` status `ready` deltaP `24.4003` edge `1.4927` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.5905` n `106` status `ready` deltaP `3.02` edge `0.3943` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.8694` n `106` status `ready` deltaP `3.9346` edge `0.2538` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.4712` n `88` status `ready` deltaP `19.0656` edge `0.221` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.3568` n `106` status `ready` deltaP `17.4931` edge `0.0421` maxDD `-5.9858`
- `market_context_high->metal_1h` score `-0.2013` n `107` status `ready` deltaP `4.0601` edge `0.0136` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.2637` n `107` status `ready` deltaP `4.4322` edge `0.0763` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2977` n `107` status `ready` deltaP `2.8261` edge `0.0042` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2403` n `107` status `ready` deltaP `-2.5589` edge `0.0359` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.3913` n `107` status `ready` deltaP `5.7795` edge `0.0234` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6651` n `107` status `ready` deltaP `-12.1272` edge `-0.0022` maxDD `-0.4566`
- `market_context_high->index_4h` score `-2.0568` n `106` status `ready` deltaP `-4.1648` edge `-0.0093` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.4358` n `106` status `ready` deltaP `-15.868` edge `-0.0049` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4859` n `107` status `ready` deltaP `-10.3713` edge `-0.0302` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.1981` n `88` status `ready` deltaP `-24.2898` edge `-0.0106` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.2487` n `106` status `ready` deltaP `-30.4187` edge `-0.1177` maxDD `-15.3518`
- `market_context_high->equity_4h` score `-10.0695` n `106` status `ready` deltaP `-8.6919` edge `-0.1135` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
