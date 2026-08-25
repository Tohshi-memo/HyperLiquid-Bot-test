# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T03:37:59.674738+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14776`

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

- `news_risk_high->unknown_24h` score `44.3427` n `51` status `ready` deltaP `6.4236` edge `3.6524` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9633` n `51` status `ready` deltaP `24.716` edge `0.9201` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.7439` n `51` status `ready` deltaP `40.237` edge `0.8035` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.146` n `51` status `ready` deltaP `48.9481` edge `0.1177` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.4986` n `51` status `ready` deltaP `26.7755` edge `0.1901` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.4314` n `51` status `ready` deltaP `16.4846` edge `0.2065` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2896` n `51` status `ready` deltaP `38.8451` edge `0.0286` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8837` n `127` status `ready` deltaP `19.5902` edge `0.0672` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2062` n `51` status `ready` deltaP `16.5463` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8914` n `51` status `ready` deltaP `18.0433` edge `0.0304` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8311` n `51` status `ready` deltaP `13.2442` edge `0.0207` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2998` n `51` status `ready` deltaP `9.2873` edge `-0.0061` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1313` n `51` status `ready` deltaP `7.3265` edge `0.0033` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0512` n `135` status `ready` deltaP `11.1687` edge `-0.0253` maxDD `-1.5916`
- `market_context_high->metal_4h` score `0.0083` n `127` status `ready` deltaP `10.0429` edge `-0.02` maxDD `-1.3378`
- `news_risk_high->metal_1h` score `-0.1855` n `51` status `ready` deltaP `0.8454` edge `-0.0071` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3523` n `51` status `ready` deltaP `5.8435` edge `-0.0152` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4131` n `135` status `ready` deltaP `2.9951` edge `0.0003` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.4716` n `51` status `ready` deltaP `21.6503` edge `-0.1794` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.0087` n `135` status `ready` deltaP `-3.3489` edge `-0.0036` maxDD `-1.3175`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
