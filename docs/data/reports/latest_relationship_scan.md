# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T12:52:34.112844+00:00`
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

- `market_context_high->unknown_24h` score `450.4222` n `117` status `ready` deltaP `11.0847` edge `37.4993` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.528` n `62` status `ready` deltaP `34.0087` edge `0.5876` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6711` n `62` status `ready` deltaP `20.1908` edge `0.4724` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.388` n `62` status `ready` deltaP `10.5587` edge `0.2219` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.1819` n `62` status `ready` deltaP `22.5086` edge `0.1151` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.7832` n `117` status `ready` deltaP `13.8681` edge `0.2359` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5355` n `62` status `ready` deltaP `28.6487` edge `0.0465` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `1.9959` n `62` status `ready` deltaP `7.7796` edge `0.15` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8187` n `62` status `ready` deltaP `23.2278` edge `0.0117` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7198` n `62` status `ready` deltaP `16.8618` edge `0.0907` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.2029` n `117` status `ready` deltaP `16.2967` edge `0.0616` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1711` n `62` status `ready` deltaP `17.1321` edge `0.0775` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.0444` n `117` status `ready` deltaP `21.1799` edge `0.0215` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7819` n `62` status `ready` deltaP `2.7091` edge `0.099` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7725` n `62` status `ready` deltaP `27.0092` edge `0.0756` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7276` n `117` status `ready` deltaP `12.5429` edge `0.0054` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7214` n `117` status `ready` deltaP `11.756` edge `0.0214` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.5463` n `117` status `ready` deltaP `-0.7218` edge `0.2227` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0576` n `62` status `ready` deltaP `4.8049` edge `0.005` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `-0.1198` n `117` status `ready` deltaP `7.3661` edge `0.0298` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
