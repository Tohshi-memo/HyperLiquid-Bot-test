# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T16:37:31.132732+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10109`

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

- `risk_on_high->unknown_24h` score `131.3251` n `108` status `ready` deltaP `24.5949` edge `10.7897` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `131.3251` n `108` status `ready` deltaP `24.5949` edge `10.7897` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `14.2842` n `108` status `ready` deltaP `28.0093` edge `1.2854` maxDD `-17.5424`
- `risk_on_and_context->crypto_major_24h` score `14.2842` n `108` status `ready` deltaP `28.0093` edge `1.2854` maxDD `-17.5424`
- `risk_on_high->crypto_alt_24h` score `5.5749` n `108` status `ready` deltaP `16.2616` edge `0.643` maxDD `-16.9467`
- `risk_on_and_context->crypto_alt_24h` score `5.5749` n `108` status `ready` deltaP `16.2616` edge `0.643` maxDD `-16.9467`
- `market_context_high->equity_24h` score `4.2395` n `196` status `ready` deltaP `18.0413` edge `0.3726` maxDD `-6.1664`
- `market_context_high->crypto_alt_24h` score `3.1655` n `196` status `ready` deltaP `16.5073` edge `0.4659` maxDD `-18.3062`
- `risk_on_high->equity_24h` score `2.1939` n `108` status `ready` deltaP `11.8055` edge `0.2437` maxDD `-6.1664`
- `risk_on_and_context->equity_24h` score `2.1939` n `108` status `ready` deltaP `11.8055` edge `0.2437` maxDD `-6.1664`
- `market_context_high->index_24h` score `0.263` n `196` status `ready` deltaP `15.5648` edge `0.0805` maxDD `-4.321`
- `risk_on_high->index_24h` score `-0.106` n `108` status `ready` deltaP `10.8218` edge `0.05` maxDD `-3.8115`
- `risk_on_and_context->index_24h` score `-0.106` n `108` status `ready` deltaP `10.8218` edge `0.05` maxDD `-3.8115`
- `risk_on_high->index_1h` score `-0.1494` n `130` status `ready` deltaP `4.3574` edge `-0.0035` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1494` n `130` status `ready` deltaP `4.3574` edge `-0.0035` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.2317` n `130` status `ready` deltaP `2.9226` edge `0.0629` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2317` n `130` status `ready` deltaP `2.9226` edge `0.0629` maxDD `-5.4685`
- `risk_on_high->metal_1h` score `-0.3608` n `130` status `ready` deltaP `4.2123` edge `-0.0031` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.3608` n `130` status `ready` deltaP `4.2123` edge `-0.0031` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.4638` n `130` status `ready` deltaP `6.3612` edge `-0.0144` maxDD `-2.6638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
