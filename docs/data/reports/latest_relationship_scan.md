# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T23:36:27.897910+00:00`
- Price records: `672`
- Market context records: `3017`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `21.5953` n `98` status `ready` deltaP `9.2829` edge `2.1294` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.9728` n `98` status `ready` deltaP `43.3355` edge `0.8032` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.7548` n `98` status `ready` deltaP `21.5207` edge `0.9659` maxDD `-1.7175`
- `market_context_high->equity_24h` score `11.6756` n `98` status `ready` deltaP `20.2559` edge `1.0383` maxDD `-12.6963`
- `market_context_high->index_24h` score `7.28` n `98` status `ready` deltaP `19.8661` edge `0.5723` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4505` n `108` status `ready` deltaP `18.2588` edge `0.1472` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6509` n `108` status `ready` deltaP `13.6179` edge `0.1734` maxDD `-12.1259`
- `market_context_high->crypto_alt_4h` score `0.1866` n `108` status `ready` deltaP `23.3289` edge `0.4232` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.1618` n `108` status `ready` deltaP `16.7852` edge `0.0953` maxDD `-10.5833`
- `market_context_high->commodity_1h` score `-0.0478` n `120` status `ready` deltaP `1.9012` edge `0.0256` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.3606` n `120` status `ready` deltaP `3.523` edge `0.0381` maxDD `-5.6254`
- `market_context_high->index_1h` score `-0.4017` n `120` status `ready` deltaP `4.2315` edge `0.0217` maxDD `-4.1126`
- `market_context_high->fx_1h` score `-0.4505` n `120` status `ready` deltaP `-3.2485` edge `0.0005` maxDD `-0.2615`
- `market_context_high->crypto_alt_1h` score `-0.6917` n `120` status `ready` deltaP `6.1327` edge `0.0834` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.8292` n `120` status `ready` deltaP `3.9721` edge `-0.0225` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1291` n `108` status `ready` deltaP `-9.7166` edge `-0.001` maxDD `-0.6521`
- `market_context_high->crypto_major_1h` score `-1.1612` n `120` status `ready` deltaP `3.8273` edge `0.0519` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1919` n `120` status `ready` deltaP `-2.4751` edge `-0.0045` maxDD `-6.8783`
- `market_context_high->unknown_4h` score `-1.2935` n `108` status `ready` deltaP `-2.1229` edge `0.0117` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.7246` n `98` status `ready` deltaP `-4.7441` edge `-0.0249` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
