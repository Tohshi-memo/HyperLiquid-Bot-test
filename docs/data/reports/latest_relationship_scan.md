# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T16:22:24.600146+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3277.2601` n `31` status `ready` deltaP `1.6322` edge `273.1117` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3179.7509` n `31` status `ready` deltaP `3.3291` edge `264.9627` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.1634` n `31` status `ready` deltaP `25.8681` edge `1.1745` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.3852` n `31` status `ready` deltaP `24.3056` edge `0.9534` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.7956` n `31` status `ready` deltaP `25.0` edge `0.8163` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.7865` n `31` status `ready` deltaP `20.2055` edge `0.6012` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.6853` n `31` status `ready` deltaP `30.3649` edge `0.3194` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8394` n `31` status `ready` deltaP `13.1196` edge `0.6747` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6358` n `31` status `ready` deltaP `38.5865` edge `0.1419` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9455` n `31` status `ready` deltaP `12.416` edge `0.2735` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.468` n `31` status `ready` deltaP `29.9076` edge `0.0323` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.409` n `31` status `ready` deltaP `25.8681` edge `0.0283` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.3366` n `31` status `ready` deltaP `15.4964` edge `0.1101` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3152` n `31` status `ready` deltaP `28.25` edge `0.0131` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.8959` n `31` status `ready` deltaP `5.9687` edge `0.2494` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6797` n `31` status `ready` deltaP `8.813` edge `0.1923` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.2002` n `31` status `ready` deltaP `25.6905` edge `0.0105` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3404` n `31` status `ready` deltaP `11.2903` edge `0.0241` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2383` n `31` status `ready` deltaP `8.6743` edge `0.0125` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4538` n `31` status `ready` deltaP `-2.9602` edge `0.0081` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
