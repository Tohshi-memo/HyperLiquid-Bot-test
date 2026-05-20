# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T02:36:16.076760+00:00`
- Price records: `672`
- Market context records: `1279`
- Flow alert records: `5592`
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

- `market_context_high->crypto_major_24h` score `17.8537` n `128` status `ready` deltaP `41.5798` edge `1.3238` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.0045` n `128` status `ready` deltaP `7.1181` edge `1.0363` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.9009` n `128` status `ready` deltaP `25.7812` edge `0.7715` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.3912` n `128` status `ready` deltaP `28.125` edge `0.3704` maxDD `-5.3574`
- `market_context_high->unknown_4h` score `4.686` n `137` status `ready` deltaP `4.2728` edge `0.492` maxDD `-6.7322`
- `market_context_high->equity_24h` score `3.9054` n `128` status `ready` deltaP `25.3472` edge `0.5644` maxDD `-14.2815`
- `market_context_high->equity_4h` score `3.0234` n `137` status `ready` deltaP `15.1916` edge `0.217` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.367` n `128` status `ready` deltaP `1.5625` edge `0.4598` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.5565` n `128` status `ready` deltaP `-13.3681` edge `0.367` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.3607` n `137` status `ready` deltaP `10.4838` edge `0.1118` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.6956` n `137` status `ready` deltaP `16.7193` edge `0.0896` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.5522` n `149` status `ready` deltaP `5.8092` edge `0.05` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.4788` n `149` status `ready` deltaP `7.905` edge `0.0244` maxDD `-0.9758`
- `market_context_high->metal_1h` score `0.4066` n `149` status `ready` deltaP `11.5079` edge `0.0182` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.2145` n `128` status `ready` deltaP `4.7744` edge `0.0325` maxDD `-0.3831`
- `market_context_high->crypto_alt_1h` score `-0.2312` n `149` status `ready` deltaP `2.1169` edge `0.0433` maxDD `-3.6309`
- `market_context_high->crypto_major_4h` score `-0.3467` n `137` status `ready` deltaP `6.0697` edge `0.15` maxDD `-11.793`
- `market_context_high->fx_1h` score `-0.5856` n `149` status `ready` deltaP `0.1758` edge `-0.0044` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.6811` n `149` status `ready` deltaP `0.862` edge `0.009` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8344` n `137` status `ready` deltaP `8.1127` edge `0.1709` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
