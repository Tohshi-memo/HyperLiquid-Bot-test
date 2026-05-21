# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T02:22:15.557463+00:00`
- Price records: `672`
- Market context records: `1380`
- Flow alert records: `5886`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.5167` n `152` status `ready` deltaP `30.1169` edge `1.0388` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.006` n `152` status `ready` deltaP `13.3224` edge `1.0784` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.45` n `152` status `ready` deltaP `28.7555` edge `0.9641` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.2668` n `152` status `ready` deltaP `21.3451` edge `0.3219` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7913` n `152` status `ready` deltaP `14.4737` edge `0.3688` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6154` n `177` status `ready` deltaP `8.8216` edge `0.1588` maxDD `-3.6396`
- `market_context_high->metal_4h` score `0.068` n `177` status `ready` deltaP `11.8601` edge `0.0697` maxDD `-6.4478`
- `market_context_high->fx_24h` score `-0.0313` n `152` status `ready` deltaP `9.0003` edge `0.0423` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0316` n `189` status `ready` deltaP `4.1513` edge `0.0162` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0543` n `189` status `ready` deltaP `2.8839` edge `0.0321` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3303` n `189` status `ready` deltaP `3.2301` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.3492` n `177` status `ready` deltaP `0.6787` edge `0.0596` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.5676` n `189` status `ready` deltaP `6.3556` edge `0.0092` maxDD `-3.5762`
- `market_context_high->crypto_alt_1h` score `-0.615` n `189` status `ready` deltaP `0.9149` edge `0.0297` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8092` n `189` status `ready` deltaP `-1.1628` edge `0.0018` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.3391` n `177` status `ready` deltaP `7.9596` edge `0.1673` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.4023` n `189` status `ready` deltaP `-1.8209` edge `0.0018` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.438` n `177` status `ready` deltaP `4.1477` edge `0.1234` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.917` n `177` status `ready` deltaP `-7.4385` edge `-0.0131` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.2573` n `177` status `ready` deltaP `3.6181` edge `-0.2146` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
