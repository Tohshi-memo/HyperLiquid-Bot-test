# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T14:37:29.362844+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11687`

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

- `risk_on_high->crypto_alt_24h` score `14.5813` n `64` status `ready` deltaP `36.9792` edge `1.2181` maxDD `-16.295`
- `risk_on_and_context->crypto_alt_24h` score `14.5813` n `64` status `ready` deltaP `36.9792` edge `1.2181` maxDD `-16.295`
- `risk_on_high->unknown_4h` score `8.1286` n `107` status `ready` deltaP `25.2508` edge `0.5707` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.1286` n `107` status `ready` deltaP `25.2508` edge `0.5707` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5826` n `159` status `ready` deltaP `21.9474` edge `0.4716` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `4.7431` n `107` status `ready` deltaP `17.7181` edge `0.6961` maxDD `-27.517`
- `risk_on_high->fx_24h` score `3.1803` n `64` status `ready` deltaP `61.8056` edge `0.0452` maxDD `-0.9608`
- `risk_on_and_context->fx_24h` score `3.1803` n `64` status `ready` deltaP `61.8056` edge `0.0452` maxDD `-0.9608`
- `risk_on_high->crypto_major_24h` score `2.4995` n `64` status `ready` deltaP `22.3958` edge `0.5665` maxDD `-26.2949`
- `risk_on_and_context->crypto_major_24h` score `2.4995` n `64` status `ready` deltaP `22.3958` edge `0.5665` maxDD `-26.2949`
- `risk_on_high->unknown_1h` score `2.461` n `107` status `ready` deltaP `6.8149` edge `0.2173` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.461` n `107` status `ready` deltaP `6.8149` edge `0.2173` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2384` n `159` status `ready` deltaP `6.1566` edge `0.2085` maxDD `-2.041`
- `market_context_high->metal_24h` score `1.9304` n `107` status `ready` deltaP `28.907` edge `0.1962` maxDD `-4.6477`
- `news_risk_high->unknown_1h` score `1.5575` n `61` status `ready` deltaP `3.9192` edge `0.1383` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.445` n `107` status `ready` deltaP `35.6812` edge `0.0284` maxDD `-1.6688`
- `risk_on_high->metal_24h` score `1.1797` n `64` status `ready` deltaP `28.8194` edge `0.0847` maxDD `-4.047`
- `risk_on_and_context->metal_24h` score `1.1797` n `64` status `ready` deltaP `28.8194` edge `0.0847` maxDD `-4.047`
- `risk_on_high->commodity_24h` score `0.7323` n `64` status `ready` deltaP `9.0278` edge `0.1325` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.7323` n `64` status `ready` deltaP `9.0278` edge `0.1325` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
