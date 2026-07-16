# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T14:22:30.400366+00:00`
- Price records: `672`
- Market context records: `6926`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->fx_1h` score `-0.1829` n `225` status `ready` deltaP `3.352` edge `0.0027` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.3862` n `225` status `ready` deltaP `3.1557` edge `0.0232` maxDD `-3.7803`
- `market_context_high->unknown_24h` score `-0.4369` n `207` status `ready` deltaP `-5.5166` edge `0.3824` maxDD `-14.4643`
- `market_context_high->crypto_major_1h` score `-0.4704` n `225` status `ready` deltaP `4.4844` edge `0.0213` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6477` n `225` status `ready` deltaP `-0.9707` edge `-0.0081` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.6975` n `225` status `ready` deltaP `0.2548` edge `0.0` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7564` n `225` status `ready` deltaP `-2.833` edge `-0.0013` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-0.7806` n `224` status `ready` deltaP `14.46` edge `0.0099` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.4931` n `225` status `ready` deltaP `-1.8177` edge `-0.0222` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.5642` n `224` status `ready` deltaP `-3.713` edge `-0.0268` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.5934` n `225` status `ready` deltaP `3.8011` edge `-0.0116` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.7066` n `224` status `ready` deltaP `7.7527` edge `-0.0125` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-1.96` n `224` status `ready` deltaP `4.9107` edge `0.0143` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7233` n `224` status `ready` deltaP `1.9055` edge `-0.0035` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7572` n `224` status `ready` deltaP `0.0653` edge `-0.0212` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9343` n `224` status `ready` deltaP `-7.3606` edge `0.0411` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.0444` n `207` status `ready` deltaP `-2.7721` edge `-0.0484` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.0343` n `207` status `ready` deltaP `-3.9092` edge `-0.0065` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.6788` n `224` status `ready` deltaP `5.1503` edge `-0.0961` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.5302` n `207` status `ready` deltaP `-12.0999` edge `-0.1141` maxDD `-31.575`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
