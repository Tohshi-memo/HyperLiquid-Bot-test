# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T04:22:34.078782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14808`

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

- `news_risk_high->unknown_24h` score `46.3386` n `51` status `ready` deltaP `11.6319` edge `3.784` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.4442` n `53` status `ready` deltaP `23.303` edge `0.8916` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `6.9465` n `51` status `ready` deltaP `29.9939` edge `0.472` maxDD `-4.7801`
- `news_risk_high->crypto_alt_24h` score `6.2808` n `51` status `ready` deltaP `29.3403` edge `0.3278` maxDD `0.0`
- `news_risk_high->index_24h` score `4.0028` n `51` status `ready` deltaP `40.2676` edge `0.0803` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3254` n `53` status `ready` deltaP `16.0123` edge `0.2059` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.8071` n `53` status `ready` deltaP `33.7437` edge `0.0224` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.4857` n `133` status `ready` deltaP `21.4446` edge `0.105` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.6329` n `53` status `ready` deltaP `19.2792` edge `0.0846` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.2297` n `51` status `ready` deltaP `29.1156` edge `-0.0874` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.0578` n `53` status `ready` deltaP `14.8712` edge `0.006` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.5074` n `53` status `ready` deltaP `11.575` edge `-0.0036` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3609` n `53` status `ready` deltaP `12.3263` edge `0.0005` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.3541` n `134` status `ready` deltaP `11.7459` edge `-0.0039` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0149` n `53` status `ready` deltaP `5.4418` edge `0.0047` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.122` n `53` status `ready` deltaP `3.1014` edge `-0.001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4843` n `134` status `ready` deltaP `1.7763` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5744` n `53` status `ready` deltaP `-1.8105` edge `-0.0132` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.8245` n `53` status `ready` deltaP `2.0708` edge `-0.0294` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0466` n `53` status `ready` deltaP `-2.1255` edge `0.0033` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
