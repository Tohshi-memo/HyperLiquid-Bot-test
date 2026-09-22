# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T12:07:24.178206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `46.9882` n `46` status `ready` deltaP `7.3171` edge `3.8669` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.825` n `46` status `ready` deltaP `17.3536` edge `2.552` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.9146` n `46` status `ready` deltaP `16.4931` edge `1.2996` maxDD `0.0`
- `market_context_high->equity_24h` score `16.4603` n `46` status `ready` deltaP `13.0133` edge `1.295` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.568` n `46` status `ready` deltaP `20.1314` edge `0.3385` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.1079` n `101` status `ready` deltaP `-8.0016` edge `1.0815` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.1735` n `101` status `ready` deltaP `38.301` edge `0.2821` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.4237` n `101` status `ready` deltaP `12.2117` edge `0.2415` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2654` n `101` status `ready` deltaP `13.8362` edge `0.1431` maxDD `-2.058`
- `market_context_high->index_4h` score `2.0659` n `46` status `ready` deltaP `24.0787` edge `0.025` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.8535` n `101` status `ready` deltaP `15.2605` edge `0.1785` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.576` n `101` status `ready` deltaP `15.4829` edge `0.0804` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.2824` n `46` status `ready` deltaP `8.7487` edge `0.0792` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.027` n `101` status `ready` deltaP `16.8724` edge `0.0367` maxDD `-0.421`
- `market_context_high->equity_1h` score `1.0008` n `46` status `ready` deltaP `7.9602` edge `0.0546` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.8681` n `46` status `ready` deltaP `7.9069` edge `0.0791` maxDD `-2.7574`
- `market_context_high->metal_24h` score `0.7847` n `46` status `ready` deltaP `20.5314` edge `-0.0481` maxDD `-0.2042`
- `market_context_high->index_1h` score `0.7489` n `46` status `ready` deltaP `11.4033` edge `0.0117` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6125` n `101` status `ready` deltaP `14.598` edge `0.0139` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4882` n `46` status `ready` deltaP `0.9113` edge `0.0869` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
