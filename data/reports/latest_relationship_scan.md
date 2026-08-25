# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T05:22:27.164896+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `44.1291` n `51` status `ready` deltaP `5.2083` edge `3.6427` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8889` n `51` status `ready` deltaP `24.716` edge `0.9139` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.3076` n `51` status `ready` deltaP `40.0633` edge `0.7683` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.0788` n `51` status `ready` deltaP `48.9481` edge `0.1121` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.2628` n `51` status `ready` deltaP `38.5402` edge `0.0284` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `3.2623` n `51` status `ready` deltaP `15.7361` edge `0.1974` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.1817` n `51` status `ready` deltaP `25.7084` edge `0.1708` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9669` n `129` status `ready` deltaP `19.7001` edge `0.0734` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1943` n `51` status `ready` deltaP `16.3966` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.808` n `51` status `ready` deltaP `17.1451` edge `0.0257` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.7062` n `51` status `ready` deltaP `12.1772` edge `0.0174` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3417` n `51` status `ready` deltaP `9.7364` edge `-0.0056` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0768` n `51` status `ready` deltaP `6.4283` edge `0.0023` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.1251` n `133` status `ready` deltaP `10.0749` edge `-0.0327` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1839` n `51` status `ready` deltaP `0.8454` edge `-0.0069` maxDD `-0.1184`
- `market_context_high->metal_4h` score `-0.1846` n `129` status `ready` deltaP `8.3215` edge `-0.0291` maxDD `-1.6699`
- `news_risk_high->metal_4h` score `-0.2945` n `51` status `ready` deltaP `5.996` edge `-0.0114` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4569` n `133` status `ready` deltaP `2.1994` edge `0.0` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.5316` n `51` status `ready` deltaP `21.6503` edge `-0.1844` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.0442` n `133` status `ready` deltaP `-4.2749` edge `-0.0047` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
