# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T23:37:23.354313+00:00`
- Price records: `672`
- Market context records: `1266`
- Flow alert records: `5554`
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

- `market_context_high->crypto_major_24h` score `17.9665` n `128` status `ready` deltaP `41.5798` edge `1.3332` maxDD `-8.0553`
- `market_context_high->metal_24h` score `9.7722` n `128` status `ready` deltaP `5.0347` edge `0.9475` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.3698` n `128` status `ready` deltaP `24.3923` edge `0.7365` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `8.2638` n `128` status `ready` deltaP `6.1357` edge `0.7694` maxDD `-6.7322`
- `market_context_high->index_24h` score `4.8297` n `128` status `ready` deltaP `26.0417` edge `0.3375` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.7566` n `128` status `ready` deltaP `19.2263` edge `0.2512` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.673` n `128` status `ready` deltaP `24.1319` edge `0.5427` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `2.301` n `128` status `ready` deltaP `1.5625` edge `0.4543` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `2.2284` n `128` status `ready` deltaP `-11.2847` edge `0.4091` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.8642` n `128` status `ready` deltaP `15.2629` edge `0.1219` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.8218` n `128` status `ready` deltaP `17.8926` edge `0.0923` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.6965` n `137` status `ready` deltaP `9.8748` edge `0.0239` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6906` n `137` status `ready` deltaP `6.6185` edge `0.0503` maxDD `-1.2834`
- `market_context_high->metal_1h` score `0.4953` n `137` status `ready` deltaP `12.5126` edge `0.0189` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `0.3329` n `128` status `ready` deltaP `8.5938` edge `0.1775` maxDD `-8.3693`
- `market_context_high->fx_24h` score `0.071` n `128` status `ready` deltaP `3.3855` edge `0.0298` maxDD `-0.3831`
- `market_context_high->crypto_alt_4h` score `-0.2553` n `128` status `ready` deltaP `9.7751` edge `0.1986` maxDD `-16.7194`
- `market_context_high->crypto_alt_1h` score `-0.3654` n `137` status `ready` deltaP `1.0206` edge `0.0334` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.3877` n `137` status `ready` deltaP `2.3493` edge `-0.0024` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.6028` n `137` status `ready` deltaP `1.0949` edge `0.0064` maxDD `-4.9451`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
