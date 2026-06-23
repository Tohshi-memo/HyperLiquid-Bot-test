# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T19:07:31.028328+00:00`
- Price records: `672`
- Market context records: `4545`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10093`

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

- `market_context_high->unknown_1h` score `56.9616` n `169` status `ready` deltaP `7.2973` edge `4.7482` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.0741` n `168` status `ready` deltaP `7.8252` edge `2.6106` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4386` n `168` status `ready` deltaP `7.4115` edge `0.0026` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.6481` n `169` status `ready` deltaP `0.6378` edge `-0.0028` maxDD `-1.1038`
- `market_context_high->commodity_1h` score `-0.6709` n `169` status `ready` deltaP `-0.9735` edge `0.0124` maxDD `-3.0206`
- `market_context_high->index_4h` score `-0.9693` n `168` status `ready` deltaP `0.9364` edge `-0.0099` maxDD `-5.9823`
- `market_context_high->equity_4h` score `-1.0295` n `168` status `ready` deltaP `3.2592` edge `0.0694` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.0655` n `169` status `ready` deltaP `-3.5751` edge `-0.0119` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.0738` n `169` status `ready` deltaP `-2.1135` edge `0.0233` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-2.077` n `168` status `ready` deltaP `2.1269` edge `0.0235` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-2.6962` n `167` status `ready` deltaP `2.6177` edge `-0.1498` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.6068` n `169` status `ready` deltaP `-5.0083` edge `-0.0826` maxDD `-18.0993`
- `market_context_high->fx_24h` score `-5.3993` n `167` status `ready` deltaP `-12.6477` edge `-0.0144` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.4949` n `169` status `ready` deltaP `-3.7177` edge `-0.1044` maxDD `-22.2982`
- `market_context_high->index_24h` score `-5.6848` n `167` status `ready` deltaP `-9.0507` edge `-0.131` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.4321` n `169` status `ready` deltaP `-5.0438` edge `-0.1271` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-8.1239` n `167` status `ready` deltaP `4.9973` edge `0.0139` maxDD `-45.2699`
- `market_context_high->crypto_alt_4h` score `-13.3579` n `168` status `ready` deltaP `-2.1051` edge `-0.2334` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.3717` n `167` status `ready` deltaP `-0.9543` edge `-0.24` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.6655` n `168` status `ready` deltaP `-7.4187` edge `-0.3211` maxDD `-68.4587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
