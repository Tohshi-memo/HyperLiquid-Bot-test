# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T12:37:31.564642+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `202.0585` n `88` status `ready` deltaP `-21.512` edge `26.3167` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.5721` n `88` status `ready` deltaP `41.3037` edge `0.3614` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.6528` n `120` status `ready` deltaP `16.0265` edge `0.078` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.1023` n `125` status `ready` deltaP `1.9066` edge `0.0199` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.1404` n `120` status `ready` deltaP `5.3354` edge `0.0069` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.1635` n `125` status `ready` deltaP `0.8539` edge `0.0015` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5518` n `125` status `ready` deltaP `1.0551` edge `-0.0062` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8177` n `125` status `ready` deltaP `-7.4359` edge `-0.0031` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.9893` n `120` status `ready` deltaP `6.7277` edge `-0.0143` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.5906` n `88` status `ready` deltaP `-9.9274` edge `0.023` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-1.6798` n `88` status `ready` deltaP `-5.9659` edge `0.0756` maxDD `-7.0954`
- `market_context_high->equity_1h` score `-1.6829` n `125` status `ready` deltaP `-9.8826` edge `-0.0459` maxDD `-4.9849`
- `market_context_high->index_24h` score `-1.9745` n `88` status `ready` deltaP `-4.6717` edge `-0.068` maxDD `-2.3194`
- `market_context_high->crypto_alt_1h` score `-1.9999` n `125` status `ready` deltaP `-1.5461` edge `-0.0224` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.0241` n `125` status `ready` deltaP `-4.6994` edge `-0.032` maxDD `-5.4277`
- `market_context_high->index_4h` score `-2.0722` n `120` status `ready` deltaP `-12.2765` edge `-0.0096` maxDD `-0.8328`
- `market_context_high->crypto_major_4h` score `-3.5488` n `120` status `ready` deltaP `1.0671` edge `-0.0671` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-4.6463` n `88` status `ready` deltaP `-3.267` edge `0.0118` maxDD `-35.189`
- `market_context_high->equity_4h` score `-5.407` n `120` status `ready` deltaP `-29.3902` edge `-0.1927` maxDD `-15.3661`
- `market_context_high->unknown_1h` score `-7.2048` n `125` status `ready` deltaP `-0.4467` edge `-0.5517` maxDD `-1.3246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
