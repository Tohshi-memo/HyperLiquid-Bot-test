# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T04:07:25.353660+00:00`
- Price records: `672`
- Market context records: `5625`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8743`

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

- `market_context_high->equity_24h` score `3.0091` n `174` status `ready` deltaP `15.0084` edge `0.6586` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3424` n `174` status `ready` deltaP `22.1325` edge `0.0617` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `0.895` n `237` status `ready` deltaP `11.6143` edge `0.2264` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4685` n `237` status `ready` deltaP `7.3814` edge `0.1537` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.1366` n `237` status `ready` deltaP `5.7644` edge `0.1351` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2883` n `237` status `ready` deltaP `1.4496` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.381` n `237` status `ready` deltaP `5.316` edge `0.0335` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5239` n `237` status `ready` deltaP `-0.007` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5858` n `237` status `ready` deltaP `4.5801` edge `0.0452` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6549` n `237` status `ready` deltaP `0.9873` edge `0.035` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.943` n `237` status `ready` deltaP `0.4289` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0836` n `237` status `ready` deltaP `-1.1774` edge `-0.0059` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3415` n `237` status `ready` deltaP `0.7609` edge `0.0063` maxDD `-1.335`
- `market_context_high->index_4h` score `-1.932` n `237` status `ready` deltaP `-0.4695` edge `0.0093` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3761` n `174` status `ready` deltaP `10.0874` edge `0.0268` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8928` n `237` status `ready` deltaP `-11.7777` edge `-0.054` maxDD `-11.7351`
- `market_context_high->crypto_major_24h` score `-3.1179` n `174` status `ready` deltaP `6.8547` edge `0.1485` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-4.0538` n `237` status `ready` deltaP `-4.779` edge `-0.0384` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2678` n `174` status `ready` deltaP `-10.9315` edge `-0.251` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.8172` n `174` status `ready` deltaP `-3.3585` edge `-0.176` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
