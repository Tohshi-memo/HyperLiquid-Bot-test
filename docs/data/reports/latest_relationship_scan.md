# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T13:22:28.538107+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `47.7456` n `51` status `ready` deltaP `16.3194` edge `3.87` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7539` n `51` status `ready` deltaP `40.237` edge `0.971` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0321` n `51` status `ready` deltaP `24.1063` edge `0.9299` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5732` n `51` status `ready` deltaP `48.9481` edge `0.1533` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.8266` n `51` status `ready` deltaP `27.0804` edge `0.2154` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6785` n `51` status `ready` deltaP `16.9337` edge `0.2241` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `2.2934` n `78` status `ready` deltaP `4.7809` edge `0.2095` maxDD `-1.0208`
- `market_context_high->unknown_4h` score `1.7097` n `134` status `ready` deltaP `19.3507` edge `0.0543` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2697` n `51` status `ready` deltaP `17.2948` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.2014` n `51` status `ready` deltaP `30.1573` edge `-0.0967` maxDD `-0.0053`
- `news_risk_high->index_4h` score `1.0335` n `51` status `ready` deltaP `14.7686` edge `0.0274` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.9537` n `51` status `ready` deltaP `18.4924` edge `0.0354` maxDD `-0.9128`
- `news_risk_high->index_1h` score `0.2442` n `51` status `ready` deltaP `9.2726` edge `0.0048` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.2211` n `134` status `ready` deltaP `11.5967` edge `-0.013` maxDD `-1.3378`
- `news_risk_high->commodity_1h` score `0.1332` n `51` status `ready` deltaP `7.94` edge `-0.011` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `-0.0067` n `134` status `ready` deltaP `10.7002` edge `-0.027` maxDD `-1.5916`
- `market_context_high->fx_24h` score `-0.1364` n `78` status `ready` deltaP `13.9022` edge `-0.0038` maxDD `-3.1759`
- `news_risk_high->metal_1h` score `-0.1473` n `51` status `ready` deltaP `1.7436` edge `-0.0082` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1523` n `51` status `ready` deltaP `7.3679` edge `-0.0087` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
