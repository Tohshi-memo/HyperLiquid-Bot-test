# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T00:52:17.884236+00:00`
- Price records: `672`
- Market context records: `2513`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.0923` n `120` status `ready` deltaP `19.6181` edge `0.3264` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.6296` n `150` status `ready` deltaP `21.3902` edge `0.5111` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8725` n `150` status `ready` deltaP `17.6565` edge `0.386` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1805` n `120` status `ready` deltaP `11.5972` edge `0.5915` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0083` n `150` status `ready` deltaP `11.315` edge `0.1969` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.9636` n `162` status `ready` deltaP `8.1356` edge `0.1448` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6034` n `162` status `ready` deltaP `7.6495` edge `0.1187` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0636` n `120` status `ready` deltaP `1.3194` edge `0.6951` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0089` n `120` status `ready` deltaP `3.4375` edge `0.0759` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1527` n `120` status `ready` deltaP `17.9514` edge `0.0203` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1604` n `150` status `ready` deltaP `6.4918` edge `0.0275` maxDD `-2.3986`
- `market_context_high->metal_1h` score `-0.4116` n `162` status `ready` deltaP `1.3473` edge `0.0142` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.4255` n `162` status `ready` deltaP `1.9831` edge `0.0048` maxDD `-0.278`
- `market_context_high->commodity_1h` score `-0.4274` n `162` status `ready` deltaP `3.4413` edge `0.0101` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4749` n `162` status `ready` deltaP `0.4842` edge `0.0066` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4866` n `162` status `ready` deltaP `2.057` edge `0.0177` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.6537` n `150` status `ready` deltaP `-1.0854` edge `0.0094` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8073` n `120` status `ready` deltaP `4.0625` edge `0.0052` maxDD `-2.5295`
- `market_context_high->equity_1h` score `-0.9001` n `162` status `ready` deltaP `-0.3973` edge `0.0115` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-1.1504` n `150` status `ready` deltaP `1.5265` edge `0.0327` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
