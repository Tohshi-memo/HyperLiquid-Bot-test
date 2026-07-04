# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T14:07:30.616950+00:00`
- Price records: `672`
- Market context records: `5670`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8670`

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

- `market_context_high->equity_24h` score `2.2028` n `194` status `ready` deltaP `16.1494` edge `0.5838` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.0082` n `244` status `ready` deltaP `11.7428` edge `0.2285` maxDD `-13.4882`
- `market_context_high->crypto_alt_4h` score `0.4846` n `244` status `ready` deltaP `8.789` edge `0.1628` maxDD `-9.1473`
- `market_context_high->equity_4h` score `0.3884` n `244` status `ready` deltaP `6.9497` edge `0.1499` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2824` n `256` status `ready` deltaP `1.5625` edge `0.001` maxDD `-0.4764`
- `market_context_high->fx_24h` score `-0.319` n `194` status `ready` deltaP `16.6953` edge `0.0512` maxDD `-2.7938`
- `market_context_high->equity_1h` score `-0.4742` n `256` status `ready` deltaP `4.5261` edge `0.031` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.554` n `256` status `ready` deltaP `1.9929` edge `0.0367` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.6013` n `256` status `ready` deltaP `0.6971` edge `0.0051` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.7513` n `256` status `ready` deltaP `3.5156` edge `0.0385` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.7753` n `256` status `ready` deltaP `0.4818` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.8793` n `256` status `ready` deltaP `0.9567` edge `-0.0031` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2356` n `244` status `ready` deltaP `2.7639` edge `0.0066` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2692` n `244` status `ready` deltaP `-0.6372` edge `0.0087` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.4749` n `194` status `ready` deltaP `6.9731` edge `0.0349` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9319` n `244` status `ready` deltaP `-12.6474` edge `-0.054` maxDD `-11.6719`
- `market_context_high->commodity_4h` score `-3.6844` n `244` status `ready` deltaP `-1.242` edge `-0.0312` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4728` n `194` status `ready` deltaP `4.419` edge `0.0435` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3534` n `194` status `ready` deltaP `-12.9135` edge `-0.2503` maxDD `-32.7652`
- `market_context_high->commodity_24h` score `-12.4305` n `194` status `ready` deltaP `-12.5072` edge `-0.0916` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
