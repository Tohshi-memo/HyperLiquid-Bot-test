# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T16:37:29.792200+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10826`

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

- `market_context_high->equity_24h` score `3.2923` n `105` status `ready` deltaP `3.5168` edge `0.5569` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.165` n `105` status `ready` deltaP `8.5515` edge `0.181` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.321` n `143` status `ready` deltaP `16.2716` edge `0.0689` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.866` n `143` status `ready` deltaP `11.5898` edge `0.0292` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6384` n `105` status `ready` deltaP `20.4018` edge `0.0325` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.3215` n `105` status `ready` deltaP `5.7986` edge `0.1557` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4079` n `143` status `ready` deltaP `2.948` edge `-0.0041` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4237` n `143` status `ready` deltaP `-1.543` edge `-0.0051` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5844` n `143` status `ready` deltaP `4.6084` edge `-0.0041` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7064` n `143` status `ready` deltaP `-5.1871` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.9366` n `143` status `ready` deltaP `-1.2205` edge `-0.0094` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9444` n `143` status `ready` deltaP `-0.4868` edge `0.0074` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0272` n `143` status `ready` deltaP `-1.9657` edge `-0.0177` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0451` n `143` status `ready` deltaP `-11.1815` edge `-0.0317` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5922` n `143` status `ready` deltaP `-1.7237` edge `-0.0708` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.3269` n `143` status `ready` deltaP `-12.1844` edge `-0.0638` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.9537` n `143` status `ready` deltaP `-8.7338` edge `-0.1056` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.2147` n `105` status `ready` deltaP `1.2004` edge `-0.1098` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.5512` n `105` status `ready` deltaP `-18.3035` edge `-0.2796` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8316` n `143` status `ready` deltaP `-6.2435` edge `-0.5663` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
