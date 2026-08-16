# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T22:22:22.945603+00:00`
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

- `market_context_high->unknown_24h` score `134.4385` n `82` status `ready` deltaP `-28.0107` edge `17.6908` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `6.373` n `82` status `ready` deltaP `40.2651` edge `0.2684` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `0.9852` n `114` status `ready` deltaP `11.5212` edge `0.0524` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.2465` n `118` status `ready` deltaP `1.2433` edge `0.0123` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.3669` n `118` status `ready` deltaP `0.647` edge `0.0016` maxDD `-0.2527`
- `market_context_high->metal_4h` score `-0.3862` n `114` status `ready` deltaP `12.9306` edge `0.005` maxDD `-4.5909`
- `market_context_high->fx_4h` score `-0.3923` n `114` status `ready` deltaP `3.5515` edge `0.0041` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.4793` n `118` status `ready` deltaP `2.0425` edge `-0.0035` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.6219` n `118` status `ready` deltaP `-3.8947` edge `-0.0016` maxDD `-0.5064`
- `market_context_high->crypto_major_4h` score `-0.8981` n `114` status `ready` deltaP `1.602` edge `-0.0155` maxDD `-4.4923`
- `market_context_high->index_4h` score `-1.0745` n `114` status `ready` deltaP `-7.8091` edge `-0.0048` maxDD `-0.8045`
- `market_context_high->index_24h` score `-1.2598` n `82` status `ready` deltaP `3.9211` edge `-0.0509` maxDD `-1.0844`
- `market_context_high->fx_24h` score `-2.0458` n `82` status `ready` deltaP `-15.2904` edge `0.0004` maxDD `-1.8596`
- `market_context_high->crypto_major_24h` score `-2.1207` n `82` status `ready` deltaP `-4.1836` edge `0.0972` maxDD `-20.2955`
- `market_context_high->metal_24h` score `-2.2573` n `82` status `ready` deltaP `-13.5459` edge `0.0521` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-2.5658` n `118` status `ready` deltaP `-5.9322` edge `-0.0386` maxDD `-7.1871`
- `market_context_high->equity_1h` score `-2.5709` n `118` status `ready` deltaP `-10.7759` edge `-0.0448` maxDD `-4.4748`
- `market_context_high->crypto_major_1h` score `-2.5869` n `118` status `ready` deltaP `-6.7797` edge `-0.0437` maxDD `-6.1342`
- `market_context_high->crypto_alt_4h` score `-5.8417` n `114` status `ready` deltaP `-8.0097` edge `-0.0537` maxDD `-17.7101`
- `market_context_high->unknown_1h` score `-6.7036` n `118` status `ready` deltaP `2.1415` edge `-0.5332` maxDD `-0.8437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
