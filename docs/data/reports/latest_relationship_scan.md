# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T01:37:25.313416+00:00`
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

- `news_risk_high->unknown_24h` score `44.5798` n `51` status `ready` deltaP `7.8125` edge `3.6629` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0838` n `51` status `ready` deltaP `25.1733` edge `0.9271` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.0307` n `51` status `ready` deltaP `40.237` edge `0.8274` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.2012` n `51` status `ready` deltaP `48.9481` edge `0.1223` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.6386` n `51` status `ready` deltaP `27.3852` edge `0.1977` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5177` n `51` status `ready` deltaP `16.784` edge `0.2117` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3042` n `51` status `ready` deltaP `38.9975` edge `0.0288` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8794` n `130` status `ready` deltaP `20.211` edge `0.0627` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2302` n `51` status `ready` deltaP `16.8457` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.9584` n `51` status `ready` deltaP `18.6421` edge `0.035` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9271` n `51` status `ready` deltaP `14.1589` edge `0.0226` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3022` n `51` status `ready` deltaP `9.2873` edge `-0.0059` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.1788` n `51` status `ready` deltaP `8.075` edge `0.0044` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `0.0057` n `131` status `ready` deltaP `11.5303` edge `-0.0315` maxDD `-1.5916`
- `market_context_high->metal_4h` score `-0.022` n `130` status `ready` deltaP `9.9531` edge `-0.0223` maxDD `-1.3378`
- `news_risk_high->metal_1h` score `-0.1995` n `51` status `ready` deltaP `0.8454` edge `-0.0089` maxDD `-0.1184`
- `news_risk_high->metal_24h` score `-0.3785` n `51` status `ready` deltaP `21.8239` edge `-0.1728` maxDD `-0.0053`
- `market_context_high->fx_1h` score `-0.423` n `131` status `ready` deltaP `2.746` edge `0.0007` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.448` n `51` status `ready` deltaP `5.0813` edge `-0.0181` maxDD `-0.249`
- `market_context_high->metal_1h` score `-0.5382` n `131` status `ready` deltaP `-3.2408` edge `-0.0097` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
