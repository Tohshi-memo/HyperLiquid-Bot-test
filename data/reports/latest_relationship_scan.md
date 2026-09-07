# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T10:37:32.804041+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10427`

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

- `risk_on_high->unknown_24h` score `424.4518` n `93` status `ready` deltaP `26.5625` edge `35.1939` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `424.4518` n `93` status `ready` deltaP `26.5625` edge `35.1939` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.1332` n `241` status `ready` deltaP `-2.6772` edge `2.1014` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `22.1048` n `93` status `ready` deltaP `37.7184` edge `1.6423` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.1048` n `93` status `ready` deltaP `37.7184` edge `1.6423` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.0378` n `93` status `ready` deltaP `31.5972` edge `1.0425` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.0378` n `93` status `ready` deltaP `31.5972` edge `1.0425` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.2588` n `187` status `ready` deltaP `25.1801` edge `0.6612` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.2076` n `187` status `ready` deltaP `21.1806` edge `0.3761` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.5462` n `117` status `ready` deltaP `29.8728` edge `0.3002` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5462` n `117` status `ready` deltaP `29.8728` edge `0.3002` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.0376` n `93` status `ready` deltaP `21.1806` edge `0.2786` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.0376` n `93` status `ready` deltaP `21.1806` edge `0.2786` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3845` n `117` status `ready` deltaP `24.4567` edge `0.2882` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3845` n `117` status `ready` deltaP `24.4567` edge `0.2882` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4864` n `93` status `ready` deltaP `21.0798` edge `0.0709` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4864` n `93` status `ready` deltaP `21.0798` edge `0.0709` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.3103` n `187` status `ready` deltaP `18.958` edge `0.0876` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.998` n `117` status `ready` deltaP `4.8455` edge `0.0861` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.998` n `117` status `ready` deltaP `4.8455` edge `0.0861` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
