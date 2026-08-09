# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T14:49:26.547214+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10825`

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

- `market_context_high->equity_24h` score `3.7822` n `103` status `ready` deltaP `4.2257` edge `0.593` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.364` n `103` status `ready` deltaP `9.434` edge `0.1917` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2554` n `143` status `ready` deltaP `15.6618` edge `0.0675` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8025` n `143` status `ready` deltaP `10.991` edge `0.0279` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7091` n `103` status `ready` deltaP `21.4013` edge `0.0349` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4092` n `103` status `ready` deltaP `6.4961` edge `0.1623` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3457` n `143` status `ready` deltaP `3.6965` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.391` n `143` status `ready` deltaP `-0.9442` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4931` n `143` status `ready` deltaP `5.6755` edge `-0.0036` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6737` n `143` status `ready` deltaP `-4.5883` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8428` n `143` status `ready` deltaP `-0.1535` edge `-0.0087` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9229` n `143` status `ready` deltaP `-0.3371` edge `0.0082` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0074` n `143` status `ready` deltaP `-1.6608` edge `-0.0172` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9084` n `143` status `ready` deltaP `-10.1336` edge `-0.0273` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4637` n `143` status `ready` deltaP `-0.6566` edge `-0.0672` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2047` n `143` status `ready` deltaP `-11.1365` edge `-0.0606` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.7557` n `143` status `ready` deltaP `-7.8192` edge `-0.0952` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.0739` n `103` status `ready` deltaP `1.8794` edge `-0.1026` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.4279` n `103` status `ready` deltaP `-17.8281` edge `-0.2725` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7753` n `143` status `ready` deltaP `-5.6447` edge `-0.5656` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
