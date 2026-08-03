# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T00:07:29.820045+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5918`

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

- `news_risk_high->unknown_24h` score `5165.2194` n `61` status `ready` deltaP `23.8245` edge `430.3182` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `15.0889` n `40` status `ready` deltaP `52.3264` edge `0.9483` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.1978` n `40` status `ready` deltaP `51.3194` edge `0.6038` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.3413` n `61` status `ready` deltaP `14.3168` edge `0.3427` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.388` n `61` status `ready` deltaP `13.2497` edge `0.0654` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `1.0573` n `40` status `ready` deltaP `13.9024` edge `0.1275` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.7687` n `40` status `ready` deltaP `8.5061` edge `0.1324` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.6551` n `40` status `ready` deltaP `20.6098` edge `0.0262` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.4243` n `44` status `ready` deltaP `8.6146` edge `0.0344` maxDD `-1.3282`
- `news_risk_high->equity_1h` score `0.257` n `61` status `ready` deltaP `6.3144` edge `0.0616` maxDD `-2.916`
- `market_context_high->fx_1h` score `0.2467` n `44` status `ready` deltaP `10.1388` edge `0.0018` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `-0.027` n `61` status `ready` deltaP `10.6508` edge `0.0225` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `-0.0303` n `61` status `ready` deltaP `3.5069` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.1283` n `61` status `ready` deltaP `1.7032` edge `0.0045` maxDD `-0.5845`
- `news_risk_high->metal_4h` score `-0.1878` n `61` status `ready` deltaP `2.2691` edge `0.0084` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `-0.1903` n `61` status `ready` deltaP `4.5475` edge `0.0135` maxDD `-3.1233`
- `news_risk_high->commodity_1h` score `-0.3282` n `61` status `ready` deltaP `5.8948` edge `-0.0136` maxDD `-2.0891`
- `news_risk_high->metal_1h` score `-0.3303` n `61` status `ready` deltaP `-0.3779` edge `0.0005` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.5335` n `61` status `ready` deltaP `0.2282` edge `0.0021` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.5521` n `44` status `ready` deltaP `-1.8236` edge `0.0041` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
