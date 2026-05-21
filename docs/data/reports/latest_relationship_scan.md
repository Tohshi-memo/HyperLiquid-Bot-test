# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T20:07:15.799875+00:00`
- Price records: `672`
- Market context records: `1456`
- Flow alert records: `6103`
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

- `market_context_high->crypto_alt_24h` score `13.1107` n `163` status `ready` deltaP `28.8887` edge `1.1016` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0528` n `163` status `ready` deltaP `27.569` edge `0.9338` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5026` n `163` status `ready` deltaP `15.0094` edge `1.0252` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.3178` n `163` status `ready` deltaP `19.8832` edge `0.3359` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.2666` n `163` status `ready` deltaP `13.1007` edge `0.5009` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.584` n `223` status `ready` deltaP `7.2596` edge `0.1666` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2436` n `163` status `ready` deltaP `11.6404` edge `0.0476` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0529` n `226` status `ready` deltaP `4.1095` edge `0.0147` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0874` n `226` status `ready` deltaP `2.2998` edge `0.0374` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.3114` n `223` status `ready` deltaP `11.3106` edge `0.2306` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4297` n `223` status `ready` deltaP `1.214` edge `0.065` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.484` n `226` status `ready` deltaP `0.5657` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5318` n `226` status `ready` deltaP `2.1528` edge `0.0437` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0174` n `223` status `ready` deltaP `-3.6859` edge `-0.0088` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.0917` n `226` status `ready` deltaP `5.3866` edge `0.0067` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.1245` n `223` status `ready` deltaP `5.472` edge `0.1407` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.2681` n `226` status `ready` deltaP `-1.7765` edge `-0.0017` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.6018` n `226` status `ready` deltaP `-0.7949` edge `0.0075` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7383` n `223` status `ready` deltaP `8.2693` edge `0.0692` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.9373` n `223` status `ready` deltaP `-11.8745` edge `-0.0703` maxDD `-16.0917`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
