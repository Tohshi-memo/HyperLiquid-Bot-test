# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T23:52:24.283843+00:00`
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

- `news_risk_high->unknown_24h` score `44.8306` n `51` status `ready` deltaP `9.0278` edge `3.6757` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0051` n `51` status `ready` deltaP `24.5636` edge `0.9246` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.3343` n `51` status `ready` deltaP `40.237` edge `0.8527` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.254` n `51` status `ready` deltaP `48.9481` edge `0.1267` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.8526` n `51` status `ready` deltaP `27.6901` edge `0.2135` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5514` n `51` status `ready` deltaP `16.3349` edge `0.2175` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3298` n `51` status `ready` deltaP `39.3024` edge `0.0289` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8006` n `130` status `ready` deltaP `19.6013` edge `0.0602` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2685` n `51` status `ready` deltaP `17.2948` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0434` n `51` status `ready` deltaP `19.0912` edge `0.0429` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9571` n `51` status `ready` deltaP `14.1589` edge `0.0251` maxDD `-0.1788`
- `market_context_high->unknown_24h` score `0.3494` n `113` status `ready` deltaP `4.603` edge `0.0277` maxDD `-0.6752`
- `news_risk_high->commodity_1h` score `0.2746` n `51` status `ready` deltaP `8.9879` edge `-0.0062` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2006` n `51` status `ready` deltaP `8.3744` edge `0.0052` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.1245` n `130` status `ready` deltaP `11.0202` edge `-0.0172` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0085` n `130` status `ready` deltaP `10.9051` edge `-0.0271` maxDD `-1.5916`
- `news_risk_high->metal_24h` score `-0.1133` n `51` status `ready` deltaP `23.0392` edge `-0.1588` maxDD `-0.0053`
- `news_risk_high->metal_1h` score `-0.173` n `51` status `ready` deltaP `1.1448` edge `-0.0075` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3015` n `51` status `ready` deltaP `6.1484` edge `-0.013` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4162` n `130` status `ready` deltaP `2.8604` edge `0.0008` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
