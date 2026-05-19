# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T11:22:18.073151+00:00`
- Price records: `672`
- Market context records: `1214`
- Flow alert records: `5402`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8777`

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

- `market_context_high->crypto_major_24h` score `18.8365` n `128` status `ready` deltaP `44.0104` edge `1.3895` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.6561` n `128` status `ready` deltaP `2.9345` edge `0.7401` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.0522` n `128` status `ready` deltaP `21.9618` edge `0.6429` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `6.0074` n `128` status `ready` deltaP `-2.7778` edge `0.6673` maxDD `-6.8535`
- `market_context_high->metal_24h` score `4.4296` n `128` status `ready` deltaP `-3.4722` edge `0.559` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.9487` n `128` status `ready` deltaP `15.2629` edge `0.2103` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.2184` n `128` status `ready` deltaP `18.75` edge `0.1685` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.9373` n `128` status `ready` deltaP `18.9236` edge `0.3549` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.0439` n `128` status `ready` deltaP `10.9946` edge `0.082` maxDD `-2.1308`
- `market_context_high->fx_24h` score `1.0338` n `128` status `ready` deltaP `10.1563` edge `0.0649` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.5929` n `128` status `ready` deltaP `9.3001` edge `0.0191` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4828` n `128` status `ready` deltaP `4.4114` edge `0.0477` maxDD `-1.2834`
- `market_context_high->metal_1h` score `-0.0549` n `128` status `ready` deltaP `9.6697` edge `-0.008` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1168` n `128` status `ready` deltaP `5.3004` edge `0.0005` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1852` n `128` status `ready` deltaP `5.545` edge `0.1314` maxDD `-8.3693`
- `market_context_high->unknown_24h` score `-0.2117` n `128` status `ready` deltaP `-0.5208` edge `0.2588` maxDD `-10.1706`
- `market_context_high->crypto_alt_1h` score `-0.3804` n `128` status `ready` deltaP `0.3462` edge `0.0332` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4323` n `128` status `ready` deltaP `2.3765` edge `0.0053` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.7847` n `128` status `ready` deltaP `-2.4607` edge `0.0125` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.998` n `128` status `ready` deltaP `11.795` edge `-0.0187` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
