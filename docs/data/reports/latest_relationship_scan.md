# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T09:52:26.925639+00:00`
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

- `risk_on_high->unknown_24h` score `435.6701` n `93` status `ready` deltaP `26.7361` edge `36.1276` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `435.6701` n `93` status `ready` deltaP `26.7361` edge `36.1276` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.1716` n `241` status `ready` deltaP `-2.5275` edge `2.1036` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `22.0007` n `93` status `ready` deltaP `37.1976` edge `1.6371` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.0007` n `93` status `ready` deltaP `37.1976` edge `1.6371` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.003` n `93` status `ready` deltaP `31.5972` edge `1.0396` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.003` n `93` status `ready` deltaP `31.5972` edge `1.0396` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.224` n `187` status `ready` deltaP `25.1801` edge `0.6583` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.2997` n `187` status `ready` deltaP `21.7014` edge `0.3803` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.591` n `117` status `ready` deltaP `30.1777` edge `0.3019` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.591` n `117` status `ready` deltaP `30.1777` edge `0.3019` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.1297` n `93` status `ready` deltaP `21.7014` edge `0.2828` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.1297` n `93` status `ready` deltaP `21.7014` edge `0.2828` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3845` n `117` status `ready` deltaP `24.4567` edge `0.2882` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3845` n `117` status `ready` deltaP `24.4567` edge `0.2882` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.5449` n `93` status `ready` deltaP `21.6006` edge `0.0723` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.5449` n `93` status `ready` deltaP `21.6006` edge `0.0723` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.3687` n `187` status `ready` deltaP `19.4788` edge `0.089` maxDD `-0.0505`
- `risk_on_high->metal_24h` score `0.9625` n `93` status `ready` deltaP `17.1875` edge `0.1244` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.9625` n `93` status `ready` deltaP `17.1875` edge `0.1244` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
