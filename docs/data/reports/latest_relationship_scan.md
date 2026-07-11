# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T20:52:25.262230+00:00`
- Price records: `672`
- Market context records: `6428`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `12.0531` n `32` status `ready` deltaP `31.0764` edge `0.812` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.6134` n `146` status `ready` deltaP `19.7964` edge `0.8325` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5532` n `32` status `ready` deltaP `55.0347` edge `0.1792` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1473` n `32` status `ready` deltaP `43.2165` edge `0.0621` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.0974` n `32` status `ready` deltaP `35.0694` edge `0.1282` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.458` n `32` status `ready` deltaP `12.6736` edge `0.4368` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.459` n `32` status `ready` deltaP `29.6407` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4967` n `32` status `ready` deltaP `14.128` edge `0.1444` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.0187` n `198` status `ready` deltaP `-6.2859` edge `0.2169` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8412` n `32` status `ready` deltaP `9.8241` edge `0.0885` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.2151` n `193` status `ready` deltaP `9.7072` edge `0.0412` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.1931` n `193` status `ready` deltaP `9.0642` edge `0.0233` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2046` n `32` status `ready` deltaP `7.1295` edge `-0.0301` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3469` n `146` status `ready` deltaP `17.5751` edge `0.0952` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5454` n `198` status `ready` deltaP `0.8604` edge `0.0021` maxDD `-1.8877`
- `news_risk_high->metal_1h` score `-0.5885` n `32` status `ready` deltaP `-0.1497` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.6161` n `193` status `ready` deltaP `6.6584` edge `0.0465` maxDD `-8.2573`
- `market_context_high->unknown_4h` score `-0.6169` n `193` status `ready` deltaP `-14.766` edge `0.2876` maxDD `-10.5788`
- `market_context_high->commodity_1h` score `-0.6307` n `198` status `ready` deltaP `-1.553` edge `-0.0022` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6953` n `198` status `ready` deltaP `-3.0122` edge `0.0029` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
