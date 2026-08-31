# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T06:37:24.172215+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11586`

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

- `risk_on_high->crypto_alt_24h` score `21.7797` n `55` status `ready` deltaP `48.2733` edge `1.5412` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `21.7797` n `55` status `ready` deltaP `48.2733` edge `1.5412` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `10.0114` n `55` status `ready` deltaP `29.5613` edge `0.779` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `10.0114` n `55` status `ready` deltaP `29.5613` edge `0.779` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.2517` n `103` status `ready` deltaP `24.7499` edge `0.5843` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.2517` n `103` status `ready` deltaP `24.7499` edge `0.5843` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.6048` n `155` status `ready` deltaP `21.5804` edge `0.4759` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.3255` n `55` status `ready` deltaP `70.8333` edge `0.0549` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3255` n `55` status `ready` deltaP `70.8333` edge `0.0549` maxDD `0.0`
- `market_context_high->metal_24h` score `5.2396` n `96` status `ready` deltaP `37.1527` edge `0.2498` maxDD `-1.8678`
- `market_context_high->crypto_alt_24h` score `4.4464` n `96` status `ready` deltaP `22.743` edge `0.8374` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.42` n `55` status `ready` deltaP `40.5808` edge `0.145` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.42` n `55` status `ready` deltaP `40.5808` edge `0.145` maxDD `-0.7767`
- `market_context_high->crypto_major_24h` score `4.0721` n `96` status `ready` deltaP `20.6598` edge `0.4507` maxDD `-17.2607`
- `risk_on_high->unknown_1h` score `2.5881` n `107` status `ready` deltaP `7.4137` edge `0.2239` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.5881` n `107` status `ready` deltaP `7.4137` edge `0.2239` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.3655` n `159` status `ready` deltaP `6.7554` edge `0.2151` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.0541` n `96` status `ready` deltaP `37.5` edge `0.031` maxDD `-1.6688`
- `risk_on_high->equity_24h` score `0.8533` n `55` status `ready` deltaP `19.0625` edge `0.0248` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `0.8533` n `55` status `ready` deltaP `19.0625` edge `0.0248` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
