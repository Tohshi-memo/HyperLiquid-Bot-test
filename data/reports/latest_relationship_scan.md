# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T01:07:32.262539+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5392`

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

- `market_context_high->unknown_4h` score `103.2422` n `97` status `ready` deltaP `2.7564` edge `8.6163` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `101.5855` n `97` status `ready` deltaP `0.1389` edge `8.506` maxDD `-0.9839`
- `news_risk_high->crypto_major_4h` score `9.6504` n `65` status `ready` deltaP `33.6187` edge `0.6004` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.8328` n `50` status `ready` deltaP `26.9792` edge `0.5381` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `6.6621` n `65` status `ready` deltaP `21.4634` edge `0.5465` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `6.5217` n `50` status `ready` deltaP `21.2361` edge `0.5292` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.0202` n `65` status `ready` deltaP `17.1101` edge `0.3143` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `3.9839` n `97` status `ready` deltaP `17.5997` edge `0.285` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.5389` n `65` status `ready` deltaP `24.8264` edge `0.1294` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.0304` n `65` status `ready` deltaP `22.1013` edge `0.1662` maxDD `-2.881`
- `news_risk_high->index_4h` score `2.974` n `65` status `ready` deltaP `32.6759` edge `0.0562` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6763` n `65` status `ready` deltaP `11.064` edge `0.1848` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.1803` n `65` status `ready` deltaP `19.8406` edge `0.091` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1237` n `65` status `ready` deltaP `26.216` edge `0.0172` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9378` n `97` status `ready` deltaP `13.9824` edge `0.1133` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.4791` n `65` status `ready` deltaP `4.8687` edge `0.1427` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4686` n `97` status `ready` deltaP `25.5831` edge `0.0275` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.4031` n `50` status `ready` deltaP `26.6667` edge `0.1039` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9935` n `97` status `ready` deltaP `15.3157` edge `0.0071` maxDD `-0.113`
- `market_context_high->crypto_alt_4h` score `0.7754` n `97` status `ready` deltaP `3.3191` edge `0.2214` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
