# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T14:52:27.909766+00:00`
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

- `risk_on_high->crypto_alt_24h` score `13.9139` n `65` status `ready` deltaP `35.7052` edge `1.1884` maxDD `-17.3555`
- `risk_on_and_context->crypto_alt_24h` score `13.9139` n `65` status `ready` deltaP `35.7052` edge `1.1884` maxDD `-17.3555`
- `risk_on_high->unknown_4h` score `8.108` n `107` status `ready` deltaP `25.0983` edge `0.57` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.108` n `107` status `ready` deltaP `25.0983` edge `0.57` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.562` n `159` status `ready` deltaP `21.7949` edge `0.4709` maxDD `-2.5493`
- `market_context_high->crypto_alt_24h` score `4.5388` n `108` status `ready` deltaP `17.1297` edge `0.683` maxDD `-27.517`
- `risk_on_high->fx_24h` score `3.0717` n `65` status `ready` deltaP `60.6571` edge `0.0441` maxDD `-1.041`
- `risk_on_and_context->fx_24h` score `3.0717` n `65` status `ready` deltaP `60.6571` edge `0.0441` maxDD `-1.041`
- `risk_on_high->unknown_1h` score `2.455` n `107` status `ready` deltaP `6.8149` edge `0.2168` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.455` n `107` status `ready` deltaP `6.8149` edge `0.2168` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2324` n `159` status `ready` deltaP `6.1566` edge `0.208` maxDD `-2.041`
- `risk_on_high->crypto_major_24h` score `2.0462` n `65` status `ready` deltaP `21.3141` edge `0.5394` maxDD `-27.8664`
- `risk_on_and_context->crypto_major_24h` score `2.0462` n `65` status `ready` deltaP `21.3141` edge `0.5394` maxDD `-27.8664`
- `market_context_high->metal_24h` score `1.7699` n `108` status `ready` deltaP `28.2407` edge `0.1905` maxDD `-5.1486`
- `news_risk_high->unknown_1h` score `1.5515` n `61` status `ready` deltaP `3.9192` edge `0.1378` maxDD `-1.1043`
- `market_context_high->fx_24h` score `1.404` n `108` status `ready` deltaP `35.301` edge `0.028` maxDD `-1.7074`
- `risk_on_high->metal_24h` score `0.98` n `65` status `ready` deltaP `27.7136` edge `0.0769` maxDD `-4.548`
- `risk_on_and_context->metal_24h` score `0.98` n `65` status `ready` deltaP `27.7136` edge `0.0769` maxDD `-4.548`
- `risk_on_high->commodity_24h` score `0.7742` n `65` status `ready` deltaP `9.383` edge `0.1355` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.7742` n `65` status `ready` deltaP `9.383` edge `0.1355` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
