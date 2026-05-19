# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T20:07:22.193538+00:00`
- Price records: `672`
- Market context records: `1252`
- Flow alert records: `5511`
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

- `market_context_high->crypto_major_24h` score `18.1018` n `128` status `ready` deltaP `42.1006` edge `1.341` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.2409` n `128` status `ready` deltaP `2.6042` edge `0.8361` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `8.0023` n `128` status `ready` deltaP `5.221` edge `0.7537` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.6583` n `128` status `ready` deltaP `22.309` edge `0.6911` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.0845` n `128` status `ready` deltaP `23.6111` edge `0.2916` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `3.3348` n `128` status `ready` deltaP `-8.8542` edge `0.4851` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.3104` n `128` status `ready` deltaP `17.5495` edge `0.2252` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.2707` n `128` status `ready` deltaP `22.3958` edge `0.5027` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.0634` n `128` status `ready` deltaP `1.5625` edge `0.4345` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5083` n `128` status `ready` deltaP `13.7385` edge `0.1024` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7523` n `128` status `ready` deltaP `10.4978` edge `0.0244` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7141` n `128` status `ready` deltaP `6.5072` edge `0.053` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.3708` n `128` status `ready` deltaP `11.7655` edge `0.0135` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.3275` n `128` status `ready` deltaP `16.0633` edge `0.0633` maxDD `-6.4478`
- `market_context_high->fx_24h` score `0.2598` n `128` status `ready` deltaP `5.2952` edge `0.0328` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `-0.0031` n `128` status `ready` deltaP `6.917` edge `0.1456` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1145` n `128` status `ready` deltaP `5.5998` edge `-0.0013` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2572` n `128` status `ready` deltaP `1.2444` edge `0.043` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3996` n `128` status `ready` deltaP `2.5262` edge `0.0085` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6552` n `128` status `ready` deltaP `8.0983` edge `0.1585` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
