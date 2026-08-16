# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T20:22:26.483384+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `199.0244` n `83` status `ready` deltaP `-25.1401` edge `25.9519` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.5222` n `83` status `ready` deltaP `41.3404` edge `0.357` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.2342` n `119` status `ready` deltaP `12.6537` edge `0.0656` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `0.0408` n `122` status `ready` deltaP `3.6345` edge `0.0203` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.2352` n `119` status `ready` deltaP `5.0945` edge `0.0069` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.319` n `122` status `ready` deltaP `1.2614` edge `0.0015` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5597` n `122` status `ready` deltaP `0.962` edge `-0.0066` maxDD `-1.7257`
- `market_context_high->metal_4h` score `-0.6318` n `119` status `ready` deltaP `10.2032` edge `-0.0083` maxDD `-4.5909`
- `market_context_high->index_1h` score `-1.1506` n `122` status `ready` deltaP `-6.1377` edge `-0.0028` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.205` n `119` status `ready` deltaP `-10.02` edge `-0.0068` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-1.5294` n `83` status `ready` deltaP `-8.6303` edge `0.0222` maxDD `-1.8596`
- `market_context_high->index_24h` score `-1.6614` n `83` status `ready` deltaP `-4.0788` edge `-0.0628` maxDD `-1.8403`
- `market_context_high->metal_24h` score `-2.0057` n `83` status `ready` deltaP `-10.8664` edge `0.0665` maxDD `-7.0954`
- `market_context_high->crypto_major_1h` score `-2.1351` n `122` status `ready` deltaP `-5.5168` edge `-0.0345` maxDD `-5.5318`
- `market_context_high->crypto_alt_1h` score `-2.2332` n `122` status `ready` deltaP `-4.0272` edge `-0.0253` maxDD `-7.0497`
- `market_context_high->equity_1h` score `-2.6623` n `122` status `ready` deltaP `-10.6925` edge `-0.0466` maxDD `-4.9849`
- `market_context_high->crypto_major_4h` score `-2.8742` n `119` status `ready` deltaP `-0.5726` edge `-0.0516` maxDD `-10.3949`
- `market_context_high->crypto_major_24h` score `-3.6066` n `83` status `ready` deltaP `-4.7273` edge `0.0386` maxDD `-27.8908`
- `market_context_high->unknown_1h` score `-6.782` n `122` status `ready` deltaP `2.1523` edge `-0.5398` maxDD `-0.8437`
- `market_context_high->crypto_alt_4h` score `-7.3703` n `119` status `ready` deltaP `-9.742` edge `-0.0901` maxDD `-24.0651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
