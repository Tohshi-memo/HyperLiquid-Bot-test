# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T12:37:25.502040+00:00`
- Price records: `672`
- Market context records: `2764`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `5.3215` n `131` status `ready` deltaP `11.8466` edge `0.3973` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `3.4569` n `131` status `ready` deltaP `6.0366` edge `0.7523` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `1.0077` n `143` status `ready` deltaP `6.7063` edge `0.1446` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0184` n `143` status `ready` deltaP `10.2465` edge `0.0182` maxDD `-2.3986`
- `market_context_high->commodity_24h` score `-0.0011` n `131` status `ready` deltaP `8.495` edge `0.2526` maxDD `-12.4171`
- `market_context_high->unknown_1h` score `-0.0237` n `143` status `ready` deltaP `4.0964` edge `0.0438` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1705` n `143` status `ready` deltaP `3.0506` edge `0.0072` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5722` n `143` status `ready` deltaP `-0.9463` edge `0.003` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6301` n `143` status `ready` deltaP `0.0524` edge `-0.0058` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6812` n `143` status `ready` deltaP `5.8457` edge `0.0497` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7747` n `143` status `ready` deltaP `-0.9506` edge `-0.0084` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9674` n `143` status `ready` deltaP `3.6473` edge `0.0386` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1932` n `143` status `ready` deltaP `-3.7864` edge `0.0091` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2441` n `143` status `ready` deltaP `-4.86` edge `0.0066` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.2524` n `143` status `ready` deltaP `14.6864` edge `0.2318` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.3226` n `131` status `ready` deltaP `-0.5738` edge `-0.0192` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6632` n `143` status `ready` deltaP `-0.4679` edge `-0.0181` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.1453` n `143` status `ready` deltaP `-1.0969` edge `-0.0335` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4639` n `143` status `ready` deltaP `-2.7962` edge `-0.0422` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6461` n `143` status `ready` deltaP `5.0753` edge `0.1175` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
