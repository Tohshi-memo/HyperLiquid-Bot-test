# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T17:22:18.885215+00:00`
- Price records: `672`
- Market context records: `1240`
- Flow alert records: `5477`
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

- `market_context_high->crypto_major_24h` score `18.6396` n `128` status `ready` deltaP `43.6631` edge `1.3754` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `8.0331` n `128` status `ready` deltaP `4.9162` edge `0.7583` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.8133` n `128` status `ready` deltaP `22.6562` edge `0.7017` maxDD `-15.1306`
- `market_context_high->metal_24h` score `7.1558` n `128` status `ready` deltaP `0.6944` edge `0.7584` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `4.09` n `128` status `ready` deltaP `-6.9444` edge `0.5353` maxDD `-6.8535`
- `market_context_high->index_24h` score `3.7438` n `128` status `ready` deltaP `22.7431` edge `0.269` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.476` n `128` status `ready` deltaP `17.5495` edge `0.239` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.195` n `128` status `ready` deltaP `22.3958` edge `0.493` maxDD `-14.2815`
- `market_context_high->unknown_24h` score `1.7622` n `128` status `ready` deltaP `1.5625` edge `0.4094` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.6371` n `128` status `ready` deltaP `14.0434` edge `0.1111` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.696` n `128` status `ready` deltaP `10.0487` edge `0.0227` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5559` n `128` status `ready` deltaP `5.3096` edge `0.0478` maxDD `-1.2834`
- `market_context_high->fx_24h` score `0.4544` n `128` status `ready` deltaP `6.8577` edge `0.0386` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1899` n `128` status `ready` deltaP `15.4536` edge `0.0559` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.1754` n `128` status `ready` deltaP `10.2685` edge `0.0072` maxDD `-2.2164`
- `market_context_high->crypto_major_4h` score `-0.0369` n `128` status `ready` deltaP `6.6121` edge `0.1433` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.0629` n `128` status `ready` deltaP `6.0489` edge `0.0` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.3087` n `128` status `ready` deltaP `0.6456` edge `0.0404` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4487` n `128` status `ready` deltaP `1.9274` edge `0.0062` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.6912` n `128` status `ready` deltaP `7.9458` edge `0.1549` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
