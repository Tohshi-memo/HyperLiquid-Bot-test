# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T20:07:40.093657+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5901`

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

- `news_risk_high->unknown_24h` score `4481.7464` n `67` status `ready` deltaP `24.4118` edge `373.3582` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `16.3947` n `40` status `ready` deltaP `55.1042` edge `1.0386` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0694` n `40` status `ready` deltaP `51.3194` edge `0.5931` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.6064` n `67` status `ready` deltaP `17.2847` edge `0.345` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6339` n `67` status `ready` deltaP `16.2177` edge `0.0661` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0927` n `40` status `ready` deltaP `14.2073` edge `0.13` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.71` n `40` status `ready` deltaP `8.3537` edge `0.1259` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.67` n `40` status `ready` deltaP `12.3952` edge `0.0407` maxDD `-1.3282`
- `news_risk_high->equity_1h` score `0.66` n `67` status `ready` deltaP `9.9875` edge `0.0707` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.6519` n `40` status `ready` deltaP `20.4573` edge `0.0268` maxDD `-1.3685`
- `market_context_high->fx_1h` score `0.4606` n `40` status `ready` deltaP `14.1467` edge `0.0025` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.3846` n `67` status `ready` deltaP `15.1961` edge `0.0265` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1457` n `67` status `ready` deltaP `5.9224` edge `0.0268` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1012` n `67` status `ready` deltaP `6.417` edge `0.0384` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.0487` n `67` status `ready` deltaP `2.8287` edge `0.0072` maxDD `-0.5845`
- `news_risk_high->fx_1h` score `-0.089` n `67` status `ready` deltaP `2.393` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0966` n `67` status `ready` deltaP `3.2778` edge `0.0061` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.2021` n `67` status `ready` deltaP `2.6879` edge `0.0282` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.4635` n `40` status `ready` deltaP `-0.2994` edge `0.0053` maxDD `-3.0178`
- `news_risk_high->commodity_1h` score `-0.6501` n `67` status `ready` deltaP `3.1415` edge `-0.0263` maxDD `-2.9058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
