# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T23:37:08.374379+00:00`
- Price records: `672`
- Market context records: `8036`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11832`

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

- `market_context_high->equity_24h` score `16.5007` n `85` status `ready` deltaP `26.0007` edge `1.3181` maxDD `-5.6434`
- `market_context_high->metal_24h` score `7.9328` n `85` status `ready` deltaP `35.8752` edge `0.4219` maxDD `0.0`
- `market_context_high->equity_4h` score `6.4891` n `98` status `ready` deltaP `25.6409` edge `0.4591` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4186` n `85` status `ready` deltaP `25.6907` edge `0.2374` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.5964` n `98` status `ready` deltaP `23.2951` edge `0.1233` maxDD `-0.979`
- `market_context_high->index_4h` score `2.5332` n `98` status `ready` deltaP `26.3688` edge `0.0713` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.8673` n `85` status `ready` deltaP `10.1601` edge `0.1549` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6349` n `98` status `ready` deltaP `13.4547` edge `0.1283` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.3685` n `85` status `ready` deltaP `24.9016` edge `0.0363` maxDD `-2.0616`
- `market_context_high->index_1h` score `0.7989` n `98` status `ready` deltaP `13.3325` edge `0.0207` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7516` n `98` status `ready` deltaP `10.5707` edge `0.03` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.482` n `98` status `ready` deltaP `10.476` edge `0.033` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.4758` n `98` status `ready` deltaP `8.7388` edge `0.1532` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.4752` n `98` status `ready` deltaP `5.3727` edge `0.1155` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0917` n `98` status `ready` deltaP `0.5988` edge `0.0275` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.4677` n `98` status `ready` deltaP `4.1376` edge `0.0029` maxDD `-0.8901`
- `market_context_high->fx_1h` score `-0.5146` n `98` status `ready` deltaP `-0.9379` edge `0.0001` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.6473` n `98` status `ready` deltaP `-2.3952` edge `-0.0047` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1971` n `98` status `ready` deltaP `0.2706` edge `-0.0051` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8631` n `98` status `ready` deltaP `7.3475` edge `-0.1619` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
