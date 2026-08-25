# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T21:21:39.415698+00:00`
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

- `news_risk_high->unknown_24h` score `44.9885` n `51` status `ready` deltaP `7.9861` edge `3.6958` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5932` n `53` status `ready` deltaP `24.3701` edge `0.8969` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.3677` n `51` status `ready` deltaP `29.9939` edge `0.5071` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0064` n `51` status `ready` deltaP `40.2676` edge `0.0806` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2809` n `53` status `ready` deltaP `16.7608` edge `0.1972` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.01` n `53` status `ready` deltaP `35.7254` edge `0.0261` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6346` n `133` status `ready` deltaP `22.5117` edge `0.1103` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.465` n `53` status `ready` deltaP `18.3646` edge `0.0767` maxDD `-2.164`
- `news_risk_high->crypto_alt_24h` score `1.4123` n `51` status `ready` deltaP `24.4792` edge `-0.0455` maxDD `0.0`
- `news_risk_high->fx_1h` score `1.2004` n `53` status `ready` deltaP `16.5179` edge `0.0069` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.4487` n `53` status `ready` deltaP `10.9762` edge `-0.0045` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4372` n `53` status `ready` deltaP `13.3742` edge `0.0033` maxDD `-0.9128`
- `news_risk_high->metal_24h` score `0.3173` n `51` status `ready` deltaP `25.9906` edge `-0.1426` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `0.2633` n `133` status `ready` deltaP `12.3204` edge `-0.0153` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.1149` n `53` status `ready` deltaP `6.6613` edge `0.0049` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.076` n `53` status `ready` deltaP `3.8499` edge `-0.0001` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4109` n `133` status `ready` deltaP `3.0976` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5517` n `53` status `ready` deltaP `-1.6608` edge `-0.0123` maxDD `-0.1413`
- `market_context_high->unknown_24h` score `-0.6187` n `125` status `ready` deltaP `7.9861` edge `-0.1048` maxDD `0.0`
- `news_risk_high->metal_4h` score `-0.7455` n `53` status `ready` deltaP `2.833` edge `-0.0279` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
