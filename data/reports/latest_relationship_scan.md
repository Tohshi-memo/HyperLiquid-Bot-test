# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T19:52:20.384991+00:00`
- Price records: `672`
- Market context records: `1455`
- Flow alert records: `6100`
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

- `market_context_high->crypto_alt_24h` score `13.021` n `162` status `ready` deltaP `28.8773` edge `1.0942` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0018` n `162` status `ready` deltaP `27.5463` edge `0.9297` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5772` n `162` status `ready` deltaP `14.892` edge `1.0322` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.3028` n `162` status `ready` deltaP `19.8302` edge `0.335` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.1718` n `162` status `ready` deltaP `13.0402` edge `0.4934` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5876` n `223` status `ready` deltaP `7.2596` edge `0.1669` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2353` n `162` status `ready` deltaP `11.4776` edge `0.048` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0505` n `226` status `ready` deltaP `4.1095` edge `0.0149` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0814` n `226` status `ready` deltaP `2.2998` edge `0.0379` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.291` n `223` status `ready` deltaP `11.3106` edge `0.2323` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4249` n `223` status `ready` deltaP `1.214` edge `0.0654` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4918` n `226` status `ready` deltaP `0.416` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5222` n `226` status `ready` deltaP `2.1528` edge `0.0445` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0181` n `223` status `ready` deltaP `-3.6859` edge `-0.0089` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.0725` n `226` status `ready` deltaP `5.5363` edge `0.0073` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.1209` n `223` status `ready` deltaP `5.472` edge `0.141` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.2562` n `226` status `ready` deltaP `-1.6268` edge `-0.0017` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5827` n `226` status `ready` deltaP `-0.6452` edge `0.0081` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7323` n `223` status `ready` deltaP `8.2693` edge `0.0697` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.9482` n `223` status `ready` deltaP `-11.8745` edge `-0.0717` maxDD `-16.0917`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
