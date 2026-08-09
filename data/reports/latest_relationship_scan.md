# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T22:37:29.944583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.1462` n `145` status `ready` deltaP `14.5521` edge `0.0658` maxDD `-2.7169`
- `market_context_high->metal_24h` score `0.8639` n `124` status `ready` deltaP `5.1131` edge `0.0955` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.862` n `157` status `ready` deltaP `11.1494` edge `0.0318` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.5245` n `124` status `ready` deltaP `3.2538` edge `0.328` maxDD `-21.1456`
- `market_context_high->fx_24h` score `0.4751` n `124` status `ready` deltaP `18.6716` edge `0.0231` maxDD `-1.9329`
- `market_context_high->index_24h` score `-0.118` n `124` status `ready` deltaP `3.9931` edge `0.1114` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5318` n `157` status `ready` deltaP `1.3692` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.6386` n `157` status `ready` deltaP `-4.3222` edge `-0.0058` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.6402` n `145` status `ready` deltaP `-1.8398` edge `-0.0093` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.6789` n `157` status `ready` deltaP `-0.9412` edge `0.0021` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.7206` n `157` status `ready` deltaP `-4.3575` edge `-0.0089` maxDD `-1.3552`
- `market_context_high->fx_4h` score `-0.7414` n `145` status `ready` deltaP `2.6461` edge `-0.0041` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0225` n `145` status `ready` deltaP `-1.8902` edge `-0.0176` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.1509` n `157` status `ready` deltaP `-8.5901` edge `-0.0261` maxDD `-2.4677`
- `market_context_high->crypto_major_1h` score `-2.0402` n `157` status `ready` deltaP `-10.9939` edge `-0.0549` maxDD `-7.3365`
- `market_context_high->equity_4h` score `-2.6072` n `145` status `ready` deltaP `-2.4201` edge `-0.0674` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-4.0724` n `124` status `ready` deltaP `2.6042` edge `-0.1073` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.0867` n `145` status `ready` deltaP `-8.8814` edge `-0.1157` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.9242` n `124` status `ready` deltaP `-14.3762` edge `-0.1702` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8011` n `157` status `ready` deltaP `-6.3885` edge `-0.5618` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
