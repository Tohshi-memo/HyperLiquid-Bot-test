# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T16:51:57.651050+00:00`
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

- `news_risk_high->unknown_24h` score `46.4351` n `51` status `ready` deltaP `13.8889` edge `3.777` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.3639` n `51` status `ready` deltaP `40.237` edge `0.9385` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.8557` n `51` status `ready` deltaP `24.1063` edge `0.9152` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.4652` n `51` status `ready` deltaP `48.9481` edge `0.1443` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.9356` n `85` status `ready` deltaP `8.0065` edge `0.3872` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.105` n `51` status `ready` deltaP `27.995` edge `0.2325` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.585` n `51` status `ready` deltaP `16.4846` edge `0.2193` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.326` n `51` status `ready` deltaP `39.1499` edge `0.0296` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6512` n `130` status `ready` deltaP `19.144` edge `0.0508` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2829` n `51` status `ready` deltaP `17.4445` edge `0.0076` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0759` n `51` status `ready` deltaP `15.0735` edge `0.0289` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0153` n `51` status `ready` deltaP `18.7918` edge `0.0413` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.7693` n `51` status `ready` deltaP `27.7267` edge `-0.1165` maxDD `-0.0053`
- `news_risk_high->index_1h` score `0.2403` n `51` status `ready` deltaP `9.1229` edge `0.0053` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2387` n `51` status `ready` deltaP `8.8382` edge `-0.0082` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.116` n `130` status `ready` deltaP `10.8678` edge `-0.0169` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.042` n `130` status `ready` deltaP `11.0548` edge `-0.0253` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1154` n `51` status `ready` deltaP `2.1927` edge `-0.0071` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3101` n `51` status `ready` deltaP `5.996` edge `-0.0127` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4069` n `130` status `ready` deltaP `3.0101` edge `0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
