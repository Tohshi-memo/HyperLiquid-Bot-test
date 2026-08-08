# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T01:07:25.058436+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `7.4598` n `81` status `ready` deltaP `5.4205` edge `0.8915` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.8185` n `81` status `ready` deltaP `12.6158` edge `0.2917` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.724` n `81` status `ready` deltaP `33.6034` edge `0.067` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.6851` n `103` status `ready` deltaP `16.8778` edge `0.0952` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.4829` n `81` status `ready` deltaP `9.973` edge `0.2084` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1267` n `103` status `ready` deltaP `13.4832` edge `0.0383` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.2195` n `103` status `ready` deltaP `5.6945` edge `0.0266` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4686` n `103` status `ready` deltaP `2.3545` edge `-0.0052` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4687` n `103` status `ready` deltaP `-2.885` edge `-0.0061` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.5939` n `103` status `ready` deltaP `-0.814` edge `-0.0102` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.5992` n `103` status `ready` deltaP `-3.2614` edge `-0.0055` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8713` n `103` status `ready` deltaP `1.0226` edge `-0.0041` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9687` n `103` status `ready` deltaP `-1.696` edge `-0.012` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.6705` n `103` status `ready` deltaP `4.1129` edge `-0.0329` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.6738` n `103` status `ready` deltaP `-8.1841` edge `-0.022` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.8994` n `81` status `ready` deltaP `11.2076` edge `-0.0688` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1641` n `103` status `ready` deltaP `-5.3398` edge `-0.0451` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5613` n `81` status `ready` deltaP `-21.4313` edge `-0.1694` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7153` n `103` status `ready` deltaP `-7.6827` edge `-0.0932` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.1111` n `103` status `ready` deltaP `-8.9184` edge `-0.194` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
