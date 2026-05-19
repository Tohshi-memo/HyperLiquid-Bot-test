# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T19:22:15.902731+00:00`
- Price records: `672`
- Market context records: `1248`
- Flow alert records: `5501`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_major_24h` score `18.2092` n `128` status `ready` deltaP `42.2743` edge `1.3488` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.9806` n `128` status `ready` deltaP `5.221` edge `0.7519` maxDD `-6.7322`
- `market_context_high->metal_24h` score `7.9473` n `128` status `ready` deltaP `2.0833` edge `0.8151` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `7.6722` n `128` status `ready` deltaP `22.4826` edge `0.6911` maxDD `-15.1306`
- `market_context_high->index_24h` score `3.942` n `128` status `ready` deltaP `23.0903` edge `0.2832` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.5733` n `128` status `ready` deltaP `-8.3333` edge `0.5015` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.3296` n `128` status `ready` deltaP `17.5495` edge `0.2268` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.2262` n `128` status `ready` deltaP `22.3958` edge `0.497` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.0262` n `128` status `ready` deltaP `1.5625` edge `0.4314` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5531` n `128` status `ready` deltaP `14.0434` edge `0.1041` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6984` n `128` status `ready` deltaP `10.0487` edge `0.0229` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6457` n `128` status `ready` deltaP `6.0581` edge `0.0503` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.3206` n `128` status `ready` deltaP `5.816` edge `0.0344` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.3181` n `128` status `ready` deltaP `11.3164` edge `0.0121` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.2609` n `128` status `ready` deltaP `15.606` edge `0.0608` maxDD `-6.4478`
- `market_context_high->crypto_major_4h` score `-0.0109` n `128` status `ready` deltaP `6.917` edge `0.1446` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0629` n `128` status `ready` deltaP `6.0489` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2541` n `128` status `ready` deltaP `1.2444` edge `0.0434` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4011` n `128` status `ready` deltaP `2.3765` edge `0.0093` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6669` n `128` status `ready` deltaP `8.0983` edge `0.157` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
