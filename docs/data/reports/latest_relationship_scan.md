# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T18:52:30.328254+00:00`
- Price records: `672`
- Market context records: `6008`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11142`

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

- `news_risk_high->fx_24h` score `7.6007` n `30` status `ready` deltaP `68.9236` edge `0.1739` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1737` n `30` status `ready` deltaP `43.2012` edge `0.0644` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7931` n `30` status `ready` deltaP `30.5903` edge `0.1327` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2322` n `30` status `ready` deltaP `26.7764` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1323` n `219` status `ready` deltaP `7.3804` edge `0.1546` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8044` n `30` status `ready` deltaP `10.3393` edge `0.0809` maxDD `-2.0691`
- `market_context_high->equity_24h` score `0.3058` n `193` status `ready` deltaP `24.633` edge `0.4064` maxDD `-31.6107`
- `news_risk_high->crypto_alt_1h` score `0.1912` n `30` status `ready` deltaP `5.4691` edge `0.0342` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1234` n `30` status `ready` deltaP `9.2361` edge `0.0414` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.4118` n `30` status `ready` deltaP `1.5369` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4846` n `219` status `ready` deltaP `2.5415` edge `0.0008` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.5721` n `219` status `ready` deltaP `2.0999` edge `0.0255` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.6007` n `219` status `ready` deltaP `-0.8346` edge `0.0019` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.6604` n `219` status `ready` deltaP `-0.4382` edge `-0.0013` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0392` n `30` status `ready` deltaP `-9.4012` edge `-0.0191` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.1381` n `219` status `ready` deltaP `-1.5926` edge `-0.0057` maxDD `-3.0339`
- `market_context_high->index_4h` score `-1.1596` n `219` status `ready` deltaP `0.3787` edge `0.0154` maxDD `-2.9939`
- `market_context_high->crypto_major_1h` score `-1.174` n `219` status `ready` deltaP `2.2571` edge `0.0112` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2152` n `219` status `ready` deltaP `1.3138` edge `0.0107` maxDD `-9.3536`
- `market_context_high->index_1h` score `-1.3378` n `219` status `ready` deltaP `-3.2825` edge `0.0016` maxDD `-1.2963`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
