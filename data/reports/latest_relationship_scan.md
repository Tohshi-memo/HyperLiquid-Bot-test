# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T00:52:28.268796+00:00`
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

- `market_context_high->equity_24h` score `7.5385` n `81` status `ready` deltaP `5.5941` edge `0.8969` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.8444` n `81` status `ready` deltaP `12.7894` edge `0.2927` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7248` n `81` status `ready` deltaP `33.6034` edge `0.0671` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.6609` n `103` status `ready` deltaP `16.7253` edge `0.0942` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.5016` n `81` status `ready` deltaP `10.1466` edge `0.2088` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1267` n `103` status `ready` deltaP `13.4832` edge `0.0383` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.2123` n `103` status `ready` deltaP `5.6945` edge `0.0272` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4554` n `103` status `ready` deltaP `2.5042` edge `-0.0051` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.468` n `103` status `ready` deltaP `-2.885` edge `-0.006` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.5907` n `103` status `ready` deltaP `-3.1117` edge `-0.0054` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.5923` n `103` status `ready` deltaP `-0.814` edge `-0.01` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8567` n `103` status `ready` deltaP `1.1751` edge `-0.0039` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9584` n `103` status `ready` deltaP `-1.5436` edge `-0.0117` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.6403` n `103` status `ready` deltaP `4.2653` edge `-0.0314` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.657` n `103` status `ready` deltaP `-8.0344` edge `-0.0216` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-1.8814` n `81` status `ready` deltaP `11.2076` edge `-0.0665` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1461` n `103` status `ready` deltaP `-5.1901` edge `-0.0446` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.5582` n `81` status `ready` deltaP `-21.4313` edge `-0.169` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7129` n `103` status `ready` deltaP `-7.6827` edge `-0.093` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.1087` n `103` status `ready` deltaP `-8.9184` edge `-0.1938` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
