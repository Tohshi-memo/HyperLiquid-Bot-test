# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T00:52:13.413430+00:00`
- Price records: `672`
- Market context records: `1272`
- Flow alert records: `5570`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `18.0157` n `128` status `ready` deltaP `41.5798` edge `1.3373` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.3696` n `128` status `ready` deltaP `5.9028` edge `0.9915` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.7104` n `128` status `ready` deltaP `25.2604` edge `0.7591` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `7.4199` n `130` status `ready` deltaP `5.9521` edge `0.7003` maxDD `-6.7322`
- `market_context_high->index_24h` score `5.1416` n `128` status `ready` deltaP `26.9097` edge `0.3577` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8624` n `128` status `ready` deltaP `25.0` edge `0.5612` maxDD `-14.2815`
- `market_context_high->equity_4h` score `3.6739` n `130` status `ready` deltaP `18.478` edge `0.2493` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3538` n `128` status `ready` deltaP `1.5625` edge `0.4587` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.878` n `130` status `ready` deltaP `14.6107` edge `0.1274` maxDD `-2.1308`
- `market_context_high->commodity_24h` score `1.859` n `128` status `ready` deltaP `-12.1528` edge `0.3841` maxDD `-6.8535`
- `market_context_high->metal_4h` score `0.9632` n `130` status `ready` deltaP `18.4897` edge `0.1001` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.5459` n `142` status `ready` deltaP `12.5601` edge `0.0228` maxDD `-2.2164`
- `market_context_high->index_1h` score `0.5446` n `142` status `ready` deltaP `8.6848` edge `0.0236` maxDD `-0.8889`
- `market_context_high->equity_1h` score `0.4595` n `142` status `ready` deltaP `5.4799` edge `0.0442` maxDD `-1.7287`
- `market_context_high->crypto_major_4h` score `0.257` n `130` status `ready` deltaP `8.5507` edge `0.1803` maxDD `-9.3482`
- `market_context_high->fx_24h` score `0.0849` n `128` status `ready` deltaP `3.5591` edge `0.0298` maxDD `-0.3831`
- `market_context_high->crypto_alt_1h` score `-0.3459` n `142` status `ready` deltaP `0.9762` edge `0.0362` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.3621` n `142` status `ready` deltaP `2.6398` edge `-0.0022` maxDD `-0.3124`
- `market_context_high->crypto_alt_4h` score `-0.3624` n `130` status `ready` deltaP `9.5638` edge `0.1977` maxDD `-17.6335`
- `market_context_high->crypto_major_1h` score `-0.7236` n `142` status `ready` deltaP `0.5988` edge `0.003` maxDD `-5.6474`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
