# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T08:22:25.382034+00:00`
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

- `news_risk_high->unknown_24h` score `49.8603` n `51` status `ready` deltaP `17.0139` edge `4.0416` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.2507` n `51` status `ready` deltaP `40.237` edge `1.0124` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0009` n `51` status `ready` deltaP `24.1063` edge `0.9273` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7328` n `51` status `ready` deltaP `48.9481` edge `0.1666` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7788` n `51` status `ready` deltaP `27.2328` edge `0.2104` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6617` n `51` status `ready` deltaP `17.2331` edge `0.2207` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2103` n `51` status `ready` deltaP `37.778` edge `0.0291` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8407` n `144` status `ready` deltaP `19.8171` edge `0.0621` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.6424` n `51` status `ready` deltaP `33.6295` edge `-0.0831` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.205` n `51` status `ready` deltaP `16.5463` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9981` n `51` status `ready` deltaP `19.0912` edge `0.0371` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9739` n `51` status `ready` deltaP `14.1589` edge `0.0265` maxDD `-0.1788`
- `market_context_high->unknown_24h` score `0.8451` n `88` status `ready` deltaP `4.5139` edge `0.091` maxDD `-1.0533`
- `news_risk_high->index_1h` score `0.2753` n `51` status `ready` deltaP `9.8714` edge `0.0048` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1895` n `51` status `ready` deltaP `8.5388` edge `-0.0103` maxDD `-0.4666`
- `market_context_high->metal_4h` score `-0.0077` n `144` status `ready` deltaP `8.8415` edge `-0.0137` maxDD `-1.3378`
- `news_risk_high->crypto_alt_24h` score `-0.0733` n `51` status `ready` deltaP `23.2639` edge `-0.1612` maxDD `0.0`
- `market_context_high->unknown_1h` score `-0.1095` n `144` status `ready` deltaP `9.8802` edge `-0.0301` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1224` n `51` status `ready` deltaP `2.043` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2155` n `51` status `ready` deltaP `6.7582` edge `-0.0099` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
