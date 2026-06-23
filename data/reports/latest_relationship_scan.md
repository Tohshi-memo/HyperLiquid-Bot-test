# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T17:42:33.907261+00:00`
- Price records: `672`
- Market context records: `4539`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9932`

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

- `market_context_high->unknown_1h` score `54.9319` n `175` status `ready` deltaP `7.5757` edge `4.5772` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.3654` n `173` status `ready` deltaP `8.452` edge `2.6307` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.5236` n `173` status `ready` deltaP `5.8976` edge `0.0018` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.5566` n `175` status `ready` deltaP `0.8041` edge `0.0152` maxDD `-3.0206`
- `market_context_high->fx_1h` score `-0.6707` n `175` status `ready` deltaP `0.4499` edge `-0.003` maxDD `-1.1377`
- `market_context_high->equity_4h` score `-1.0242` n `173` status `ready` deltaP `4.0753` edge `0.0644` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.0252` n `175` status `ready` deltaP `-2.9803` edge `-0.0107` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0594` n `175` status `ready` deltaP `-1.3481` edge `0.0194` maxDD `-5.5624`
- `market_context_high->index_4h` score `-1.2592` n `173` status `ready` deltaP `-0.6635` edge `-0.0114` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.5334` n `173` status `ready` deltaP `1.1587` edge `0.0185` maxDD `-10.1583`
- `market_context_high->unknown_24h` score `-2.6836` n `173` status `ready` deltaP `2.2198` edge `-0.1461` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4871` n `175` status `ready` deltaP `-4.8024` edge `-0.074` maxDD `-18.0993`
- `market_context_high->crypto_alt_1h` score `-5.3259` n `175` status `ready` deltaP `-3.225` edge `-0.0936` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.5164` n `173` status `ready` deltaP `-13.8107` edge `-0.0164` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.6967` n `173` status `ready` deltaP `-8.5139` edge `-0.1361` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.2015` n `175` status `ready` deltaP `-3.9461` edge `-0.1152` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.3661` n `173` status `ready` deltaP `4.2901` edge `0.015` maxDD `-46.5954`
- `market_context_high->crypto_alt_4h` score `-13.2453` n `173` status `ready` deltaP `-1.3878` edge `-0.2288` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.5571` n `173` status `ready` deltaP `-0.7707` edge `-0.265` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.5533` n `173` status `ready` deltaP `-7.7717` edge `-0.3094` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
