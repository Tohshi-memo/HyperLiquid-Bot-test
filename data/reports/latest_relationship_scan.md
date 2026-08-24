# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T15:19:48.764602+00:00`
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

- `news_risk_high->unknown_24h` score `46.996` n `51` status `ready` deltaP `14.9306` edge `3.8168` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.6531` n `51` status `ready` deltaP `40.237` edge `0.9626` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9037` n `51` status `ready` deltaP `24.1063` edge `0.9192` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.5288` n `51` status `ready` deltaP `48.9481` edge `0.1496` maxDD `-0.2147`
- `market_context_high->unknown_24h` score `4.8432` n `80` status `ready` deltaP `8.6806` edge `0.375` maxDD `-0.6752`
- `news_risk_high->equity_4h` score `4.1062` n `51` status `ready` deltaP `27.995` edge `0.2326` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6006` n `51` status `ready` deltaP `16.4846` edge `0.2206` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2882` n `51` status `ready` deltaP `38.6926` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.6992` n `130` status `ready` deltaP `19.144` edge `0.0548` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2314` n `51` status `ready` deltaP `16.8457` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->index_4h` score `1.0783` n `51` status `ready` deltaP `15.0735` edge `0.0291` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `1.0621` n `51` status `ready` deltaP `19.0912` edge `0.0453` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.9691` n `51` status `ready` deltaP `28.7684` edge `-0.1068` maxDD `-0.0053`
- `news_risk_high->index_1h` score `0.2862` n `51` status `ready` deltaP `9.8714` edge `0.0062` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1937` n `130` status `ready` deltaP `11.63` edge `-0.0155` maxDD `-1.3378`
- `news_risk_high->commodity_1h` score `0.1728` n `51` status `ready` deltaP `8.2394` edge `-0.0097` maxDD `-0.4666`
- `market_context_high->unknown_1h` score `0.0576` n `130` status `ready` deltaP `11.0548` edge `-0.024` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1341` n `51` status `ready` deltaP `1.8933` edge `-0.0075` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2323` n `51` status `ready` deltaP `6.7582` edge `-0.0113` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4404` n `130` status `ready` deltaP `2.4113` edge `0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
