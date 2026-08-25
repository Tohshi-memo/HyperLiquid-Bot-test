# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T00:37:28.377686+00:00`
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

- `news_risk_high->unknown_24h` score `44.7194` n `51` status `ready` deltaP `8.5069` edge `3.6699` maxDD `0.0`
- `news_risk_high->unknown_4h` score `13.0693` n `51` status `ready` deltaP `25.0209` edge `0.9269` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `12.1903` n `51` status `ready` deltaP `40.237` edge `0.8407` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.23` n `51` status `ready` deltaP `48.9481` edge `0.1247` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.777` n `51` status `ready` deltaP `27.6901` edge `0.2072` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5909` n `51` status `ready` deltaP `16.784` edge `0.2178` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.3298` n `51` status `ready` deltaP `39.3024` edge `0.0289` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8648` n `130` status `ready` deltaP `20.0586` edge `0.0625` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.2554` n `51` status `ready` deltaP `17.1451` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0527` n `51` status `ready` deltaP `19.2409` edge `0.0431` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9463` n `51` status `ready` deltaP `14.1589` edge `0.0242` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.2746` n `51` status `ready` deltaP `8.9879` edge `-0.0062` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.2107` n `51` status `ready` deltaP `8.5241` edge `0.0055` maxDD `-0.1583`
- `market_context_high->metal_4h` score `0.0604` n `130` status `ready` deltaP `10.5629` edge `-0.0195` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.048` n `130` status `ready` deltaP `11.3542` edge `-0.0268` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1824` n `51` status `ready` deltaP `0.9951` edge `-0.0077` maxDD `-0.1184`
- `news_risk_high->metal_24h` score `-0.2257` n `51` status `ready` deltaP `22.5184` edge `-0.1647` maxDD `-0.0053`
- `market_context_high->unknown_24h` score `-0.3024` n `116` status `ready` deltaP `4.1966` edge `-0.0239` maxDD `-0.6752`
- `news_risk_high->metal_4h` score `-0.3657` n `51` status `ready` deltaP `5.6911` edge `-0.0153` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4248` n `130` status `ready` deltaP `2.7107` edge `0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
