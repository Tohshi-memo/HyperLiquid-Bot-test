# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T20:52:56.281402+00:00`
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

- `news_risk_high->unknown_24h` score `44.8779` n `51` status `ready` deltaP `7.6389` edge `3.6889` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5836` n `53` status `ready` deltaP `24.3701` edge `0.8961` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.4241` n `51` status `ready` deltaP `29.9939` edge `0.5118` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0148` n `51` status `ready` deltaP `40.2676` edge `0.0813` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2269` n `53` status `ready` deltaP `16.4614` edge `0.1947` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0124` n `53` status `ready` deltaP `35.7254` edge `0.0263` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.625` n `133` status `ready` deltaP `22.5117` edge `0.1095` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.4736` n `53` status `ready` deltaP `18.517` edge `0.0764` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1884` n `53` status `ready` deltaP `16.3682` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->crypto_alt_24h` score `1.0066` n `51` status `ready` deltaP `24.1319` edge `-0.077` maxDD `0.0`
- `news_risk_high->commodity_1h` score `0.4535` n `53` status `ready` deltaP `10.9762` edge `-0.0041` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4255` n `53` status `ready` deltaP `13.2245` edge `0.0028` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.2343` n `51` status `ready` deltaP `25.6434` edge `-0.1472` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `0.2093` n `133` status `ready` deltaP `12.021` edge `-0.0178` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.1161` n `53` status `ready` deltaP `6.6613` edge `0.005` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0916` n `53` status `ready` deltaP `3.5505` edge `-0.0001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4187` n `133` status `ready` deltaP `2.9479` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5541` n `53` status `ready` deltaP `-1.6608` edge `-0.0125` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7175` n `53` status `ready` deltaP `3.1379` edge `-0.0276` maxDD `-0.249`
- `market_context_high->unknown_24h` score `-0.7293` n `125` status `ready` deltaP `7.6389` edge `-0.1117` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
