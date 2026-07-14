# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T07:37:28.274410+00:00`
- Price records: `672`
- Market context records: `6688`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `1.4265` n `194` status `ready` deltaP `-5.0883` edge `0.2429` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.7662` n `194` status `ready` deltaP `11.0807` edge `0.1768` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.3905` n `194` status `ready` deltaP `9.5438` edge `0.0549` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `0.2337` n `194` status `ready` deltaP `-2.0565` edge `0.4189` maxDD `-12.3511`
- `market_context_high->crypto_alt_1h` score `0.1389` n `194` status `ready` deltaP `6.2844` edge `0.0461` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2587` n `194` status `ready` deltaP `2.3628` edge `0.0013` maxDD `-0.6845`
- `market_context_high->index_1h` score `-0.4589` n `194` status `ready` deltaP `1.1976` edge `0.0046` maxDD `-0.7136`
- `market_context_high->equity_1h` score `-0.5201` n `194` status `ready` deltaP `4.0234` edge `0.0092` maxDD `-3.8827`
- `market_context_high->commodity_1h` score `-0.5568` n `194` status `ready` deltaP `0.8133` edge `-0.0085` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.5788` n `194` status `ready` deltaP `-3.3582` edge `0.0007` maxDD `-1.2017`
- `market_context_high->index_4h` score `-0.8883` n `194` status `ready` deltaP `10.6943` edge `0.0028` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.4097` n `194` status `ready` deltaP `6.1479` edge `-0.0008` maxDD `-3.3405`
- `market_context_high->crypto_major_4h` score `-1.4659` n `194` status `ready` deltaP `8.5523` edge `0.0865` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.6065` n `194` status `ready` deltaP `-3.1934` edge `-0.0352` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.7353` n `194` status `ready` deltaP `6.3019` edge `0.0757` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.13` n `194` status `ready` deltaP `-1.2352` edge `0.0212` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-2.2887` n `194` status `ready` deltaP `-15.1889` edge `0.1511` maxDD `-10.5788`
- `market_context_high->equity_4h` score `-3.2942` n `194` status `ready` deltaP `7.3469` edge `-0.0444` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.6325` n `194` status `ready` deltaP `-11.0914` edge `-0.008` maxDD `-9.3276`
- `market_context_high->metal_24h` score `-7.0329` n `194` status `ready` deltaP `-6.7404` edge `-0.0082` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
