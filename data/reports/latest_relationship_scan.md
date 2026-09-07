# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T11:37:24.916482+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10429`

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

- `risk_on_high->unknown_24h` score `408.4921` n `93` status `ready` deltaP `26.0417` edge `33.8674` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `408.4921` n `93` status `ready` deltaP `26.0417` edge `33.8674` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.1812` n `241` status `ready` deltaP `-2.2281` edge `2.1024` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `22.1763` n `93` status `ready` deltaP `37.892` edge `1.6471` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.1763` n `93` status `ready` deltaP `37.892` edge `1.6471` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1172` n `93` status `ready` deltaP `31.9444` edge `1.0468` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1172` n `93` status `ready` deltaP `31.9444` edge `1.0468` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.9345` n `190` status `ready` deltaP `24.576` edge `0.6382` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.9589` n `190` status `ready` deltaP `20.4861` edge `0.36` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.4363` n `117` status `ready` deltaP `29.2631` edge `0.2951` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4363` n `117` status `ready` deltaP `29.2631` edge `0.2951` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.9077` n `93` status `ready` deltaP `20.4861` edge `0.2724` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.9077` n `93` status `ready` deltaP `20.4861` edge `0.2724` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3713` n `117` status `ready` deltaP `24.4567` edge `0.2871` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3713` n `117` status `ready` deltaP `24.4567` edge `0.2871` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4521` n `93` status `ready` deltaP `20.9061` edge `0.0692` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4521` n `93` status `ready` deltaP `20.9061` edge `0.0692` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.1239` n `190` status `ready` deltaP `17.2898` edge `0.0835` maxDD `-0.075`
- `risk_on_high->crypto_alt_1h` score `0.9309` n `117` status `ready` deltaP `4.3964` edge `0.0835` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9309` n `117` status `ready` deltaP `4.3964` edge `0.0835` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
