# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T15:07:29.838296+00:00`
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

- `news_risk_high->unknown_24h` score `43.9489` n `51` status `ready` deltaP `3.6458` edge `3.6381` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.4182` n `53` status `ready` deltaP `23.6079` edge `0.8874` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `8.636` n `51` status `ready` deltaP `33.2925` edge `0.5908` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.289` n `51` status `ready` deltaP `42.5245` edge `0.0891` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.1405` n `53` status `ready` deltaP `16.3117` edge `0.1885` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0392` n `53` status `ready` deltaP `36.0303` edge `0.0265` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.4596` n `133` status `ready` deltaP `21.7495` edge `0.1008` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `2.0143` n `53` status `ready` deltaP `21.8707` edge `0.0991` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1872` n `53` status `ready` deltaP `16.3682` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.5393` n `53` status `ready` deltaP `14.5718` edge `0.0084` maxDD `-0.9128`
- `news_risk_high->commodity_1h` score `0.3709` n `53` status `ready` deltaP `10.2277` edge `-0.006` maxDD `-0.5024`
- `news_risk_high->index_4h` score `0.2426` n `53` status `ready` deltaP `8.0333` edge `0.0064` maxDD `-0.1788`
- `market_context_high->unknown_1h` score `0.123` n `133` status `ready` deltaP `11.8713` edge `-0.024` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.0309` n `53` status `ready` deltaP `4.5984` edge `0.0007` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.339` n `53` status `ready` deltaP `6.3391` edge `-0.0174` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.4067` n `53` status `ready` deltaP `-0.1638` edge `-0.0102` maxDD `-0.1413`
- `news_risk_high->metal_24h` score `-0.4186` n `51` status `ready` deltaP `23.2128` edge `-0.1854` maxDD `-0.0053`
- `market_context_high->fx_1h` score `-0.4195` n `133` status `ready` deltaP `2.9479` edge `-0.0002` maxDD `-0.8587`
- `market_context_high->metal_4h` score `-0.8394` n `133` status `ready` deltaP `5.3319` edge `-0.0418` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1904` n `133` status `ready` deltaP `-5.7719` edge `-0.0069` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
