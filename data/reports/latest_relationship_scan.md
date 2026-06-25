# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T13:37:35.440386+00:00`
- Price records: `672`
- Market context records: `4728`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7432`

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

- `market_context_high->unknown_1h` score `78.5946` n `142` status `ready` deltaP `15.1662` edge `6.4902` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.5285` n `142` status `ready` deltaP `14.7673` edge `0.4833` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.2985` n `133` status `ready` deltaP `16.6811` edge `0.256` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.317` n `142` status `ready` deltaP `2.2286` edge `0.0241` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6261` n `142` status `ready` deltaP `4.8352` edge `-0.0015` maxDD `-5.8807`
- `market_context_high->fx_4h` score `-0.8596` n `142` status `ready` deltaP `-0.1095` edge `-0.0018` maxDD `-1.9475`
- `market_context_high->commodity_4h` score `-0.9435` n `142` status `ready` deltaP `9.0153` edge `0.0297` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.0364` n `142` status `ready` deltaP `-3.5043` edge `-0.0091` maxDD `-2.6999`
- `market_context_high->equity_1h` score `-1.0794` n `142` status `ready` deltaP `-2.0073` edge `-0.0263` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.269` n `142` status `ready` deltaP `3.0638` edge `-0.0062` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.3518` n `142` status `ready` deltaP `-5.8173` edge `-0.0059` maxDD `-1.1038`
- `market_context_high->metal_1h` score `-2.8127` n `142` status `ready` deltaP `-5.6676` edge `-0.0768` maxDD `-16.348`
- `market_context_high->crypto_alt_1h` score `-3.0981` n `142` status `ready` deltaP `-0.3606` edge `-0.0703` maxDD `-21.9591`
- `market_context_high->crypto_major_1h` score `-3.6636` n `142` status `ready` deltaP `-0.9762` edge `-0.0879` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.1644` n `133` status `ready` deltaP `17.2762` edge `0.071` maxDD `-29.3231`
- `market_context_high->fx_24h` score `-4.751` n `133` status `ready` deltaP `-13.4999` edge `-0.0188` maxDD `-5.3025`
- `market_context_high->crypto_alt_4h` score `-7.5445` n `142` status `ready` deltaP `-1.387` edge `-0.1287` maxDD `-61.01`
- `market_context_high->index_24h` score `-8.2317` n `133` status `ready` deltaP `-11.1947` edge `-0.0985` maxDD `-28.0273`
- `market_context_high->metal_4h` score `-8.5895` n `142` status `ready` deltaP `2.1406` edge `-0.2554` maxDD `-63.14`
- `market_context_high->crypto_major_4h` score `-10.3648` n `142` status `ready` deltaP `-0.9662` edge `-0.2428` maxDD `-81.0332`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
