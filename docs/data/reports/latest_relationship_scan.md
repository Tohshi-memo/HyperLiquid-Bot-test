# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T20:22:30.127579+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12744`

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

- `market_context_high->unknown_24h` score `17680.0296` n `56` status `ready` deltaP `10.2093` edge `1473.2879` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `8931.1913` n `35` status `ready` deltaP `10.5665` edge `744.202` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `8931.1913` n `35` status `ready` deltaP `10.5665` edge `744.202` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `429.3759` n `82` status `ready` deltaP `-5.1008` edge `35.8575` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6883` n `82` status `ready` deltaP `36.2027` edge `1.3648` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3328` n `82` status `ready` deltaP `38.0236` edge `1.4213` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.6677` n `82` status `ready` deltaP `28.4777` edge `0.7938` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.2716` n `82` status `ready` deltaP `52.2497` edge `0.2753` maxDD `-0.0797`
- `risk_on_high->commodity_24h` score `4.817` n `35` status `ready` deltaP `39.8276` edge `0.1359` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.817` n `35` status `ready` deltaP `39.8276` edge `0.1359` maxDD `0.0`
- `news_risk_high->metal_24h` score `4.8017` n `82` status `ready` deltaP `26.8293` edge `0.2667` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.619` n `56` status `ready` deltaP `39.8276` edge `0.1194` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.7611` n `56` status `ready` deltaP `5.0616` edge `0.4458` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `3.4587` n `35` status `ready` deltaP `1.8473` edge `0.4095` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.4587` n `35` status `ready` deltaP `1.8473` edge `0.4095` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `1.9872` n `35` status `ready` deltaP `43.0788` edge `0.0194` maxDD `-1.1462`
- `risk_on_and_context->fx_24h` score `1.9872` n `35` status `ready` deltaP `43.0788` edge `0.0194` maxDD `-1.1462`
- `risk_on_high->commodity_4h` score `1.2389` n `59` status `ready` deltaP `18.4607` edge `0.0155` maxDD `-0.1596`
- `risk_on_and_context->commodity_4h` score `1.2389` n `59` status `ready` deltaP `18.4607` edge `0.0155` maxDD `-0.1596`
- `market_context_high->commodity_4h` score `0.8734` n `131` status `ready` deltaP `15.0449` edge `0.0143` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
