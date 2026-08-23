# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T03:37:37.993978+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `13.2403` n `36` status `ready` deltaP `29.5732` edge `0.9062` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.6797` n `36` status `ready` deltaP `47.2561` edge `0.2416` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.8126` n `48` status `ready` deltaP `24.9251` edge `0.2467` maxDD `-0.2787`
- `news_risk_high->fx_4h` score `3.1969` n `36` status `ready` deltaP `37.5508` edge `0.0295` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `2.1511` n `36` status `ready` deltaP `27.727` edge `0.0028` maxDD `-0.0045`
- `news_risk_high->fx_1h` score `1.546` n `48` status `ready` deltaP `20.8084` edge `0.0071` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.5441` n `135` status `ready` deltaP `6.314` edge `0.1093` maxDD `-0.4843`
- `news_risk_high->equity_1h` score `1.1126` n `48` status `ready` deltaP `21.8563` edge `0.0251` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.9194` n `135` status `ready` deltaP `19.9436` edge `-0.035` maxDD `-0.3736`
- `news_risk_high->index_4h` score `0.5851` n `36` status `ready` deltaP `13.3977` edge `0.0243` maxDD `-0.0884`
- `news_risk_high->commodity_1h` score `0.3064` n `48` status `ready` deltaP `9.9551` edge `-0.01` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.0952` n `135` status `ready` deltaP `8.1063` edge `0.0084` maxDD `-0.3527`
- `news_risk_high->index_1h` score `0.0644` n `48` status `ready` deltaP `6.1003` edge `0.0029` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `0.0442` n `48` status `ready` deltaP `5.2021` edge `-0.0067` maxDD `-0.1184`
- `market_context_high->index_1h` score `-0.0626` n `135` status `ready` deltaP `6.1466` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1747` n `135` status `ready` deltaP `1.364` edge `0.0044` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.3322` n `135` status `ready` deltaP `4.6341` edge `0.0335` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6165` n `135` status `ready` deltaP `-0.6775` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6678` n `135` status `ready` deltaP `1.1755` edge `0.0101` maxDD `-2.618`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
