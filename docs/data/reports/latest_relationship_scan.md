# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T13:37:29.528437+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `773.4324` n `136` status `ready` deltaP `1.2153` edge `64.4446` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.408` n `40` status `ready` deltaP `10.3743` edge `12.9695` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `57.5257` n `36` status `ready` deltaP `29.6875` edge `4.631` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.8216` n `36` status `ready` deltaP `35.5903` edge `2.3626` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `29.2378` n `36` status `ready` deltaP `14.4097` edge `2.3784` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.5453` n `36` status `ready` deltaP `32.9861` edge `0.501` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `4.9118` n `40` status `ready` deltaP `19.6037` edge `0.3329` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.398` n `36` status `ready` deltaP `39.4098` edge `0.1276` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.9825` n `40` status `ready` deltaP `24.8476` edge `0.1997` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.2013` n `40` status `ready` deltaP `35.0915` edge `0.0399` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.5553` n `40` status `ready` deltaP `10.2439` edge `0.2351` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7766` n `40` status `ready` deltaP `19.4611` edge `0.0586` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.6072` n `40` status `ready` deltaP `11.3623` edge `0.1471` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.4419` n `40` status `ready` deltaP `11.5569` edge `0.1289` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.0535` n `40` status `ready` deltaP `14.6108` edge `0.0099` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9137` n `40` status `ready` deltaP `15.5389` edge `0.0082` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.8766` n `136` status `ready` deltaP `16.6463` edge `0.0316` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4122` n `136` status `ready` deltaP `14.7366` edge `0.1216` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.4069` n `40` status `ready` deltaP `7.5305` edge `0.0216` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.1378` n `139` status `ready` deltaP `2.1648` edge `0.0031` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
