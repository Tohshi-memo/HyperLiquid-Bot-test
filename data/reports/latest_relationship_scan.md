# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T23:22:28.399283+00:00`
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

- `market_context_high->unknown_1h` score `12009.548` n `108` status `ready` deltaP `1.1367` edge `1000.8079` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7451.5859` n `108` status `ready` deltaP `0.0621` edge `620.9935` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `23.7693` n `88` status `ready` deltaP `42.3295` edge `1.7579` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.9551` n `88` status `ready` deltaP `25.6156` edge `1.5012` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8808` n `108` status `ready` deltaP `4.3981` edge `0.4093` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.2489` n `108` status `ready` deltaP `5.6176` edge `0.2742` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.6308` n `88` status `ready` deltaP `19.0656` edge `0.2343` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.412` n `108` status `ready` deltaP `18.1741` edge `0.0476` maxDD `-6.4211`
- `market_context_high->crypto_major_1h` score `-0.2344` n `108` status `ready` deltaP `4.8459` edge `0.0773` maxDD `-6.5061`
- `market_context_high->metal_1h` score `-0.2776` n `108` status `ready` deltaP `4.1916` edge `0.0154` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2919` n `108` status `ready` deltaP `2.8166` edge `0.005` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.7262` n `108` status `ready` deltaP `-1.935` edge `0.042` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.1878` n `108` status `ready` deltaP `6.3429` edge `0.0366` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6325` n `108` status `ready` deltaP `-11.6988` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8916` n `108` status `ready` deltaP `-2.8342` edge `-0.0044` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.4023` n `108` status `ready` deltaP `-15.2552` edge `-0.0047` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4403` n `108` status `ready` deltaP `-10.1187` edge `-0.0277` maxDD `-3.9892`
- `market_context_high->fx_24h` score `-7.274` n `88` status `ready` deltaP `-24.9842` edge `-0.0123` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0592` n `108` status `ready` deltaP `-28.6529` edge `-0.1113` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.5387` n `108` status `ready` deltaP `-7.2041` edge `-0.0647` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
