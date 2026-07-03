# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T21:37:29.584398+00:00`
- Price records: `672`
- Market context records: `5597`
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

- `market_context_high->equity_24h` score `3.6367` n `174` status `ready` deltaP `15.0084` edge `0.7109` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.3645` n `211` status `ready` deltaP `12.4733` edge `0.2598` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.1201` n `174` status `ready` deltaP `20.2227` edge `0.0559` maxDD `-1.457`
- `market_context_high->crypto_alt_4h` score `0.6662` n `211` status `ready` deltaP `7.5454` edge `0.1693` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.5793` n `211` status `ready` deltaP `6.8164` edge `0.1667` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.3287` n `223` status `ready` deltaP `5.7457` edge `0.035` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.3291` n `223` status `ready` deltaP `0.6713` edge `0.0009` maxDD `-0.472`
- `market_context_high->crypto_major_1h` score `-0.5515` n `223` status `ready` deltaP `4.4091` edge `0.0492` maxDD `-6.9639`
- `market_context_high->crypto_major_24h` score `-0.562` n `174` status `ready` deltaP `11.3686` edge `0.3314` maxDD `-29.6555`
- `market_context_high->crypto_alt_1h` score `-0.5655` n `223` status `ready` deltaP `1.2648` edge `0.0406` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.5655` n `223` status `ready` deltaP `-0.8217` edge `0.0005` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.602` n `223` status `ready` deltaP `1.4165` edge `0.0064` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.2561` n `223` status `ready` deltaP `-3.0645` edge `-0.0077` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2825` n `211` status `ready` deltaP `2.7561` edge `0.0082` maxDD `-1.0094`
- `market_context_high->index_4h` score `-1.5437` n `211` status `ready` deltaP `2.7728` edge `0.0138` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2845` n `174` status `ready` deltaP `11.1291` edge `0.0316` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9253` n `211` status `ready` deltaP `-11.9827` edge `-0.0568` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1552` n `211` status `ready` deltaP `-5.1923` edge `-0.0441` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0626` n `174` status `ready` deltaP `-8.501` edge `-0.2409` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.6465` n `174` status `ready` deltaP `1.1554` edge `-0.0252` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
