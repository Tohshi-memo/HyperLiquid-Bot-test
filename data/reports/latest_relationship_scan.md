# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T12:22:17.587939+00:00`
- Price records: `672`
- Market context records: `1219`
- Flow alert records: `5415`
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

- `market_context_high->crypto_major_24h` score `18.9178` n `128` status `ready` deltaP `44.5312` edge `1.3928` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.7139` n `128` status `ready` deltaP `3.0869` edge `0.7439` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.2491` n `128` status `ready` deltaP `22.309` edge `0.657` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `5.6554` n `128` status `ready` deltaP `-3.4722` edge `0.6426` maxDD `-6.8535`
- `market_context_high->metal_24h` score `4.826` n `128` status `ready` deltaP `-2.7778` edge `0.5874` maxDD `-6.3373`
- `market_context_high->equity_4h` score `3.1307` n `128` status `ready` deltaP `15.8727` edge `0.2214` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.5067` n `128` status `ready` deltaP `19.4444` edge `0.1879` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2417` n `128` status `ready` deltaP `19.6181` edge `0.3893` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.1515` n `128` status `ready` deltaP `11.6044` edge `0.0869` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.9195` n `128` status `ready` deltaP `9.4619` edge `0.06` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.6408` n `128` status `ready` deltaP `9.7493` edge `0.0201` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5655` n `128` status `ready` deltaP `5.0102` edge `0.0506` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.0391` n `128` status `ready` deltaP `-0.5208` edge `0.2797` maxDD `-10.1706`
- `market_context_high->metal_1h` score `-0.0333` n `128` status `ready` deltaP `9.8194` edge `-0.0072` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1156` n `128` status `ready` deltaP `5.3004` edge `0.0006` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1611` n `128` status `ready` deltaP `5.545` edge `0.1345` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3071` n `128` status `ready` deltaP `0.945` edge `0.0386` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3778` n `128` status `ready` deltaP `2.9753` edge `0.0083` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.7895` n `128` status `ready` deltaP `-2.4607` edge `0.0121` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.8796` n `128` status `ready` deltaP `12.4048` edge `-0.0129` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
