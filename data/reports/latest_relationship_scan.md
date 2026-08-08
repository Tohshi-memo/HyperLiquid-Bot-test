# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T23:37:27.117258+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.0612` n `103` status `ready` deltaP `4.5729` edge `0.5306` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4734` n `103` status `ready` deltaP `12.2118` edge `0.1823` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6844` n `113` status `ready` deltaP `16.4944` edge `0.0977` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9642` n `124` status `ready` deltaP `11.6477` edge `0.037` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8697` n `103` status `ready` deltaP `22.2694` edge `0.0497` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4549` n `103` status `ready` deltaP `9.1002` edge `0.1508` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4443` n `124` status `ready` deltaP `2.5691` edge `-0.0046` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5159` n `124` status `ready` deltaP `-3.0616` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6271` n `124` status `ready` deltaP `-3.6024` edge `-0.0068` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6476` n `113` status `ready` deltaP `-1.5014` edge `-0.0125` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.6762` n `113` status `ready` deltaP `3.5209` edge `-0.0045` maxDD `-1.6928`
- `market_context_high->equity_1h` score `-0.688` n `124` status `ready` deltaP `2.2986` edge `0.0102` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.1649` n `113` status `ready` deltaP `-4.8551` edge `-0.0161` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-2.2731` n `113` status `ready` deltaP `0.9754` edge `-0.0622` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-2.3037` n `124` status `ready` deltaP `-13.8449` edge `-0.0355` maxDD `-2.4677`
- `market_context_high->crypto_major_1h` score `-3.1416` n `124` status `ready` deltaP `-11.0585` edge `-0.067` maxDD `-6.3528`
- `market_context_high->crypto_major_24h` score `-3.8011` n `103` status `ready` deltaP `6.2197` edge `-0.1088` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.4086` n `103` status `ready` deltaP `-12.4461` edge `-0.1401` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7948` n `113` status `ready` deltaP `-13.5266` edge `-0.1442` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.3553` n `124` status `ready` deltaP `-5.3796` edge `-0.6157` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
