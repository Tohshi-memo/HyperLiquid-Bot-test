# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T19:52:27.065095+00:00`
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

- `news_risk_high->unknown_24h` score `48.1673` n `50` status `ready` deltaP `11.5717` edge `3.9368` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.4905` n `50` status `ready` deltaP `26.9268` edge `0.8713` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `12.2051` n `50` status `ready` deltaP `35.8964` edge `0.8219` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8277` n `50` status `ready` deltaP `33.9136` edge `0.5193` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0757` n `50` status `ready` deltaP `40.5043` edge `0.0848` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.4698` n `50` status `ready` deltaP `40.9329` edge `0.0253` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3507` n `137` status `ready` deltaP `25.6275` edge `0.1492` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.6959` n `50` status `ready` deltaP `15.479` edge `0.157` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.234` n `50` status `ready` deltaP `32.715` edge `-0.0277` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.561` n `50` status `ready` deltaP `19.4451` edge `0.0775` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.3479` n `50` status `ready` deltaP `18.4072` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.327` n `137` status `ready` deltaP `12.8513` edge `0.0698` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `1.3107` n `50` status `ready` deltaP `16.9641` edge `0.0242` maxDD `-0.2455`
- `news_risk_high->commodity_1h` score `0.4911` n `50` status `ready` deltaP `13.8503` edge `0.0019` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1132` n `50` status `ready` deltaP `6.4756` edge `0.006` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.0952` n `50` status `ready` deltaP `6.6108` edge `0.0021` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0874` n `50` status `ready` deltaP `5.2515` edge `-0.0012` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0175` n `50` status `ready` deltaP `8.378` edge `-0.0042` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.2482` n `133` status `ready` deltaP `5.5567` edge `0.015` maxDD `-3.1513`
- `market_context_high->fx_1h` score `-0.4029` n `137` status `ready` deltaP `3.3415` edge `-0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
