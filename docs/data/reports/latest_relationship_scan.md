# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T06:37:30.283141+00:00`
- Price records: `672`
- Market context records: `6471`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5859`

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

- `news_risk_high->crypto_alt_24h` score `12.3156` n `32` status `ready` deltaP `32.8125` edge `0.8223` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.0076` n `153` status `ready` deltaP `16.5442` edge `0.8037` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3956` n `32` status `ready` deltaP `53.125` edge `0.1788` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1339` n `32` status `ready` deltaP `43.064` edge `0.062` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.9923` n `32` status `ready` deltaP `15.1042` edge `0.4891` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.3137` n `32` status `ready` deltaP `30.2083` edge `0.0953` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6598` n `172` status `ready` deltaP `-5.337` edge `0.264` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `0.605` n `38` status `ready` deltaP `5.3498` edge `0.0956` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4075` n `172` status `ready` deltaP `11.0395` edge `0.028` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.3035` n `153` status `ready` deltaP `6.6176` edge `0.168` maxDD `-5.2791`
- `market_context_high->unknown_4h` score `0.2969` n `172` status `ready` deltaP `-15.0879` edge `0.3659` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.1278` n `172` status `ready` deltaP `7.7886` edge `0.1141` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.103` n `38` status `ready` deltaP `1.8831` edge `0.0516` maxDD `-2.0756`
- `market_context_high->metal_4h` score `0.0823` n `172` status `ready` deltaP `10.8267` edge `0.0435` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4626` n `32` status `ready` deltaP `4.6875` edge `-0.0034` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5193` n `172` status `ready` deltaP `1.497` edge `0.0012` maxDD `-1.8877`
- `news_risk_high->unknown_1h` score `-0.5288` n `38` status `ready` deltaP `4.3019` edge `-0.0356` maxDD `-0.9718`
- `market_context_high->equity_4h` score `-0.5383` n `172` status `ready` deltaP `7.2249` edge `0.0527` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5829` n `172` status `ready` deltaP `-0.3342` edge `-0.0042` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
