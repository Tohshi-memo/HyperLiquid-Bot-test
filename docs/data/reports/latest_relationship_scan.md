# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T23:50:00.646334+00:00`
- Price records: `672`
- Market context records: `1267`
- Flow alert records: `5557`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_major_24h` score `17.9677` n `128` status `ready` deltaP `41.5798` edge `1.3333` maxDD `-8.0553`
- `market_context_high->metal_24h` score `9.8941` n `128` status `ready` deltaP `5.2083` edge `0.9565` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.4353` n `128` status `ready` deltaP `24.5659` edge `0.7408` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `8.2638` n `128` status `ready` deltaP `6.1357` edge `0.7694` maxDD `-6.7322`
- `market_context_high->index_24h` score `4.888` n `128` status `ready` deltaP `26.2153` edge `0.3412` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.777` n `128` status `ready` deltaP `19.2263` edge `0.2529` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.7101` n `128` status `ready` deltaP `24.3056` edge `0.5463` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.3046` n `128` status `ready` deltaP `1.5625` edge `0.4546` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `2.1473` n `128` status `ready` deltaP `-11.4583` edge `0.4035` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.887` n `128` status `ready` deltaP `15.2629` edge `0.1238` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.835` n `128` status `ready` deltaP `17.8926` edge `0.0934` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.7278` n `138` status `ready` deltaP `10.0864` edge `0.0251` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7227` n `138` status `ready` deltaP `6.8406` edge `0.0515` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.5372` n `138` status `ready` deltaP `12.7506` edge `0.0208` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.358` n `128` status `ready` deltaP `8.7462` edge `0.1797` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.0547` n `128` status `ready` deltaP `3.2119` edge `0.0296` maxDD `-0.3831`
- `market_context_high->crypto_alt_4h` score `-0.2333` n `128` status `ready` deltaP `9.9275` edge `0.2004` maxDD `-16.7194`
- `market_context_high->crypto_alt_1h` score `-0.3278` n `138` status `ready` deltaP `1.3538` edge `0.036` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.4219` n `138` status `ready` deltaP `1.9526` edge `-0.0026` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.5656` n `138` status `ready` deltaP `1.4493` edge `0.0088` maxDD `-4.9451`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
