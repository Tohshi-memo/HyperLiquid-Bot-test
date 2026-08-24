# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T08:52:27.237372+00:00`
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

- `news_risk_high->unknown_24h` score `49.6551` n `51` status `ready` deltaP `17.0139` edge `4.0245` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.1979` n `51` status `ready` deltaP `40.237` edge `1.008` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0179` n `51` status `ready` deltaP `24.2587` edge `0.9277` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.716` n `51` status `ready` deltaP `48.9481` edge `0.1652` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7728` n `51` status `ready` deltaP `27.2328` edge `0.2099` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6485` n `51` status `ready` deltaP `17.0834` edge `0.2206` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.209` n `51` status `ready` deltaP `37.778` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.937` n `142` status `ready` deltaP `19.8815` edge `0.0697` maxDD `-0.5994`
- `news_risk_high->metal_24h` score `1.599` n `51` status `ready` deltaP `33.2823` edge `-0.0844` maxDD `-0.0053`
- `market_context_high->unknown_24h` score `1.2503` n `86` status `ready` deltaP `4.2232` edge `0.1267` maxDD `-1.0533`
- `news_risk_high->fx_1h` score `1.205` n `51` status `ready` deltaP `16.5463` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9872` n `51` status `ready` deltaP `18.9415` edge `0.0367` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9727` n `51` status `ready` deltaP `14.1589` edge `0.0264` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2668` n `51` status `ready` deltaP `9.7217` edge `0.0047` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2039` n `51` status `ready` deltaP `8.6885` edge `-0.0101` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.0865` n `142` status `ready` deltaP `9.8098` edge `-0.0123` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0062` n `142` status `ready` deltaP `10.7868` edge `-0.0265` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1224` n `51` status `ready` deltaP `2.043` edge `-0.007` maxDD `-0.1184`
- `news_risk_high->crypto_alt_24h` score `-0.2115` n `51` status `ready` deltaP `22.9167` edge `-0.1704` maxDD `0.0`
- `news_risk_high->metal_4h` score `-0.2191` n `51` status `ready` deltaP `6.7582` edge `-0.0102` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
