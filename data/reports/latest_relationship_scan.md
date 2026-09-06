# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T16:07:30.140125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `risk_on_high->unknown_24h` score `130.9351` n `108` status `ready` deltaP `23.8426` edge `10.7633` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `130.9351` n `108` status `ready` deltaP `23.8426` edge `10.7633` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `12.962` n `108` status `ready` deltaP `26.5046` edge `1.2454` maxDD `-21.6879`
- `risk_on_and_context->crypto_major_24h` score `12.962` n `108` status `ready` deltaP `26.5046` edge `1.2454` maxDD `-21.6879`
- `risk_on_high->crypto_alt_24h` score `4.3162` n `108` status `ready` deltaP `14.757` edge `0.5949` maxDD `-20.0213`
- `risk_on_and_context->crypto_alt_24h` score `4.3162` n `108` status `ready` deltaP `14.757` edge `0.5949` maxDD `-20.0213`
- `market_context_high->equity_24h` score `3.8415` n `196` status `ready` deltaP `17.3682` edge `0.3672` maxDD `-7.3623`
- `market_context_high->crypto_alt_24h` score `2.2924` n `196` status `ready` deltaP `15.8341` edge `0.4444` maxDD `-21.3807`
- `risk_on_high->equity_24h` score `1.6477` n `108` status `ready` deltaP `10.301` edge `0.2315` maxDD `-7.3623`
- `risk_on_and_context->equity_24h` score `1.6477` n `108` status `ready` deltaP `10.301` edge `0.2315` maxDD `-7.3623`
- `market_context_high->index_24h` score `0.018` n `196` status `ready` deltaP `14.8916` edge `0.0787` maxDD `-4.7851`
- `risk_on_high->index_1h` score `-0.1172` n `130` status `ready` deltaP `4.977` edge `-0.0035` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1172` n `130` status `ready` deltaP `4.977` edge `-0.0035` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.2948` n `130` status `ready` deltaP `5.4514` edge `-0.0029` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.2948` n `130` status `ready` deltaP `5.4514` edge `-0.0029` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.352` n `130` status `ready` deltaP `2.3031` edge `0.057` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.352` n `130` status `ready` deltaP `2.3031` edge `0.057` maxDD `-5.4685`
- `risk_on_high->index_24h` score `-0.4428` n `108` status `ready` deltaP `9.3171` edge `0.0461` maxDD `-4.2757`
- `risk_on_and_context->index_24h` score `-0.4428` n `108` status `ready` deltaP `9.3171` edge `0.0461` maxDD `-4.2757`
- `risk_on_high->equity_1h` score `-0.4661` n `130` status `ready` deltaP `6.3612` edge `-0.0147` maxDD `-2.6638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
