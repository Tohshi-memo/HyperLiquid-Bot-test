# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T14:37:33.229660+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10202`

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

- `risk_on_high->unknown_24h` score `377.0713` n `93` status `ready` deltaP `24.8264` edge `31.2571` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `377.0713` n `93` status `ready` deltaP `24.8264` edge `31.2571` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.5197` n `93` status `ready` deltaP `39.4545` edge `1.6653` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.5197` n `93` status `ready` deltaP `39.4545` edge `1.6653` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.2354` n `93` status `ready` deltaP `32.1181` edge `1.0555` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.2354` n `93` status `ready` deltaP `32.1181` edge `1.0555` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.3966` n `202` status `ready` deltaP `24.6924` edge `0.5926` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.3145` n `117` status `ready` deltaP `28.8058` edge `0.288` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3145` n `117` status `ready` deltaP `28.8058` edge `0.288` maxDD `-1.9733`
- `market_context_high->equity_24h` score `5.0842` n `202` status `ready` deltaP `18.4028` edge `0.301` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.5157` n `117` status `ready` deltaP `24.7616` edge `0.2971` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.5157` n `117` status `ready` deltaP `24.7616` edge `0.2971` maxDD `-3.8693`
- `risk_on_high->equity_24h` score `4.4182` n `93` status `ready` deltaP `18.4028` edge `0.2455` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.4182` n `93` status `ready` deltaP `18.4028` edge `0.2455` maxDD `0.0`
- `risk_on_high->index_24h` score `2.2865` n `93` status `ready` deltaP `19.6909` edge `0.0635` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.2865` n `93` status `ready` deltaP `19.6909` edge `0.0635` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.5038` n `202` status `ready` deltaP `14.0058` edge `0.0713` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.8685` n `117` status `ready` deltaP `4.097` edge `0.0803` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8685` n `117` status `ready` deltaP `4.097` edge `0.0803` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.8159` n `93` status `ready` deltaP `17.1875` edge `0.1056` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
