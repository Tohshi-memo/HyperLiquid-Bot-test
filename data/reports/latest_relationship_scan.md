# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T10:22:32.940708+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_4h` score `40.8772` n `112` status `ready` deltaP `-0.3049` edge `3.442` maxDD `-1.016`
- `market_context_high->unknown_1h` score `3.8389` n `113` status `ready` deltaP `4.1704` edge `0.341` maxDD `-1.5781`
- `market_context_high->commodity_24h` score `0.8682` n `47` status `ready` deltaP `17.9559` edge `0.0825` maxDD `-3.6055`
- `market_context_high->crypto_major_24h` score `0.3891` n `47` status `ready` deltaP `3.2801` edge `0.1006` maxDD `-4.5369`
- `market_context_high->fx_4h` score `0.0177` n `112` status `ready` deltaP `7.818` edge `0.0092` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0412` n `113` status `ready` deltaP `4.0088` edge `0.0029` maxDD `-0.1258`
- `market_context_high->crypto_alt_24h` score `-0.1447` n `47` status `ready` deltaP `11.3106` edge `0.2139` maxDD `-20.2948`
- `market_context_high->commodity_1h` score `-0.5182` n `113` status `ready` deltaP `-0.3325` edge `0.0091` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.57` n `113` status `ready` deltaP `5.3826` edge `-0.0042` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.616` n `113` status `ready` deltaP `-1.2877` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8774` n `112` status `ready` deltaP `-2.9835` edge `0.0303` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3503` n `113` status `ready` deltaP `2.0494` edge `-0.0287` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.6537` n `47` status `ready` deltaP `-1.8543` edge `0.006` maxDD `-1.1826`
- `market_context_high->metal_4h` score `-1.8267` n `112` status `ready` deltaP `5.4878` edge `-0.0178` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.127` n `112` status `ready` deltaP `-7.4042` edge `-0.0359` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.0538` n `113` status `ready` deltaP `-2.0097` edge `-0.0537` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.242` n `47` status `ready` deltaP `-8.4995` edge `-0.0096` maxDD `-6.9787`
- `market_context_high->equity_1h` score `-3.6905` n `113` status `ready` deltaP `0.8081` edge `-0.0856` maxDD `-12.1865`
- `market_context_high->index_24h` score `-4.6726` n `47` status `ready` deltaP `-14.7828` edge `-0.1626` maxDD `-4.925`
- `market_context_high->crypto_major_4h` score `-6.4291` n `112` status `ready` deltaP `-12.4347` edge `-0.2457` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
