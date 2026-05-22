# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T13:37:18.689612+00:00`
- Price records: `672`
- Market context records: `1531`
- Flow alert records: `6319`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8792`

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

- `market_context_high->metal_24h` score `13.343` n `171` status `ready` deltaP `23.5745` edge `1.0548` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.8096` n `171` status `ready` deltaP `28.9748` edge `0.9926` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.395` n `171` status `ready` deltaP `28.3717` edge `0.7903` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9288` n `171` status `ready` deltaP `20.2851` edge `0.3008` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7098` n `171` status `ready` deltaP `13.56` edge `0.3681` maxDD `-14.2815`
- `market_context_high->fx_24h` score `0.8721` n `171` status `ready` deltaP `18.1469` edge `0.0566` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.1763` n `196` status `ready` deltaP `3.951` edge `0.0978` maxDD `-5.0894`
- `market_context_high->fx_1h` score `-0.5829` n `199` status `ready` deltaP `-1.2457` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.6037` n `196` status `ready` deltaP `10.7796` edge `0.1827` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.6201` n `199` status `ready` deltaP `-0.5296` edge `0.0264` maxDD `-4.1892`
- `market_context_high->crypto_major_4h` score `-0.6705` n `196` status `ready` deltaP `6.3931` edge `0.1423` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-0.7398` n `199` status `ready` deltaP `-0.4972` edge `0.0006` maxDD `-4.7041`
- `market_context_high->index_1h` score `-0.7608` n `199` status `ready` deltaP `-0.1241` edge `0.0006` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7688` n `199` status `ready` deltaP `4.8484` edge `0.0027` maxDD `-6.3532`
- `market_context_high->equity_1h` score `-0.9159` n `199` status `ready` deltaP `-1.7813` edge `0.0164` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-1.1164` n `199` status `ready` deltaP `-1.9408` edge `0.0055` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.4067` n `196` status `ready` deltaP `9.5943` edge `0.088` maxDD `-12.5349`
- `market_context_high->index_4h` score `-1.4546` n `196` status `ready` deltaP `-5.1922` edge `0.0223` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.9308` n `196` status `ready` deltaP `-8.3561` edge `-0.0123` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-5.1198` n `171` status `ready` deltaP `-0.2832` edge `-0.1518` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
