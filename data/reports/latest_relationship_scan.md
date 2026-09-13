# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T20:52:24.094340+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12657`

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

- `market_context_high->unknown_24h` score `17681.1228` n `56` status `ready` deltaP `10.2093` edge `1473.379` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `8931.0737` n `35` status `ready` deltaP `10.5665` edge `744.1922` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `8931.0737` n `35` status `ready` deltaP `10.5665` edge `744.1922` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `429.0256` n `82` status `ready` deltaP `-5.4002` edge `35.8303` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.7087` n `82` status `ready` deltaP `36.2027` edge `1.3665` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3292` n `82` status `ready` deltaP `38.0236` edge `1.421` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.7625` n `82` status `ready` deltaP `28.8225` edge `0.7994` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.3124` n `82` status `ready` deltaP `52.5946` edge `0.2764` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.8203` n `82` status `ready` deltaP `27.0017` edge `0.2671` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.8098` n `35` status `ready` deltaP `39.8276` edge `0.1353` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8098` n `35` status `ready` deltaP `39.8276` edge `0.1353` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6814` n `56` status `ready` deltaP `39.8276` edge `0.1246` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `3.5643` n `56` status `ready` deltaP `5.0616` edge `0.4294` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `3.4791` n `35` status `ready` deltaP `1.8473` edge `0.4112` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `3.4791` n `35` status `ready` deltaP `1.8473` edge `0.4112` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `1.9653` n `35` status `ready` deltaP `42.734` edge `0.0189` maxDD `-1.1462`
- `risk_on_and_context->fx_24h` score `1.9653` n `35` status `ready` deltaP `42.734` edge `0.0189` maxDD `-1.1462`
- `risk_on_high->commodity_4h` score `1.2109` n `59` status `ready` deltaP `18.1558` edge `0.0152` maxDD `-0.1596`
- `risk_on_and_context->commodity_4h` score `1.2109` n `59` status `ready` deltaP `18.1558` edge `0.0152` maxDD `-0.1596`
- `market_context_high->commodity_4h` score `0.9629` n `130` status `ready` deltaP `16.0436` edge `0.0151` maxDD `-0.345`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
