# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T21:52:15.501082+00:00`
- Price records: `672`
- Market context records: `1464`
- Flow alert records: `6124`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `12.7777` n `165` status `ready` deltaP `28.911` edge `1.0737` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.9424` n `165` status `ready` deltaP `27.6136` edge `0.9243` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.4373` n `165` status `ready` deltaP `15.4988` edge `1.0165` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.1438` n `165` status `ready` deltaP `19.9874` edge `0.3207` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9762` n `165` status `ready` deltaP `13.2197` edge `0.4759` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5312` n `221` status `ready` deltaP `7.2295` edge `0.1624` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2751` n `165` status `ready` deltaP `11.9602` edge `0.0481` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0962` n `221` status `ready` deltaP `3.6281` edge `0.0143` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1292` n `221` status `ready` deltaP `1.9881` edge `0.036` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.2208` n `221` status `ready` deltaP `11.3184` edge `0.2381` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4201` n `221` status `ready` deltaP `1.243` edge `0.0656` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4776` n `221` status `ready` deltaP `0.6889` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5503` n `221` status `ready` deltaP `1.7707` edge `0.0447` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0459` n `221` status `ready` deltaP `-4.1607` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.1358` n `221` status `ready` deltaP `5.1361` edge `0.142` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.1531` n `221` status `ready` deltaP `5.2341` edge `0.0026` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.2543` n `221` status `ready` deltaP `-1.5735` edge `-0.0019` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5793` n `221` status `ready` deltaP `-0.6482` edge `0.0084` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7649` n `221` status `ready` deltaP `8.0565` edge `0.0684` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.0516` n `221` status `ready` deltaP `-11.6861` edge `-0.0699` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
