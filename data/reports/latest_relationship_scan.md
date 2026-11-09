# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T08:07:29.408734+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8006`

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

- `market_context_high->equity_24h` score `9.2636` n `32` status `ready` deltaP `16.4931` edge `0.8993` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.4341` n `32` status `ready` deltaP `7.8125` edge `0.2095` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.3623` n `32` status `ready` deltaP `16.6667` edge `0.1098` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.8061` n `32` status `ready` deltaP `11.8056` edge `-0.0027` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.1438` n `76` status `ready` deltaP `6.3864` edge `0.0432` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.1142` n `76` status `ready` deltaP `0.5376` edge `0.0454` maxDD `-2.4235`
- `market_context_high->metal_1h` score `-0.255` n `88` status `ready` deltaP `4.8449` edge `0.0141` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4354` n `88` status `ready` deltaP `1.3405` edge `0.0035` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.4376` n `76` status `ready` deltaP `6.5227` edge `0.0129` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.8414` n `88` status `ready` deltaP `-5.1102` edge `0.0093` maxDD `-0.9814`
- `market_context_high->equity_1h` score `-1.1683` n `88` status `ready` deltaP `-5.2599` edge `0.0689` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.3023` n `88` status `ready` deltaP `-13.9085` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.6653` n `88` status `ready` deltaP `2.1298` edge `-0.0298` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.8024` n `32` status `ready` deltaP `-1.7361` edge `-0.1642` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.5503` n `76` status `ready` deltaP `-14.6422` edge `-0.0156` maxDD `-2.4335`
- `market_context_high->crypto_major_1h` score `-3.0178` n `88` status `ready` deltaP `-4.0623` edge `-0.0975` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-4.3462` n `32` status `ready` deltaP `-4.8611` edge `0.0345` maxDD `-23.1423`
- `market_context_high->equity_4h` score `-4.3466` n `76` status `ready` deltaP `4.0597` edge `-0.0113` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-8.6217` n `76` status `ready` deltaP `0.8505` edge `-0.245` maxDD `-31.6652`
- `market_context_high->crypto_alt_24h` score `-9.1774` n `32` status `ready` deltaP `-18.75` edge `-0.1819` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
