# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T20:22:21.201578+00:00`
- Price records: `672`
- Market context records: `1253`
- Flow alert records: `5514`
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

- `market_context_high->crypto_major_24h` score `18.0766` n `128` status `ready` deltaP `42.1006` edge `1.3389` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.34` n `128` status `ready` deltaP `2.7778` edge `0.8432` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `7.9974` n `128` status `ready` deltaP `5.221` edge `0.7533` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.6794` n `128` status `ready` deltaP `22.4826` edge `0.6917` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.132` n `128` status `ready` deltaP `23.7847` edge `0.2944` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.3056` n `128` status `ready` deltaP `17.5495` edge `0.2248` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.2871` n `128` status `ready` deltaP `22.3958` edge `0.5048` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `3.2538` n `128` status `ready` deltaP `-9.0278` edge `0.4795` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.0742` n `128` status `ready` deltaP `1.5625` edge `0.4354` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.4913` n `128` status `ready` deltaP `13.5861` edge `0.102` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7691` n `128` status `ready` deltaP `10.6475` edge `0.0248` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.7296` n `128` status `ready` deltaP `6.6569` edge `0.0533` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.3732` n `128` status `ready` deltaP `11.7655` edge `0.0137` maxDD `-2.2164`
- `market_context_high->metal_4h` score `0.3529` n `128` status `ready` deltaP `16.2158` edge `0.0644` maxDD `-6.4478`
- `market_context_high->fx_24h` score `0.2399` n `128` status `ready` deltaP `5.1216` edge `0.0323` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `-0.0008` n `128` status `ready` deltaP `6.917` edge `0.1459` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1301` n `128` status `ready` deltaP `5.4501` edge `-0.0016` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2721` n `128` status `ready` deltaP `1.0947` edge `0.0421` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.412` n `128` status `ready` deltaP `2.3765` edge `0.0079` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6505` n `128` status `ready` deltaP `8.0983` edge `0.1591` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
