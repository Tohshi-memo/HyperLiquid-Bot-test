# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T23:07:25.498593+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2624`

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

- `market_context_high->unknown_1h` score `12009.8468` n `108` status `ready` deltaP `1.1367` edge `1000.8328` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7451.6495` n `108` status `ready` deltaP `0.0621` edge `620.9988` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `23.8173` n `88` status `ready` deltaP `42.3295` edge `1.7619` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.9668` n `88` status `ready` deltaP `25.6156` edge `1.5027` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8676` n `108` status `ready` deltaP `4.3981` edge `0.4082` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.2417` n `108` status `ready` deltaP `5.6176` edge `0.2736` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.6152` n `88` status `ready` deltaP `19.0656` edge `0.233` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.3854` n `108` status `ready` deltaP `18.0217` edge `0.0464` maxDD `-6.4211`
- `market_context_high->crypto_major_1h` score `-0.2321` n `108` status `ready` deltaP `4.8459` edge `0.0776` maxDD `-6.5061`
- `market_context_high->metal_1h` score `-0.2908` n `108` status `ready` deltaP `4.0419` edge `0.0153` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3005` n `108` status `ready` deltaP `2.6669` edge `0.0049` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.7215` n `108` status `ready` deltaP `-1.935` edge `0.0426` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.2106` n `108` status `ready` deltaP `6.1932` edge `0.0357` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6325` n `108` status `ready` deltaP `-11.6988` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.9086` n `108` status `ready` deltaP `-2.9867` edge `-0.0048` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.4023` n `108` status `ready` deltaP `-15.2552` edge `-0.0047` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4403` n `108` status `ready` deltaP `-10.1187` edge `-0.0277` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.2728` n `88` status `ready` deltaP `-24.9842` edge `-0.0122` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0434` n `108` status `ready` deltaP `-28.5004` edge `-0.111` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.6109` n `108` status `ready` deltaP `-7.3566` edge `-0.0697` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
