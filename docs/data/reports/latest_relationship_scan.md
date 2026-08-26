# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T19:37:24.820794+00:00`
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

- `news_risk_high->unknown_24h` score `48.1025` n `50` status `ready` deltaP `11.5717` edge `3.9314` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.4761` n `50` status `ready` deltaP `26.9268` edge `0.8701` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `12.0485` n `50` status `ready` deltaP `35.7237` edge `0.81` maxDD `-2.8629`
- `news_risk_high->equity_24h` score `7.8301` n `50` status `ready` deltaP `33.9136` edge `0.5195` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.092` n `50` status `ready` deltaP `40.677` edge `0.085` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `3.4698` n `50` status `ready` deltaP `40.9329` edge `0.0253` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.3363` n `137` status `ready` deltaP `25.6275` edge `0.148` maxDD `-0.5994`
- `news_risk_high->unknown_1h` score `2.6767` n `50` status `ready` deltaP `15.479` edge `0.1554` maxDD `-0.8426`
- `news_risk_high->metal_24h` score `2.207` n `50` status `ready` deltaP `32.5423` edge `-0.0288` maxDD `-0.0053`
- `news_risk_high->equity_4h` score `1.5454` n `50` status `ready` deltaP `19.4451` edge `0.0762` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.3479` n `50` status `ready` deltaP `18.4072` edge `0.0066` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3078` n `137` status `ready` deltaP `12.8513` edge `0.0682` maxDD `-1.5916`
- `news_risk_high->equity_1h` score `1.2891` n `50` status `ready` deltaP `16.8144` edge `0.0234` maxDD `-0.2455`
- `news_risk_high->commodity_1h` score `0.4996` n `50` status `ready` deltaP `14.0` edge `0.002` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.112` n `50` status `ready` deltaP `6.4756` edge `0.0059` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.103` n `50` status `ready` deltaP `6.7605` edge `0.0021` maxDD `-0.0505`
- `news_risk_high->metal_1h` score `0.0789` n `50` status `ready` deltaP `5.1018` edge `-0.0013` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0333` n `50` status `ready` deltaP `8.2256` edge `-0.0045` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.313` n `133` status `ready` deltaP `5.5567` edge `0.0096` maxDD `-3.1513`
- `market_context_high->fx_1h` score `-0.4029` n `137` status `ready` deltaP `3.3415` edge `-0.0007` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
