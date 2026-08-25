# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T22:22:26.305968+00:00`
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

- `news_risk_high->unknown_24h` score `45.2072` n `51` status `ready` deltaP `8.6806` edge `3.7094` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6064` n `53` status `ready` deltaP `24.3701` edge `0.898` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.2573` n `51` status `ready` deltaP `29.9939` edge `0.4979` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9932` n `51` status `ready` deltaP `40.2676` edge `0.0795` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2629` n `53` status `ready` deltaP `16.4614` edge `0.1977` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.004` n `53` status `ready` deltaP `35.7254` edge `0.0256` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6478` n `133` status `ready` deltaP `22.5117` edge `0.1114` maxDD `-0.5994`
- `news_risk_high->crypto_alt_24h` score `2.1327` n `51` status `ready` deltaP `25.1736` edge `0.0099` maxDD `0.0`
- `news_risk_high->equity_4h` score `1.477` n `53` status `ready` deltaP `18.3646` edge `0.0777` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1764` n `53` status `ready` deltaP `16.2185` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.482` n `51` status `ready` deltaP `26.685` edge `-0.1335` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4487` n `53` status `ready` deltaP `10.9762` edge `-0.0045` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4021` n `53` status `ready` deltaP `12.9251` edge `0.0018` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.2453` n `133` status `ready` deltaP `12.021` edge `-0.0148` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0577` n `53` status `ready` deltaP `6.0516` edge `0.0042` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0846` n `53` status `ready` deltaP `3.7002` edge `-0.0002` maxDD `-0.1583`
- `market_context_high->unknown_24h` score `-0.4` n `125` status `ready` deltaP `8.6806` edge `-0.0912` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.4265` n `133` status `ready` deltaP `2.7982` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5804` n `53` status `ready` deltaP `-1.9602` edge `-0.0127` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7467` n `53` status `ready` deltaP `2.833` edge `-0.028` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
