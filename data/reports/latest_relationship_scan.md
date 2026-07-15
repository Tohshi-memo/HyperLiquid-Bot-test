# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T07:37:36.167147+00:00`
- Price records: `672`
- Market context records: `6795`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8558` n `176` status `ready` deltaP `-1.3731` edge `0.4941` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.1764` n `176` status `ready` deltaP `8.8384` edge `0.1426` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2803` n `185` status `ready` deltaP `6.3489` edge `0.0203` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.4106` n `185` status `ready` deltaP `-0.636` edge `0.0001` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4429` n `185` status `ready` deltaP `3.3468` edge `0.0172` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.6595` n `185` status `ready` deltaP `-1.8587` edge `-0.0006` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.7065` n `185` status `ready` deltaP `-1.8255` edge `-0.0101` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.721` n `185` status `ready` deltaP `-5.4426` edge `-0.0033` maxDD `-1.2285`
- `market_context_high->equity_1h` score `-1.2954` n `185` status `ready` deltaP `2.2326` edge `-0.0184` maxDD `-4.0213`
- `market_context_high->fx_4h` score `-1.3712` n `180` status `ready` deltaP `4.9763` edge `-0.0026` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.4514` n `180` status `ready` deltaP `3.4891` edge `-0.0202` maxDD `-5.7981`
- `market_context_high->commodity_4h` score `-1.4988` n `180` status `ready` deltaP `-3.2656` edge `-0.0214` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5455` n `185` status `ready` deltaP `-5.1432` edge `-0.0044` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6404` n `180` status `ready` deltaP `-5.1999` edge `-0.007` maxDD `-5.4145`
- `market_context_high->crypto_major_4h` score `-3.0192` n `180` status `ready` deltaP `1.3313` edge `-0.0645` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.0563` n `180` status `ready` deltaP `0.4268` edge `-0.0545` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2816` n `180` status `ready` deltaP `-13.3367` edge `0.052` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.4591` n `180` status `ready` deltaP `0.874` edge `-0.1506` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4857` n `176` status `ready` deltaP `-9.6117` edge `-0.0061` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.2719` n `176` status `ready` deltaP `-19.0183` edge `-0.2134` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
