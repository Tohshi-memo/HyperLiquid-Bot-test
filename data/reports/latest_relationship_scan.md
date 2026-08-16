# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T22:07:33.021610+00:00`
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

- `market_context_high->unknown_24h` score `142.9489` n `82` status `ready` deltaP `-26.9648` edge `18.7749` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `6.5959` n `82` status `ready` deltaP `41.311` edge `0.28` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.0124` n `115` status `ready` deltaP `11.6663` edge `0.0537` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.1691` n `118` status `ready` deltaP `1.941` edge `0.0141` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.3099` n `118` status `ready` deltaP `1.3448` edge `0.0017` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.3558` n `115` status `ready` deltaP `3.9024` edge `0.0048` maxDD `-0.504`
- `market_context_high->metal_4h` score `-0.4335` n `115` status `ready` deltaP `12.3661` edge `0.0027` maxDD `-4.5909`
- `market_context_high->metal_1h` score `-0.484` n `118` status `ready` deltaP `2.0425` edge `-0.0041` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.6628` n `118` status `ready` deltaP `-4.5925` edge `-0.0022` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.0927` n `115` status `ready` deltaP `-8.1297` edge `-0.005` maxDD `-0.8045`
- `market_context_high->index_24h` score `-1.4255` n `82` status `ready` deltaP `2.8752` edge `-0.0525` maxDD `-1.1704`
- `market_context_high->crypto_major_4h` score `-1.6321` n `115` status `ready` deltaP `1.1519` edge `-0.0223` maxDD `-5.3779`
- `market_context_high->fx_24h` score `-1.9688` n `82` status `ready` deltaP `-14.2446` edge `0.0033` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.1803` n `82` status `ready` deltaP `-12.5` edge `0.055` maxDD `-7.0954`
- `market_context_high->crypto_major_24h` score `-2.3008` n `82` status `ready` deltaP `-4.1836` edge `0.0917` maxDD `-21.3691`
- `market_context_high->crypto_alt_1h` score `-2.532` n `118` status `ready` deltaP `-5.9322` edge `-0.0375` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.5622` n `118` status `ready` deltaP `-6.7797` edge `-0.0444` maxDD `-6.2467`
- `market_context_high->equity_1h` score `-2.6342` n `118` status `ready` deltaP `-10.7759` edge `-0.0466` maxDD `-4.7529`
- `market_context_high->crypto_alt_4h` score `-6.061` n `115` status `ready` deltaP `-8.3682` edge `-0.0595` maxDD `-18.5167`
- `market_context_high->unknown_1h` score `-6.5974` n `118` status `ready` deltaP `2.8392` edge `-0.529` maxDD `-0.8437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
