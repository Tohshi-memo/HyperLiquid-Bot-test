# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T12:37:31.522701+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8732`

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

- `market_context_high->unknown_24h` score `389.6314` n `117` status `ready` deltaP `11.0847` edge `32.4334` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.5534` n `62` status `ready` deltaP `34.1611` edge `0.5887` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6711` n `62` status `ready` deltaP `20.1908` edge `0.4724` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.4258` n `62` status `ready` deltaP `10.7305` edge `0.2239` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2028` n `62` status `ready` deltaP `22.6804` edge `0.1157` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.8086` n `117` status `ready` deltaP `14.0205` edge `0.237` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5501` n `62` status `ready` deltaP `28.8012` edge `0.0467` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `1.9768` n `62` status `ready` deltaP `7.6299` edge `0.1494` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8055` n `62` status `ready` deltaP `23.0781` edge `0.0116` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7198` n `62` status `ready` deltaP `16.8618` edge `0.0907` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.2005` n `117` status `ready` deltaP `16.2967` edge `0.0614` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1798` n `62` status `ready` deltaP `17.2846` edge `0.0776` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.0456` n `117` status `ready` deltaP `21.1799` edge `0.0216` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.7647` n `62` status `ready` deltaP `27.0092` edge `0.0746` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.7555` n `62` status `ready` deltaP `2.5594` edge `0.0978` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7276` n `117` status `ready` deltaP `12.5429` edge `0.0054` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7214` n `117` status `ready` deltaP `11.756` edge `0.0214` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.5463` n `117` status `ready` deltaP `-0.7218` edge `0.2227` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0732` n `62` status `ready` deltaP `4.6552` edge `0.0047` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `-0.139` n `117` status `ready` deltaP `7.2164` edge `0.0292` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
