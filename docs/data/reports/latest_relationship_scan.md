# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T08:07:25.906007+00:00`
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

- `news_risk_high->unknown_24h` score `49.9827` n `51` status `ready` deltaP `17.0139` edge `4.0518` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.2759` n `51` status `ready` deltaP `40.237` edge `1.0145` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9815` n `51` status `ready` deltaP `23.9538` edge `0.9267` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7412` n `51` status `ready` deltaP `48.9481` edge `0.1673` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7752` n `51` status `ready` deltaP `27.2328` edge `0.2101` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6593` n `51` status `ready` deltaP `17.2331` edge `0.2205` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2103` n `51` status `ready` deltaP `37.778` edge `0.0291` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.7791` n `145` status `ready` deltaP `19.7077` edge `0.0577` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.6647` n `51` status `ready` deltaP `33.8031` edge `-0.0824` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.217` n `51` status `ready` deltaP `16.696` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9973` n `51` status `ready` deltaP `19.0912` edge `0.037` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9727` n `51` status `ready` deltaP `14.1589` edge `0.0264` maxDD `-0.1788`
- `market_context_high->unknown_24h` score `0.6655` n `89` status `ready` deltaP `4.6543` edge `0.0751` maxDD `-1.0533`
- `news_risk_high->index_1h` score `0.2753` n `51` status `ready` deltaP `9.8714` edge `0.0048` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1895` n `51` status `ready` deltaP `8.5388` edge `-0.0103` maxDD `-0.4666`
- `news_risk_high->crypto_alt_24h` score `0.0078` n `51` status `ready` deltaP `23.4375` edge `-0.1556` maxDD `0.0`
- `market_context_high->metal_4h` score `-0.0395` n `145` status `ready` deltaP `8.5198` edge `-0.0142` maxDD `-1.3378`
- `news_risk_high->metal_1h` score `-0.1232` n `51` status `ready` deltaP `2.043` edge `-0.0071` maxDD `-0.1184`
- `market_context_high->unknown_1h` score `-0.1785` n `145` status `ready` deltaP `9.363` edge `-0.0324` maxDD `-1.5916`
- `news_risk_high->metal_4h` score `-0.2021` n `51` status `ready` deltaP `6.9106` edge `-0.0098` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
