# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T17:37:15.487724+00:00`
- Price records: `672`
- Market context records: `1549`
- Flow alert records: `6369`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8813`

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

- `market_context_high->metal_24h` score `12.2638` n `182` status `ready` deltaP `22.7754` edge `0.9702` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.9374` n `182` status `ready` deltaP `26.9974` edge `0.9331` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `9.2697` n `182` status `ready` deltaP `26.7399` edge `0.7074` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1232` n `182` status `ready` deltaP `20.7799` edge `0.3137` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5761` n `182` status `ready` deltaP `13.3738` edge `0.3582` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.67` n `182` status `ready` deltaP `16.3557` edge `0.0517` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.2915` n `199` status `ready` deltaP `5.091` edge `0.0998` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `-0.2038` n `199` status `ready` deltaP `12.9496` edge `0.2195` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.2914` n `199` status `ready` deltaP `8.9747` edge `0.1737` maxDD `-13.3376`
- `market_context_high->crypto_alt_1h` score `-0.4556` n `199` status `ready` deltaP `0.5183` edge `0.0405` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.6242` n `199` status `ready` deltaP `-1.9942` edge `-0.0035` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.697` n `199` status `ready` deltaP `-0.0481` edge `0.0031` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.7532` n `199` status `ready` deltaP `4.9981` edge `0.0037` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7956` n `199` status `ready` deltaP `-0.4235` edge `-0.0003` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.8596` n `199` status `ready` deltaP `-1.4819` edge `0.0191` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.9753` n `199` status `ready` deltaP `-0.8929` edge `0.0166` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.3342` n `199` status `ready` deltaP `10.516` edge `0.0879` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.3459` n `199` status `ready` deltaP `-9.9399` edge `-0.0134` maxDD `-1.4313`
- `market_context_high->index_4h` score `-1.4366` n `199` status `ready` deltaP `-4.5923` edge `0.0198` maxDD `-3.7119`
- `market_context_high->commodity_4h` score `-5.1856` n `199` status `ready` deltaP `-14.8525` edge `-0.1031` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
