# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T15:52:19.258461+00:00`
- Price records: `672`
- Market context records: `1952`
- Flow alert records: `7515`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.0406` n `232` status `ready` deltaP `21.8232` edge `0.5557` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4933` n `232` status `ready` deltaP `25.5023` edge `0.4957` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.3726` n `232` status `ready` deltaP `13.4268` edge `0.3106` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0588` n `232` status `ready` deltaP `14.1325` edge `0.1868` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.0121` n `199` status `ready` deltaP `16.0778` edge `0.5092` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.8349` n `234` status `ready` deltaP `8.3538` edge `0.1125` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6684` n `234` status `ready` deltaP `7.6463` edge `0.1161` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2846` n `199` status `ready` deltaP `11.9871` edge `0.1864` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1333` n `199` status `ready` deltaP `4.1922` edge `0.106` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1282` n `232` status `ready` deltaP `8.3225` edge `0.0641` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2134` n `234` status `ready` deltaP `4.6497` edge `0.0306` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2615` n `199` status `ready` deltaP `9.9323` edge `0.0169` maxDD `-1.3925`
- `market_context_high->equity_24h` score `-0.2782` n `199` status `ready` deltaP `10.4943` edge `0.3967` maxDD `-33.1875`
- `market_context_high->index_1h` score `-0.6221` n `234` status `ready` deltaP `0.6347` edge `0.0071` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6421` n `234` status `ready` deltaP `-2.8635` edge `0.0` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0664` n `232` status `ready` deltaP `-6.735` edge `-0.003` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2496` n `234` status `ready` deltaP `3.3971` edge `0.0068` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.5563` n `234` status `ready` deltaP `0.3596` edge `-0.0369` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.7069` n `199` status `ready` deltaP `15.0358` edge `0.6161` maxDD `-62.3533`
- `market_context_high->metal_4h` score `-1.8468` n `232` status `ready` deltaP `6.7174` edge `0.0705` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
