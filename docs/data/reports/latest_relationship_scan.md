# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T20:07:46.350046+00:00`
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

- `news_risk_high->unknown_24h` score `48.2249` n `50` status `ready` deltaP `11.5717` edge `3.9416` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5001` n `50` status `ready` deltaP `26.9268` edge `0.8721` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `12.3557` n `50` status `ready` deltaP `36.0691` edge `0.8333` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8055` n `50` status `ready` deltaP `33.7409` edge `0.5186` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0607` n `50` status `ready` deltaP `40.3316` edge `0.0847` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.4698` n `50` status `ready` deltaP `40.9329` edge `0.0253` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3603` n `137` status `ready` deltaP `25.6275` edge `0.15` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.7079` n `50` status `ready` deltaP `15.479` edge `0.158` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.2598` n `50` status `ready` deltaP `32.8877` edge `-0.0267` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.567` n `50` status `ready` deltaP `19.4451` edge `0.078` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.3479` n `50` status `ready` deltaP `18.4072` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.339` n `137` status `ready` deltaP `12.8513` edge `0.0708` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `1.3143` n `50` status `ready` deltaP `16.9641` edge `0.0245` maxDD `-0.2455`
- `news_risk_high->commodity_1h` score `0.4911` n `50` status `ready` deltaP `13.8503` edge `0.0019` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.1144` n `50` status `ready` deltaP `6.4756` edge `0.0061` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.0952` n `50` status `ready` deltaP `6.6108` edge `0.0021` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0874` n `50` status `ready` deltaP `5.2515` edge `-0.0012` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0029` n `50` status `ready` deltaP `8.5305` edge `-0.004` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.1906` n `133` status `ready` deltaP `5.5567` edge `0.0198` maxDD `-3.1513`
- `market_context_high->fx_1h` score `-0.4029` n `137` status `ready` deltaP `3.3415` edge `-0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
