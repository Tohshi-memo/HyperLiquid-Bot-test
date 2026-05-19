# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T15:37:25.959861+00:00`
- Price records: `672`
- Market context records: `1233`
- Flow alert records: `5455`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8788`

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

- `market_context_high->crypto_major_24h` score `18.8156` n `128` status `ready` deltaP `44.184` edge `1.3866` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.8913` n `128` status `ready` deltaP `3.8491` edge `0.7536` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.6693` n `128` status `ready` deltaP `22.6562` edge `0.6897` maxDD `-15.1306`
- `market_context_high->metal_24h` score `6.3985` n `128` status `ready` deltaP `-0.5208` edge `0.7034` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.5424` n `128` status `ready` deltaP `-5.7292` edge `0.5649` maxDD `-6.8535`
- `market_context_high->equity_4h` score `3.4892` n `128` status `ready` deltaP `17.5495` edge `0.2401` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.4193` n `128` status `ready` deltaP `21.7014` edge `0.2489` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.0432` n `128` status `ready` deltaP `21.875` edge `0.477` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.5379` n `128` status `ready` deltaP `13.4336` edge `0.1069` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `1.1684` n `128` status `ready` deltaP `0.6944` edge `0.3657` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.732` n `128` status `ready` deltaP `10.1984` edge `0.0247` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.6746` n `128` status `ready` deltaP `5.609` edge `0.0557` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.5289` n `128` status `ready` deltaP `7.2049` edge `0.0425` maxDD `-0.3831`
- `market_context_high->metal_1h` score `0.1502` n `128` status `ready` deltaP `10.2685` edge `0.0051` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0581` n `128` status `ready` deltaP `6.0489` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1115` n `128` status `ready` deltaP `6.0023` edge `0.1378` maxDD `-8.3693`
- `market_context_high->metal_4h` score `-0.1631` n `128` status `ready` deltaP `14.3865` edge `0.0336` maxDD `-6.4478`
- `market_context_high->crypto_alt_1h` score `-0.3297` n `128` status `ready` deltaP `0.4959` edge `0.0387` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4284` n `128` status `ready` deltaP `2.2268` edge `0.0068` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.8276` n `128` status `ready` deltaP `7.1836` edge `0.1425` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
