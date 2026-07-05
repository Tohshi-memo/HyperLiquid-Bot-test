# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T14:13:00.050258+00:00`
- Price records: `672`
- Market context records: `5779`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8698`

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

- `market_context_high->equity_24h` score `0.6174` n `236` status `ready` deltaP `15.6074` edge `0.483` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1286` n `293` status `ready` deltaP `7.6318` edge `0.1237` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2801` n `305` status `ready` deltaP `1.7748` edge `0.0008` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.5886` n `305` status `ready` deltaP `3.7411` edge `0.0267` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6203` n `305` status `ready` deltaP `2.5086` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7617` n `305` status `ready` deltaP `-1.7959` edge `-0.0052` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.8576` n `305` status `ready` deltaP `3.6208` edge `0.0365` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-0.9378` n `236` status `ready` deltaP `14.551` edge `0.0411` maxDD `-3.6674`
- `market_context_high->index_1h` score `-0.9389` n `305` status `ready` deltaP `0.7196` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.016` n `305` status `ready` deltaP `2.0669` edge `0.035` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2007` n `293` status `ready` deltaP `0.6441` edge `0.0105` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.3023` n `293` status `ready` deltaP `1.8703` edge `0.0051` maxDD `-1.4288`
- `market_context_high->commodity_4h` score `-2.4442` n `293` status `ready` deltaP `-2.9265` edge `-0.0263` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8561` n `236` status `ready` deltaP `2.7454` edge `0.03` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.8679` n `293` status `ready` deltaP `7.7021` edge `0.1469` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8949` n `293` status `ready` deltaP `-6.0794` edge `-0.0481` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.434` n `293` status `ready` deltaP `5.3926` edge `0.0954` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-6.3205` n `236` status `ready` deltaP `3.5075` edge `-0.0669` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0548` n `236` status `ready` deltaP `-7.8655` edge `-0.2451` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.9194` n `236` status `ready` deltaP `-13.8506` edge `-0.08` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
