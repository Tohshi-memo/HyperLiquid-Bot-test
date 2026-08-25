# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T01:52:32.441831+00:00`
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

- `news_risk_high->unknown_24h` score `44.5443` n `51` status `ready` deltaP `7.6389` edge `3.6611` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0525` n `51` status `ready` deltaP `25.0209` edge `0.9255` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.0007` n `51` status `ready` deltaP `40.237` edge `0.8249` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.194` n `51` status `ready` deltaP `48.9481` edge `0.1217` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.6072` n `51` status `ready` deltaP `27.2328` edge `0.1961` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5213` n `51` status `ready` deltaP `16.784` edge `0.212` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3042` n `51` status `ready` deltaP `38.9975` edge `0.0288` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.848` n `130` status `ready` deltaP `20.0586` edge `0.0611` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2182` n `51` status `ready` deltaP `16.696` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9389` n `51` status `ready` deltaP `18.4924` edge `0.0335` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9113` n `51` status `ready` deltaP `14.0064` edge `0.0223` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2878` n `51` status `ready` deltaP `9.1376` edge `-0.0061` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1694` n `51` status `ready` deltaP `7.9253` edge `0.0042` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.004` n `132` status `ready` deltaP `11.7038` edge `-0.0328` maxDD `-1.5916`
- `market_context_high->metal_4h` score `-0.0366` n `130` status `ready` deltaP `9.8007` edge `-0.0225` maxDD `-1.3378`
- `news_risk_high->metal_1h` score `-0.1987` n `51` status `ready` deltaP `0.8454` edge `-0.0088` maxDD `-0.1184`
- `news_risk_high->metal_24h` score `-0.4104` n `51` status `ready` deltaP `21.6503` edge `-0.1743` maxDD `-0.0053`
- `market_context_high->fx_1h` score `-0.4136` n `132` status `ready` deltaP `2.926` edge `0.0007` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.4626` n `51` status `ready` deltaP `4.9289` edge `-0.0183` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.5629` n `132` status `ready` deltaP `-3.611` edge `-0.0104` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
