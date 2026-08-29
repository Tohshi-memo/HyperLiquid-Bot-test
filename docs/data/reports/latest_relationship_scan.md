# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T15:07:23.696341+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11348`

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

- `news_risk_high->unknown_24h` score `45.7972` n `60` status `ready` deltaP `10.9375` edge `3.8326` maxDD `-3.7936`
- `news_risk_high->crypto_alt_24h` score `20.9971` n `60` status `ready` deltaP `32.4306` edge `1.8394` maxDD `-20.4678`
- `market_context_high->unknown_24h` score `8.5754` n `104` status `ready` deltaP `19.9119` edge `0.6551` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3868` n `80` status `ready` deltaP `11.5854` edge `0.514` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.4854` n `104` status `ready` deltaP `32.5053` edge `0.259` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6092` n `80` status `ready` deltaP `5.2246` edge `0.2183` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.4924` n `80` status `ready` deltaP `36.0366` edge `0.0224` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.3599` n `117` status `ready` deltaP `17.782` edge `0.1213` maxDD `-0.7887`
- `news_risk_high->equity_24h` score `1.542` n `60` status `ready` deltaP `20.8681` edge `0.3161` maxDD `-17.2691`
- `market_context_high->unknown_1h` score `1.1214` n `129` status `ready` deltaP `9.8176` edge `0.0761` maxDD `-1.5148`
- `news_risk_high->metal_24h` score `0.9286` n `60` status `ready` deltaP `33.4028` edge `0.018` maxDD `-6.3973`
- `news_risk_high->fx_1h` score `0.7483` n `80` status `ready` deltaP `14.3413` edge `0.0056` maxDD `-0.108`
- `news_risk_high->crypto_major_24h` score `0.7069` n `60` status `ready` deltaP `17.2222` edge `0.3153` maxDD `-23.1588`
- `news_risk_high->index_24h` score `0.4497` n `60` status `ready` deltaP `16.9097` edge `0.0141` maxDD `-1.8674`
- `news_risk_high->commodity_1h` score `0.3987` n `80` status `ready` deltaP `11.7515` edge `0.0048` maxDD `-0.5618`
- `market_context_high->crypto_major_4h` score `-0.0232` n `117` status `ready` deltaP `18.5611` edge `0.2194` maxDD `-20.9394`
- `market_context_high->metal_4h` score `-0.282` n `117` status `ready` deltaP `7.0305` edge `0.0087` maxDD `-3.3377`
- `market_context_high->crypto_alt_4h` score `-0.3724` n `117` status `ready` deltaP `20.8477` edge `0.3146` maxDD `-31.4361`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->commodity_1h` score `-0.5371` n `129` status `ready` deltaP `-1.1361` edge `0.0081` maxDD `-1.5507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
