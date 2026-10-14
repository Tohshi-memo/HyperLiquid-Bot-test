# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T15:22:37.093087+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9234`

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

- `market_context_high->crypto_alt_4h` score `6.7281` n `117` status `ready` deltaP `17.679` edge `0.5877` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.2068` n `54` status `ready` deltaP `32.0` edge `0.3039` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2068` n `54` status `ready` deltaP `32.0` edge `0.3039` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.9684` n `117` status `ready` deltaP `20.8151` edge `0.5145` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.317` n `54` status `ready` deltaP `19.9582` edge `0.3548` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.317` n `54` status `ready` deltaP `19.9582` edge `0.3548` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.4192` n `54` status `ready` deltaP `33.9205` edge `0.4257` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4192` n `54` status `ready` deltaP `33.9205` edge `0.4257` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7735` n `117` status `ready` deltaP `13.7162` edge `0.1631` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2634` n `117` status `ready` deltaP `5.9612` edge `0.1461` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2242` n `117` status `ready` deltaP `13.3078` edge `0.0345` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.3352` n `54` status `ready` deltaP `1.4028` edge `0.0199` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3352` n `54` status `ready` deltaP `1.4028` edge `0.0199` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.359` n `117` status `ready` deltaP `7.4147` edge `0.0076` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.378` n `117` status `ready` deltaP `0.6468` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.4477` n `54` status `ready` deltaP `2.0016` edge `0.0024` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4477` n `54` status `ready` deltaP `2.0016` edge `0.0024` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.5805` n `54` status `ready` deltaP `3.4598` edge `0.0051` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5805` n `54` status `ready` deltaP `3.4598` edge `0.0051` maxDD `-5.8734`
- `risk_on_high->metal_4h` score `-0.6352` n `54` status `ready` deltaP `0.9146` edge `0.017` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
