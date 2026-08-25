# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T04:51:17.692094+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `44.1928` n `51` status `ready` deltaP `5.5556` edge `3.6457` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.9297` n `51` status `ready` deltaP `24.716` edge `0.9173` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.4523` n `51` status `ready` deltaP `40.237` edge `0.7792` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.098` n `51` status `ready` deltaP `48.9481` edge `0.1137` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3078` n `51` status `ready` deltaP `16.0355` edge `0.1992` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.2829` n `51` status `ready` deltaP `26.0133` edge `0.1772` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.264` n `51` status `ready` deltaP `38.5402` edge `0.0285` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.8957` n `127` status `ready` deltaP `19.5902` edge `0.0682` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1823` n `51` status `ready` deltaP `16.2469` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8361` n `51` status `ready` deltaP `17.4445` edge `0.0273` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.7437` n `51` status `ready` deltaP `12.482` edge `0.0185` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.313` n `51` status `ready` deltaP `9.437` edge `-0.006` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0955` n `51` status `ready` deltaP `6.7277` edge `0.0027` maxDD `-0.1583`
- `market_context_high->metal_4h` score `-0.059` n `127` status `ready` deltaP `9.408` edge `-0.0244` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.0796` n `133` status `ready` deltaP `10.3743` edge `-0.0309` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1753` n `51` status `ready` deltaP `0.9951` edge `-0.0068` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.3029` n `51` status `ready` deltaP `5.996` edge `-0.0121` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4646` n `133` status `ready` deltaP `2.0497` edge `0.0` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.51` n `51` status `ready` deltaP `21.6503` edge `-0.1826` maxDD `-0.0053`
- `market_context_high->index_1h` score `-1.0154` n `133` status `ready` deltaP `-3.9755` edge `-0.0043` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
