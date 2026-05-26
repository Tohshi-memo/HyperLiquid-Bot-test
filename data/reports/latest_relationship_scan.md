# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T17:07:18.691251+00:00`
- Price records: `672`
- Market context records: `1958`
- Flow alert records: `7531`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7565`

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

- `market_context_high->crypto_alt_4h` score `6.9837` n `233` status `ready` deltaP `21.681` edge `0.5519` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4487` n `233` status `ready` deltaP `25.335` edge `0.4931` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4256` n `233` status `ready` deltaP `13.4585` edge `0.3148` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1882` n `233` status `ready` deltaP `14.1153` edge `0.1977` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.1967` n `199` status `ready` deltaP `16.4203` edge `0.5223` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.8337` n `234` status `ready` deltaP `8.5035` edge `0.1114` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6205` n `234` status `ready` deltaP `7.4966` edge `0.1131` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.5146` n `199` status `ready` deltaP `12.6721` edge `0.201` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.2216` n `233` status `ready` deltaP `8.6204` edge `0.0699` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.2017` n `199` status `ready` deltaP `4.1922` edge `0.1117` maxDD `-4.1604`
- `market_context_high->equity_24h` score `0.0231` n `199` status `ready` deltaP `11.3505` edge `0.4161` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.2278` n `234` status `ready` deltaP `4.6497` edge `0.0294` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2555` n `199` status `ready` deltaP `9.9323` edge `0.0174` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6506` n `234` status `ready` deltaP `-3.0132` edge `-0.0001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6533` n `234` status `ready` deltaP `0.485` edge `0.0055` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-1.0912` n `233` status `ready` deltaP `-7.1823` edge `-0.0032` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2616` n `234` status `ready` deltaP `3.3971` edge `0.0058` maxDD `-6.3532`
- `market_context_high->crypto_major_24h` score `-1.4224` n `199` status `ready` deltaP `15.892` edge `0.6341` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.6114` n `234` status `ready` deltaP `0.0602` edge `-0.0395` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.8377` n `233` status `ready` deltaP `6.8611` edge `0.0703` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
