# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T18:22:29.474161+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8954`

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

- `market_context_high->crypto_major_24h` score `8.6845` n `59` status `ready` deltaP `27.9984` edge `1.3131` maxDD `-25.5749`
- `market_context_high->crypto_alt_24h` score `4.9094` n `59` status `ready` deltaP `16.0193` edge `1.0765` maxDD `-38.644`
- `risk_on_high->crypto_alt_4h` score `4.398` n `48` status `ready` deltaP `19.1057` edge `0.2839` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.398` n `48` status `ready` deltaP `19.1057` edge `0.2839` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.7468` n `48` status `ready` deltaP `33.7399` edge `0.3407` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7468` n `48` status `ready` deltaP `33.7399` edge `0.3407` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.6961` n `100` status `ready` deltaP `14.189` edge `0.3583` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.3738` n `100` status `ready` deltaP `17.5732` edge `0.3199` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6017` n `100` status `ready` deltaP `12.0539` edge `0.1482` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9803` n `48` status `ready` deltaP `6.3872` edge `0.0988` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9803` n `48` status `ready` deltaP `6.3872` edge `0.0988` maxDD `-2.4421`
- `market_context_high->unknown_4h` score `0.8195` n `100` status `ready` deltaP `-3.9268` edge `0.1591` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.6896` n `100` status `ready` deltaP `4.497` edge `0.1038` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4365` n `48` status `ready` deltaP `5.6637` edge `0.0835` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4365` n `48` status `ready` deltaP `5.6637` edge `0.0835` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.018` n `100` status `ready` deltaP `4.7508` edge `0.0037` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1477` n `100` status `ready` deltaP `5.9521` edge `0.0041` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.2824` n `100` status `ready` deltaP `9.2195` edge `0.0103` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3303` n `48` status `ready` deltaP `3.1188` edge `0.0036` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3303` n `48` status `ready` deltaP `3.1188` edge `0.0036` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
