# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T06:37:18.583686+00:00`
- Price records: `672`
- Market context records: `1604`
- Flow alert records: `6531`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `14.1188` n `184` status `ready` deltaP `30.782` edge `1.0714` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.7719` n `184` status `ready` deltaP `27.1437` edge `1.085` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.8377` n `184` status `ready` deltaP `26.9399` edge `0.8409` maxDD `-8.0553`
- `market_context_high->equity_24h` score `5.3535` n `184` status `ready` deltaP `21.4221` edge `0.536` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.2713` n `184` status `ready` deltaP `22.9015` edge `0.3119` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.2213` n `199` status `ready` deltaP `10.5788` edge `0.1407` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.1683` n `199` status `ready` deltaP `12.9496` edge `0.2672` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0598` n `199` status `ready` deltaP `9.1272` edge `0.2177` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1731` n `184` status `ready` deltaP `7.8125` edge `0.0384` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3768` n `199` status `ready` deltaP `0.3686` edge `0.0516` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5455` n `199` status `ready` deltaP `0.9133` edge `0.0293` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6024` n `199` status `ready` deltaP `-1.5451` edge `-0.0037` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6661` n `199` status `ready` deltaP `0.6244` edge `0.0035` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7407` n `199` status `ready` deltaP `4.9981` edge `0.0053` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7694` n `199` status `ready` deltaP `-0.9463` edge `-0.0002` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-0.8958` n `199` status `ready` deltaP `-0.7432` edge `0.0258` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9375` n `199` status `ready` deltaP `-0.0192` edge `0.0309` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.3823` n `199` status `ready` deltaP `9.4489` edge `0.091` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4203` n `199` status `ready` deltaP `-11.1594` edge `-0.0148` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.177` n `199` status `ready` deltaP `-13.9379` edge `-0.1081` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
