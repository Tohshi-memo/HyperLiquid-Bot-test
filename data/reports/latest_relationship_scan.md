# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T00:52:29.907629+00:00`
- Price records: `672`
- Market context records: `5612`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.2395` n `174` status `ready` deltaP `15.0084` edge `0.6778` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.4281` n `224` status `ready` deltaP `13.6433` edge `0.2573` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.3052` n `174` status `ready` deltaP `22.1325` edge `0.0586` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.7863` n `224` status `ready` deltaP `8.6564` edge `0.1719` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4389` n `224` status `ready` deltaP `6.2609` edge `0.1587` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.323` n `236` status `ready` deltaP `0.7967` edge `0.0009` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3581` n `236` status `ready` deltaP `5.6024` edge `0.0335` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5287` n `236` status `ready` deltaP `-0.099` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.6153` n `236` status `ready` deltaP `4.3616` edge `0.0442` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6352` n `236` status `ready` deltaP `1.0682` edge `0.0361` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9111` n `236` status `ready` deltaP `0.7967` edge `0.0056` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1394` n `236` status `ready` deltaP `-1.8446` edge `-0.0061` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2961` n `224` status `ready` deltaP `1.2631` edge `0.0071` maxDD `-1.2021`
- `market_context_high->index_4h` score `-1.679` n `224` status `ready` deltaP `1.4264` edge `0.0115` maxDD `-2.874`
- `market_context_high->crypto_major_24h` score `-1.909` n `174` status `ready` deltaP `9.1116` edge `0.2342` maxDD `-29.6555`
- `market_context_high->index_24h` score `-2.3902` n `174` status `ready` deltaP `10.0874` edge `0.025` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8212` n `224` status `ready` deltaP `-10.3549` edge `-0.0543` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1664` n `224` status `ready` deltaP `-5.662` edge `-0.0419` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2728` n `174` status `ready` deltaP `-10.7579` edge `-0.2528` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-11.8699` n `174` status `ready` deltaP `-1.1015` edge `-0.1121` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
