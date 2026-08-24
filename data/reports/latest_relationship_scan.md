# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T13:07:25.220199+00:00`
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

- `news_risk_high->unknown_24h` score `47.8458` n `51` status `ready` deltaP `16.4931` edge `3.8772` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.7731` n `51` status `ready` deltaP `40.237` edge `0.9726` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0501` n `51` status `ready` deltaP `24.1063` edge `0.9314` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5804` n `51` status `ready` deltaP `48.9481` edge `0.1539` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7988` n `51` status `ready` deltaP `26.9279` edge `0.2141` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6869` n `51` status `ready` deltaP `16.9337` edge `0.2248` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2894` n `51` status `ready` deltaP `38.6926` edge `0.0296` maxDD `-0.0746`
- `market_context_high->unknown_24h` score `2.3936` n `78` status `ready` deltaP `4.9546` edge `0.2167` maxDD `-1.0208`
- `market_context_high->unknown_4h` score `1.7277` n `134` status `ready` deltaP `19.3507` edge `0.0558` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2697` n `51` status `ready` deltaP `17.2948` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `1.2261` n `51` status `ready` deltaP `30.3309` edge `-0.0958` maxDD `-0.0053`
- `news_risk_high->index_4h` score `1.0201` n `51` status `ready` deltaP `14.6162` edge `0.0273` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.9436` n `51` status `ready` deltaP `18.3427` edge `0.0351` maxDD `-0.9128`
- `news_risk_high->index_1h` score `0.2356` n `51` status `ready` deltaP `9.1229` edge `0.0047` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.2223` n `134` status `ready` deltaP `11.5967` edge `-0.0129` maxDD `-1.3378`
- `news_risk_high->commodity_1h` score `0.1332` n `51` status `ready` deltaP `7.94` edge `-0.011` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0017` n `134` status `ready` deltaP `10.7002` edge `-0.0263` maxDD `-1.5916`
- `market_context_high->fx_24h` score `-0.1372` n `78` status `ready` deltaP `13.9022` edge `-0.0039` maxDD `-3.1759`
- `news_risk_high->metal_1h` score `-0.1466` n `51` status `ready` deltaP `1.7436` edge `-0.0081` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1511` n `51` status `ready` deltaP `7.3679` edge `-0.0086` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
