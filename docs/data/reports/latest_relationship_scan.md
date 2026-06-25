# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T22:22:34.545697+00:00`
- Price records: `672`
- Market context records: `4766`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7476`

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

- `market_context_high->unknown_1h` score `7.7287` n `128` status `ready` deltaP `13.4122` edge `0.5964` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.0282` n `128` status `ready` deltaP `16.654` edge `0.5957` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.4406` n `113` status `ready` deltaP `13.1576` edge `0.208` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.0796` n `128` status `ready` deltaP `3.7098` edge `0.0274` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `-0.1475` n `128` status `ready` deltaP `9.7751` edge `0.0424` maxDD `-5.1182`
- `market_context_high->equity_4h` score `-0.4621` n `128` status `ready` deltaP `7.2218` edge `0.0612` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.4865` n `128` status `ready` deltaP `5.9261` edge `0.005` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.5341` n `128` status `ready` deltaP `1.2385` edge `0.0009` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.9614` n `128` status `ready` deltaP `0.6643` edge `-0.0078` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.029` n `128` status `ready` deltaP `-2.6245` edge `-0.0033` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.5082` n `128` status `ready` deltaP `-2.6946` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.2161` n `113` status `ready` deltaP `19.4506` edge `0.0971` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2617` n `128` status `ready` deltaP `-0.945` edge `-0.0661` maxDD `-14.0715`
- `market_context_high->crypto_major_1h` score `-3.545` n `128` status `ready` deltaP `-2.442` edge `-0.0951` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-3.6138` n `113` status `ready` deltaP `-14.6524` edge `-0.0203` maxDD `-3.6536`
- `market_context_high->crypto_alt_1h` score `-4.4031` n `128` status `ready` deltaP `-2.0444` edge `-0.0767` maxDD `-19.1277`
- `market_context_high->crypto_alt_4h` score `-4.9921` n `128` status `ready` deltaP `4.0396` edge `-0.0245` maxDD `-46.0617`
- `market_context_high->index_24h` score `-6.178` n `113` status `ready` deltaP `-8.0307` edge `-0.1086` maxDD `-20.2154`
- `market_context_high->crypto_major_4h` score `-8.0892` n `128` status `ready` deltaP `4.1731` edge `-0.1418` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3813` n `128` status `ready` deltaP `5.1829` edge `-0.285` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
