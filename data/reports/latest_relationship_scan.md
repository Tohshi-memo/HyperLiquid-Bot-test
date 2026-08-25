# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T09:52:38.791549+00:00`
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

- `news_risk_high->unknown_24h` score `43.6668` n `51` status `ready` deltaP `2.4306` edge `3.6227` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9884` n `51` status `ready` deltaP `25.6307` edge `0.9161` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.082` n `51` status `ready` deltaP `36.9383` edge `0.687` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.7095` n `51` status `ready` deltaP `45.9967` edge `0.101` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0996` n `52` status `ready` deltaP `15.4997` edge `0.1905` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0753` n `51` status `ready` deltaP `36.406` edge `0.027` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.5859` n `51` status `ready` deltaP `23.4218` edge `0.1364` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9943` n `133` status `ready` deltaP `20.0727` edge `0.0732` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1748` n `52` status `ready` deltaP `16.2137` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.7299` n `52` status `ready` deltaP `16.5131` edge `0.0199` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4852` n `51` status `ready` deltaP `10.1955` edge `0.0122` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2224` n `52` status `ready` deltaP `8.7172` edge `-0.0083` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.0347` n `52` status `ready` deltaP `5.7232` edge `0.0016` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0246` n `133` status `ready` deltaP `11.4222` edge `-0.0292` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.2739` n `51` status `ready` deltaP `6.1484` edge `-0.0107` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.3894` n `52` status `ready` deltaP `-0.1727` edge `-0.0087` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4989` n `133` status `ready` deltaP `1.4509` edge `-0.0004` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.6617` n `133` status `ready` deltaP `6.399` edge `-0.0341` maxDD `-2.4293`
- `news_risk_high->metal_24h` score `-0.6636` n `51` status `ready` deltaP `21.6503` edge `-0.1954` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.1832` n `133` status `ready` deltaP `-5.7719` edge `-0.0063` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
