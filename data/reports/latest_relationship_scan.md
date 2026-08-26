# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T05:52:23.479506+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14824`

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

- `news_risk_high->unknown_24h` score `46.5078` n `51` status `ready` deltaP `11.6319` edge `3.7981` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.8188` n `53` status `ready` deltaP `23.1506` edge `0.8405` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `7.413` n `51` status `ready` deltaP `30.3819` edge `0.4152` maxDD `0.0`
- `news_risk_high->equity_24h` score `6.9921` n `51` status `ready` deltaP `29.9939` edge `0.4758` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.0268` n `51` status `ready` deltaP `40.2676` edge `0.0823` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.8059` n `53` status `ready` deltaP `33.7437` edge `0.0223` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7495` n `53` status `ready` deltaP `15.4135` edge `0.1619` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.544` n `134` status `ready` deltaP `21.3483` edge `0.1105` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.6869` n `53` status `ready` deltaP `19.2792` edge `0.0891` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.3341` n `51` status `ready` deltaP `29.1156` edge `-0.0787` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `1.0678` n `136` status `ready` deltaP `11.4873` edge `0.0573` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.0578` n `53` status `ready` deltaP `14.8712` edge `0.006` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.4655` n `53` status `ready` deltaP `11.1259` edge `-0.0041` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3679` n `53` status `ready` deltaP `12.476` edge `0.0004` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.0233` n `53` status `ready` deltaP `5.4418` edge `0.0054` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.1048` n `53` status `ready` deltaP `3.4008` edge `-0.0008` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4512` n `136` status `ready` deltaP `2.4128` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.5469` n `53` status `ready` deltaP `-1.5111` edge `-0.0129` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.8087` n `53` status `ready` deltaP `2.2233` edge `-0.0291` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-1.0459` n `53` status `ready` deltaP `-2.1255` edge `0.0034` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
