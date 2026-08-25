# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T23:57:39.448873+00:00`
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

- `news_risk_high->unknown_24h` score `45.5294` n `51` status `ready` deltaP `9.7222` edge `3.7293` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.673` n `53` status `ready` deltaP `24.8274` edge `0.9005` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.1421` n `51` status `ready` deltaP `29.9939` edge `0.4883` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9824` n `51` status `ready` deltaP `40.2676` edge `0.0786` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.3169` n `53` status `ready` deltaP `16.3117` edge `0.2032` maxDD `-0.8426`
- `news_risk_high->crypto_alt_24h` score `3.0884` n `51` status `ready` deltaP `26.2153` edge `0.0826` maxDD `0.0`
- `news_risk_high->fx_4h` score `2.9628` n `53` status `ready` deltaP `35.4205` edge `0.0242` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.7144` n `133` status `ready` deltaP `22.969` edge `0.1139` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.5156` n `53` status `ready` deltaP `18.517` edge `0.0799` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1381` n `53` status `ready` deltaP `15.7694` edge `0.0067` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.7417` n `51` status `ready` deltaP `27.7267` edge `-0.1188` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4631` n `53` status `ready` deltaP `11.1259` edge `-0.0043` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3866` n `53` status `ready` deltaP `12.7754` edge `0.0008` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.2994` n `133` status `ready` deltaP `11.8713` edge `-0.0093` maxDD `-1.5916`
- `news_risk_high->index_4h` score `-0.0105` n `53` status `ready` deltaP `5.2894` edge `0.0036` maxDD `-0.1788`
- `market_context_high->unknown_24h` score `-0.0778` n `125` status `ready` deltaP `9.7222` edge `-0.0713` maxDD `0.0`
- `news_risk_high->index_1h` score `-0.0861` n `53` status `ready` deltaP `3.7002` edge `-0.0004` maxDD `-0.1583`
- `market_context_high->fx_1h` score `-0.4514` n `133` status `ready` deltaP `2.3491` edge `-0.0003` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.578` n `53` status `ready` deltaP `-1.9602` edge `-0.0125` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7029` n `53` status `ready` deltaP `3.2904` edge `-0.0274` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
