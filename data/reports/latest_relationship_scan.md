# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T10:07:28.864134+00:00`
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

- `risk_on_high->unknown_24h` score `430.831` n `93` status `ready` deltaP `26.5625` edge `35.7255` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `430.831` n `93` status `ready` deltaP `26.5625` edge `35.7255` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.1488` n `241` status `ready` deltaP `-2.6772` edge `2.1027` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `22.0338` n `93` status `ready` deltaP `37.3712` edge `1.6387` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.0338` n `93` status `ready` deltaP `37.3712` edge `1.6387` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.0078` n `93` status `ready` deltaP `31.5972` edge `1.04` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.0078` n `93` status `ready` deltaP `31.5972` edge `1.04` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.2288` n `187` status `ready` deltaP `25.1801` edge `0.6587` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.269` n `187` status `ready` deltaP `21.5278` edge `0.3789` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.5716` n `117` status `ready` deltaP `30.0253` edge `0.3013` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.5716` n `117` status `ready` deltaP `30.0253` edge `0.3013` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.099` n `93` status `ready` deltaP `21.5278` edge `0.2814` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.099` n `93` status `ready` deltaP `21.5278` edge `0.2814` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3857` n `117` status `ready` deltaP `24.4567` edge `0.2883` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3857` n `117` status `ready` deltaP `24.4567` edge `0.2883` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.525` n `93` status `ready` deltaP `21.427` edge `0.0718` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.525` n `93` status `ready` deltaP `21.427` edge `0.0718` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.3488` n `187` status `ready` deltaP `19.3052` edge `0.0885` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.9597` n `117` status `ready` deltaP `4.5461` edge `0.0849` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9597` n `117` status `ready` deltaP `4.5461` edge `0.0849` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
