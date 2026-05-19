# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T12:52:17.290096+00:00`
- Price records: `672`
- Market context records: `1221`
- Flow alert records: `5421`
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

- `market_context_high->crypto_major_24h` score `18.9449` n `128` status `ready` deltaP `44.7048` edge `1.3939` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.7707` n `128` status `ready` deltaP `3.3918` edge `0.7466` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.3537` n `128` status `ready` deltaP `22.6562` edge `0.6634` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `5.4716` n `128` status `ready` deltaP `-3.8194` edge `0.6296` maxDD `-6.8535`
- `market_context_high->metal_24h` score `5.0302` n `128` status `ready` deltaP `-2.4306` edge `0.6021` maxDD `-6.3373`
- `market_context_high->equity_4h` score `3.1935` n `128` status `ready` deltaP `16.1775` edge `0.2246` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.6497` n `128` status `ready` deltaP `19.7917` edge `0.1975` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3932` n `128` status `ready` deltaP `19.9653` edge `0.4064` maxDD `-14.2815`
- `market_context_high->index_4h` score `1.2011` n `128` status `ready` deltaP `11.9092` edge `0.089` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.8617` n `128` status `ready` deltaP `9.1146` edge `0.0575` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.642` n `128` status `ready` deltaP `9.7493` edge `0.0202` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5679` n `128` status `ready` deltaP `5.0102` edge `0.0508` maxDD `-1.2834`
- `market_context_high->unknown_24h` score `0.1891` n `128` status `ready` deltaP `-0.5208` edge `0.2922` maxDD `-10.1706`
- `market_context_high->metal_1h` score `-0.0309` n `128` status `ready` deltaP `9.8194` edge `-0.007` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.0893` n `128` status `ready` deltaP `5.5998` edge `0.0008` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1634` n `128` status `ready` deltaP `5.545` edge `0.1342` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3079` n `128` status `ready` deltaP `0.945` edge `0.0385` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.391` n `128` status `ready` deltaP `2.8256` edge `0.0076` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.7679` n `128` status `ready` deltaP `-2.311` edge `0.0129` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.8204` n `128` status `ready` deltaP `12.7097` edge `-0.01` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
