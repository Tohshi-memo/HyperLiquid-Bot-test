# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T01:37:27.181820+00:00`
- Price records: `672`
- Market context records: `5615`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8757`

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

- `market_context_high->equity_24h` score `3.1747` n `174` status `ready` deltaP `15.0084` edge `0.6724` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3124` n `174` status `ready` deltaP `22.1325` edge `0.0592` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `1.3089` n `227` status `ready` deltaP `13.2333` edge `0.2501` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `0.6122` n `227` status `ready` deltaP `7.9651` edge `0.162` maxDD `-9.46`
- `market_context_high->equity_4h` score `0.4332` n `227` status `ready` deltaP `6.4743` edge `0.1568` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.3038` n `237` status `ready` deltaP `1.1502` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3391` n `237` status `ready` deltaP `5.7651` edge `0.034` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5161` n `237` status `ready` deltaP `0.1427` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.581` n `237` status `ready` deltaP `4.5801` edge `0.0456` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6249` n `237` status `ready` deltaP `1.137` edge `0.0365` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9046` n `237` status `ready` deltaP `0.878` edge `0.0056` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.1387` n `237` status `ready` deltaP `-1.7762` edge `-0.0065` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2885` n `227` status `ready` deltaP `1.4244` edge `0.007` maxDD `-1.2021`
- `market_context_high->index_4h` score `-1.7201` n `227` status `ready` deltaP `1.0174` edge `0.0108` maxDD `-2.874`
- `market_context_high->crypto_major_24h` score `-2.1655` n `174` status `ready` deltaP `8.5908` edge `0.2163` maxDD `-29.6555`
- `market_context_high->index_24h` score `-2.3894` n `174` status `ready` deltaP `10.0874` edge `0.0251` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.8379` n `227` status `ready` deltaP `-10.6922` edge `-0.0542` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1259` n `227` status `ready` deltaP `-5.3052` edge `-0.0409` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2802` n `174` status `ready` deltaP `-10.9315` edge `-0.2526` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.0795` n `174` status `ready` deltaP `-1.6224` edge `-0.1261` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
