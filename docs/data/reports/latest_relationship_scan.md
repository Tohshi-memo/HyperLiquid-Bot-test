# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T12:22:29.917670+00:00`
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

- `news_risk_high->unknown_24h` score `48.1256` n `51` status `ready` deltaP `16.8403` edge `3.8982` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.8247` n `51` status `ready` deltaP `40.237` edge `0.9769` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.1041` n `51` status `ready` deltaP `24.1063` edge `0.9359` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5996` n `51` status `ready` deltaP `48.9481` edge `0.1555` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7276` n `51` status `ready` deltaP `26.623` edge `0.2102` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6977` n `51` status `ready` deltaP `16.9337` edge `0.2257` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2614` n `51` status `ready` deltaP `38.3877` edge `0.0293` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6759` n `137` status `ready` deltaP `19.4978` edge `0.0505` maxDD `-0.5994`
- `market_context_high->unknown_24h` score `1.3388` n `81` status `ready` deltaP `3.2601` edge `0.1405` maxDD `-1.0533`
- `news_risk_high->metal_24h` score `1.2893` n `51` status `ready` deltaP `30.8517` edge `-0.094` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2446` n `51` status `ready` deltaP `16.9954` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->index_4h` score `0.9763` n `51` status `ready` deltaP `14.1589` edge `0.0267` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.9218` n `51` status `ready` deltaP `18.0433` edge `0.0343` maxDD `-0.9128`
- `market_context_high->metal_4h` score `0.3236` n `137` status `ready` deltaP `12.234` edge `-0.0087` maxDD `-1.3378`
- `news_risk_high->index_1h` score `0.2177` n `51` status `ready` deltaP `8.8235` edge `0.0044` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1476` n `51` status `ready` deltaP `8.0897` edge `-0.0108` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0087` n `137` status `ready` deltaP `11.2231` edge `-0.0292` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1364` n `51` status `ready` deltaP `1.8933` edge `-0.0078` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1523` n `51` status `ready` deltaP `7.3679` edge `-0.0087` maxDD `-0.249`
- `market_context_high->fx_24h` score `-0.4039` n `81` status `ready` deltaP `11.6705` edge `-0.0051` maxDD `-3.1759`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
