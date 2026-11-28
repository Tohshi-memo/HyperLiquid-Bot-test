# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T18:07:30.254230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7476`

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

- `news_risk_high->unknown_1h` score `3439.3644` n `31` status `ready` deltaP `2.231` edge `286.6164` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3271.3445` n `31` status `ready` deltaP `3.3291` edge `272.5955` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `25.28` n `31` status `ready` deltaP `38.9948` edge `1.8467` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.4779` n `31` status `ready` deltaP `37.0884` edge `1.3759` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.1966` n `31` status `ready` deltaP `29.4627` edge `0.9033` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.5119` n `31` status `ready` deltaP `24.7787` edge `0.7145` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.0258` n `31` status `ready` deltaP `33.871` edge `0.3244` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.9916` n `31` status `ready` deltaP `18.9123` edge `0.7838` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.193` n `31` status `ready` deltaP `43.1822` edge `0.1577` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9086` n `31` status `ready` deltaP `17.0403` edge `0.2396` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.7363` n `31` status `ready` deltaP `33.2612` edge `0.0323` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.515` n `31` status `ready` deltaP `26.8631` edge `0.0305` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3906` n `31` status `ready` deltaP `29.2979` edge `0.0124` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.3222` n `31` status `ready` deltaP `15.4964` edge `0.1089` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.115` n `31` status `ready` deltaP `7.316` edge `0.2685` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0125` n `31` status `ready` deltaP `11.2082` edge `0.219` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1714` n `31` status `ready` deltaP `25.2414` edge `0.0098` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.5675` n `31` status `ready` deltaP `12.4852` edge `0.0293` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.5609` n `65` status `ready` deltaP `11.5244` edge `0.0095` maxDD `-0.1673`
- `news_risk_high->metal_4h` score `0.4844` n `31` status `ready` deltaP `13.7293` edge `0.0263` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
