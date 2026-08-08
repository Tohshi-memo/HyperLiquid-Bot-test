# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T14:37:25.542190+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `3.9521` n `94` status `ready` deltaP `2.8997` edge `0.616` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6557` n `94` status `ready` deltaP `10.365` edge `0.2098` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4228` n `103` status `ready` deltaP `13.5241` edge `0.0957` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.2902` n `94` status `ready` deltaP `28.8711` edge `0.0596` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.9794` n `103` status `ready` deltaP `11.3874` edge `0.04` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3976` n `94` status `ready` deltaP `6.4975` edge `0.1608` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4376` n `103` status `ready` deltaP `3.7484` edge `0.0214` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4974` n `103` status `ready` deltaP `2.0551` edge `-0.0056` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5131` n `103` status `ready` deltaP `-3.6335` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6113` n `103` status `ready` deltaP `-1.1189` edge `-0.0104` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6397` n `103` status `ready` deltaP `-4.0099` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8479` n `103` status `ready` deltaP `1.4799` edge `-0.0052` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0557` n `103` status `ready` deltaP `-3.2204` edge `-0.013` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.8917` n `103` status `ready` deltaP `2.8934` edge `-0.0432` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.9385` n `103` status `ready` deltaP `-10.8787` edge `-0.0261` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.4697` n `103` status `ready` deltaP `-8.0344` edge `-0.0526` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.737` n `94` status `ready` deltaP `4.2183` edge `-0.1296` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.1923` n `94` status `ready` deltaP `-16.1643` edge `-0.1572` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.1758` n `103` status `ready` deltaP `-11.1887` edge `-0.1082` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.8581` n `103` status `ready` deltaP `-14.1013` edge `-0.2217` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
