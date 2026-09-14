# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T10:22:26.096789+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_1h` score `442.8305` n `82` status `ready` deltaP `-6.1487` edge `36.9857` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.3105` n `82` status `ready` deltaP `41.781` edge `1.4628` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.2308` n `82` status `ready` deltaP `34.464` edge `1.3532` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.1098` n `82` status `ready` deltaP `35.4844` edge `0.9506` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2464` n `82` status `ready` deltaP `59.3199` edge `0.3094` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `7.0855` n `88` status `ready` deltaP `40.1042` edge `0.3231` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2155` n `41` status `ready` deltaP `40.1042` edge `0.2506` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2155` n `41` status `ready` deltaP `40.1042` edge `0.2506` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.85` n `82` status `ready` deltaP `35.1626` edge `0.2985` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.1024` n `41` status `ready` deltaP `57.1096` edge `0.0487` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.1024` n `41` status `ready` deltaP `57.1096` edge `0.0487` maxDD `-0.0054`
- `news_risk_high->unknown_4h` score `4.9533` n `82` status `ready` deltaP `-20.5793` edge `0.6393` maxDD `-4.1464`
- `market_context_high->fx_24h` score `4.5931` n `88` status `ready` deltaP `52.7304` edge `0.0528` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9511` n `52` status `ready` deltaP `26.2899` edge `0.0223` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9511` n `52` status `ready` deltaP `26.2899` edge `0.0223` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7514` n `137` status `ready` deltaP `21.6998` edge `0.0431` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7238` n `137` status `ready` deltaP `12.5126` edge `0.0146` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6669` n `82` status `ready` deltaP `16.311` edge `0.0396` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3421` n `137` status `ready` deltaP `12.293` edge `0.0095` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2084` n `52` status `ready` deltaP `6.8978` edge `0.0066` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
