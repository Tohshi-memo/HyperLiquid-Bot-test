# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T07:37:30.275521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5984`

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

- `market_context_high->unknown_4h` score `42.3795` n `85` status `ready` deltaP `-12.9484` edge `3.676` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.5756` n `71` status `ready` deltaP `38.0183` edge `0.5874` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.472` n `71` status `ready` deltaP `12.3558` edge `1.1904` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.6193` n `85` status `ready` deltaP `22.7259` edge `0.0118` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.2521` n `71` status `ready` deltaP `11.8936` edge `0.1027` maxDD `-1.6399`
- `market_context_high->fx_1h` score `0.2088` n `97` status `ready` deltaP `7.3477` edge `0.002` maxDD `-0.271`
- `market_context_high->commodity_1h` score `-0.1201` n `97` status `ready` deltaP `2.5094` edge `0.0067` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `-0.1565` n `85` status `ready` deltaP `4.1212` edge `0.0058` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `-0.2367` n `97` status `ready` deltaP `3.1422` edge `0.0376` maxDD `-3.7778`
- `market_context_high->crypto_major_4h` score `-0.3591` n `85` status `ready` deltaP `3.4845` edge `0.1331` maxDD `-10.5224`
- `market_context_high->metal_1h` score `-0.5666` n `97` status `ready` deltaP `-2.1622` edge `0.0013` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.81` n `71` status `ready` deltaP `-0.472` edge `0.0478` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.8435` n `97` status `ready` deltaP `-2.6282` edge `0.0253` maxDD `-4.9401`
- `market_context_high->fx_24h` score `-1.0231` n `71` status `ready` deltaP `2.4599` edge `0.0037` maxDD `-1.7677`
- `market_context_high->metal_4h` score `-1.4016` n `85` status `ready` deltaP `-13.7483` edge `0.0134` maxDD `-1.1153`
- `market_context_high->index_4h` score `-1.4243` n `85` status `ready` deltaP `-13.377` edge `-0.0002` maxDD `-1.1242`
- `market_context_high->crypto_alt_24h` score `-1.5535` n `71` status `ready` deltaP `-1.1297` edge `0.4196` maxDD `-35.5652`
- `market_context_high->index_1h` score `-1.7117` n `97` status `ready` deltaP `-8.0314` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.765` n `97` status `ready` deltaP `-7.9835` edge `-0.0069` maxDD `-2.2898`
- `market_context_high->equity_4h` score `-2.9915` n `85` status `ready` deltaP `-12.2633` edge `-0.0083` maxDD `-6.4057`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
