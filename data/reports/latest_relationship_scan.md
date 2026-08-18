# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T09:07:28.418134+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.17` n `82` status `ready` deltaP `6.5879` edge `0.2577` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.4447` n `82` status `ready` deltaP `15.9213` edge `0.2624` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.9811` n `97` status `ready` deltaP `8.7259` edge `0.054` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7646` n `97` status `ready` deltaP `9.7216` edge `0.101` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.7022` n `97` status `ready` deltaP `14.0699` edge `0.0223` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6135` n `97` status `ready` deltaP `12.3526` edge `0.0075` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5267` n `97` status `ready` deltaP `9.4605` edge `0.0035` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.4446` n `97` status `ready` deltaP `11.7033` edge `0.1107` maxDD `-5.5373`
- `market_context_high->metal_1h` score `-0.0234` n `97` status `ready` deltaP `4.207` edge `0.0087` maxDD `-0.4291`
- `market_context_high->unknown_24h` score `-0.0412` n `82` status `ready` deltaP `13.7823` edge `-0.0765` maxDD `-0.1719`
- `market_context_high->fx_4h` score `-0.2565` n `97` status `ready` deltaP `2.6575` edge `-0.0001` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.2902` n `97` status `ready` deltaP `3.1591` edge `0.0219` maxDD `-2.413`
- `market_context_high->equity_4h` score `-0.318` n `97` status `ready` deltaP `0.968` edge `0.0575` maxDD `-2.5696`
- `market_context_high->commodity_4h` score `-0.3977` n `97` status `ready` deltaP `3.6522` edge `0.0097` maxDD `-2.4692`
- `market_context_high->crypto_major_1h` score `-0.4476` n `97` status `ready` deltaP `1.6791` edge `0.0159` maxDD `-2.7581`
- `market_context_high->fx_1h` score `-0.4775` n `97` status `ready` deltaP `-3.8907` edge `0.0009` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.6721` n `97` status `ready` deltaP `0.1179` edge `0.0087` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9019` n `97` status `ready` deltaP `-7.1332` edge `-0.0068` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.6974` n `82` status `ready` deltaP `-5.7552` edge `0.0238` maxDD `-6.2435`
- `market_context_high->index_24h` score `-4.0226` n `82` status `ready` deltaP `-13.5415` edge `-0.1699` maxDD `-10.4437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
