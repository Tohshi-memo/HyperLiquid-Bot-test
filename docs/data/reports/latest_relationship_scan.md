# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T14:37:33.488543+00:00`
- Price records: `672`
- Market context records: `1431`
- Flow alert records: `6035`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8796`

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

- `market_context_high->crypto_alt_24h` score `11.9849` n `154` status `ready` deltaP `28.7811` edge `1.0085` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.89` n `154` status `ready` deltaP `12.6826` edge `1.073` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.7044` n `154` status `ready` deltaP `27.3539` edge `0.9062` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9357` n `154` status `ready` deltaP `19.3813` edge `0.3074` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.0351` n `154` status `ready` deltaP `12.5271` edge `0.4021` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0071` n `205` status `ready` deltaP `5.8232` edge `0.1281` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1212` n `154` status `ready` deltaP `9.7065` edge `0.0503` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1788` n `217` status `ready` deltaP `3.1507` edge `0.0106` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3008` n `217` status `ready` deltaP `1.9881` edge `0.0217` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.6697` n `205` status `ready` deltaP `-0.1219` edge `0.0539` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.6847` n `217` status `ready` deltaP `0.7499` edge `-0.003` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7067` n `217` status `ready` deltaP `-0.8409` edge `0.0082` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.7834` n `217` status `ready` deltaP `1.2576` edge `0.0287` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9195` n `217` status `ready` deltaP `4.0343` edge `-0.0112` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.1807` n `205` status `ready` deltaP `8.1097` edge `0.1795` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3738` n `205` status `ready` deltaP `4.7561` edge `0.1247` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5909` n `205` status `ready` deltaP `-3.9329` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.7702` n `217` status `ready` deltaP `-1.5191` edge `-0.0017` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-2.6626` n `205` status `ready` deltaP `-10.2439` edge `-0.0184` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.797` n `205` status `ready` deltaP `4.7256` edge `0.0046` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
