# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T03:07:19.109309+00:00`
- Price records: `672`
- Market context records: `1694`
- Flow alert records: `6785`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->unknown_24h` score `7.8233` n `141` status `ready` deltaP `18.7918` edge `1.0587` maxDD `-35.8966`
- `market_context_high->metal_24h` score `6.5539` n `141` status `ready` deltaP `25.6435` edge `0.6178` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.1989` n `192` status `ready` deltaP `22.4339` edge `0.5501` maxDD `-16.3135`
- `market_context_high->crypto_major_4h` score `3.9011` n `192` status `ready` deltaP `22.1671` edge `0.4482` maxDD `-13.3376`
- `market_context_high->index_24h` score `3.8753` n `141` status `ready` deltaP `16.9415` edge `0.3478` maxDD `-5.3574`
- `market_context_high->equity_4h` score `2.9967` n `192` status `ready` deltaP `15.7012` edge `0.2545` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.9047` n `141` status `ready` deltaP `15.8347` edge `0.543` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.6625` n `199` status `ready` deltaP `6.5056` edge `0.1142` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4095` n `141` status `ready` deltaP `24.0509` edge `1.0547` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.3726` n `192` status `ready` deltaP `7.3424` edge `0.091` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0133` n `199` status `ready` deltaP `4.2812` edge `0.0512` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.033` n `199` status `ready` deltaP `4.3353` edge `0.0825` maxDD `-4.4654`
- `market_context_high->index_1h` score `-0.5024` n `199` status `ready` deltaP `0.7207` edge `0.0165` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.5194` n `192` status `ready` deltaP `12.0299` edge `0.1224` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.627` n `199` status `ready` deltaP `5.49` edge `0.0166` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6636` n `199` status `ready` deltaP `-2.903` edge `-0.0025` maxDD `-0.3914`
- `market_context_high->crypto_major_24h` score `-0.718` n `141` status `ready` deltaP `22.3392` edge `0.6176` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.8425` n `141` status `ready` deltaP `4.605` edge `0.004` maxDD `-1.3925`
- `market_context_high->fx_4h` score `-1.7909` n `192` status `ready` deltaP `-6.593` edge `-0.0124` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1173` n `199` status `ready` deltaP `0.4649` edge `-0.0291` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
