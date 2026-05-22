# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T12:52:15.795868+00:00`
- Price records: `672`
- Market context records: `1528`
- Flow alert records: `6310`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `13.5348` n `168` status `ready` deltaP `23.5119` edge `1.0712` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6691` n `168` status `ready` deltaP `28.9435` edge `0.9811` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.4768` n `168` status `ready` deltaP `28.2986` edge `0.7976` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8439` n `168` status `ready` deltaP `20.1389` edge `0.2947` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.604` n `168` status `ready` deltaP `13.3929` edge `0.3604` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.9101` n `168` status `ready` deltaP `18.4276` edge `0.0579` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1042` n `193` status `ready` deltaP `3.5148` edge `0.0947` maxDD `-5.0894`
- `market_context_high->fx_1h` score `-0.5751` n `199` status `ready` deltaP `-1.096` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6224` n `199` status `ready` deltaP `-0.5296` edge `0.0261` maxDD `-4.1892`
- `market_context_high->crypto_alt_4h` score `-0.7066` n `193` status `ready` deltaP `10.2245` edge `0.1732` maxDD `-19.5565`
- `market_context_high->commodity_1h` score `-0.7313` n `199` status `ready` deltaP `-0.3475` edge `0.0007` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-0.747` n `199` status `ready` deltaP `5.1478` edge `0.0035` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.7472` n `193` status `ready` deltaP `5.7745` edge `0.1366` maxDD `-13.3376`
- `market_context_high->index_1h` score `-0.756` n `199` status `ready` deltaP `-0.1241` edge `0.001` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.9063` n `199` status `ready` deltaP `-1.7813` edge `0.0172` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.1288` n `199` status `ready` deltaP `-2.0905` edge `0.0049` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.3759` n `193` status `ready` deltaP `9.7987` edge `0.0892` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.5268` n `193` status `ready` deltaP `-5.8108` edge `0.0204` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.8818` n `193` status `ready` deltaP `-7.8186` edge `-0.0118` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-4.3446` n `168` status `ready` deltaP `-0.868` edge `-0.0833` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
