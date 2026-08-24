# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T05:52:21.874056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `50.9907` n `51` status `ready` deltaP `17.0139` edge `4.1358` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3755` n `51` status `ready` deltaP `40.237` edge `1.0228` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9049` n `51` status `ready` deltaP `23.1916` edge `0.9254` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8` n `51` status `ready` deltaP `48.9481` edge `0.1722` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.5915` n `51` status `ready` deltaP `26.1657` edge `0.2019` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5287` n `51` status `ready` deltaP `15.8858` edge `0.2186` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2394` n `51` status `ready` deltaP `38.0829` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.3206` n `145` status `ready` deltaP `22.3938` edge `0.0621` maxDD `-0.4407`
- `news_risk_high->metal_24h` score `1.8701` n `51` status `ready` deltaP `35.3656` edge `-0.0757` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2697` n `51` status `ready` deltaP `17.2948` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->crypto_alt_24h` score `1.0292` n `51` status `ready` deltaP `25.0` edge `-0.0809` maxDD `0.0`
- `news_risk_high->equity_1h` score `0.9343` n `51` status `ready` deltaP `18.193` edge `0.0349` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9107` n `51` status `ready` deltaP `13.5491` edge `0.0253` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2496` n `51` status `ready` deltaP `9.4223` edge `0.0045` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1763` n `51` status `ready` deltaP `8.3891` edge `-0.0104` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `-0.1029` n `51` status `ready` deltaP `2.3424` edge `-0.0065` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1085` n `51` status `ready` deltaP `7.8252` edge `-0.0081` maxDD `-0.249`
- `market_context_high->unknown_1h` score `-0.2642` n `154` status `ready` deltaP `9.5069` edge `-0.0405` maxDD `-1.5916`
- `market_context_high->fx_24h` score `-0.2726` n `92` status `ready` deltaP `7.4728` edge `0.0023` maxDD `-1.9653`
- `market_context_high->metal_4h` score `-0.3121` n `145` status `ready` deltaP `5.2964` edge `-0.0198` maxDD `-1.4421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
