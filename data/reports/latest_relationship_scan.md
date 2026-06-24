# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T05:22:32.440628+00:00`
- Price records: `672`
- Market context records: `4590`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9937`

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

- `market_context_high->unknown_1h` score `66.8911` n `151` status `ready` deltaP `6.2409` edge `5.5827` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.8898` n `151` status `ready` deltaP `7.9935` edge `0.3919` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.4921` n `151` status `ready` deltaP `2.0234` edge `0.0251` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.6694` n `151` status `ready` deltaP `3.2274` edge `0.0009` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.828` n `151` status `ready` deltaP `-1.4603` edge `-0.0038` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8734` n `151` status `ready` deltaP `1.7707` edge `-0.0115` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9718` n `151` status `ready` deltaP `-3.5383` edge `-0.0023` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1766` n `151` status `ready` deltaP `3.8271` edge `0.0344` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.5022` n `151` status `ready` deltaP `0.3937` edge `-0.0183` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6949` n `151` status `ready` deltaP `-4.1371` edge `-0.0128` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.6433` n `149` status `ready` deltaP `1.764` edge `-0.1397` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.944` n `151` status `ready` deltaP `-4.0459` edge `-0.0853` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7446` n `149` status `ready` deltaP `10.278` edge `0.061` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.4086` n `149` status `ready` deltaP `-13.2586` edge `-0.0111` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.4911` n `151` status `ready` deltaP `-2.0641` edge `-0.1151` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7951` n `151` status `ready` deltaP `-6.101` edge `-0.1503` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3282` n `149` status `ready` deltaP `-7.4303` edge `-0.107` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.0857` n `151` status `ready` deltaP `-3.7373` edge `-0.2742` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2242` n `151` status `ready` deltaP `-6.4065` edge `-0.3467` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.0998` n `151` status `ready` deltaP `-4.0472` edge `-0.4299` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
