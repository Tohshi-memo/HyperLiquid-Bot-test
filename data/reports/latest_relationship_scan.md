# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T13:22:30.118304+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11908`

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

- `risk_on_high->crypto_alt_24h` score `18.0556` n `91` status `ready` deltaP `35.4777` edge `1.2911` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.0556` n `91` status `ready` deltaP `35.4777` edge `1.2911` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.4669` n `201` status `ready` deltaP `27.0419` edge `1.0247` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.5057` n `91` status `ready` deltaP `41.3361` edge `0.4704` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5057` n `91` status `ready` deltaP `41.3361` edge `0.4704` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.984` n `91` status `ready` deltaP `31.1344` edge `0.4603` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.984` n `91` status `ready` deltaP `31.1344` edge `0.4603` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.4973` n `91` status `ready` deltaP `24.3266` edge `1.0776` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.4973` n `91` status `ready` deltaP `24.3266` edge `1.0776` maxDD `-24.5429`
- `market_context_high->equity_24h` score `3.9201` n `201` status `ready` deltaP `20.4861` edge `0.1901` maxDD `0.0`
- `risk_on_high->index_24h` score `3.5482` n `91` status `ready` deltaP `36.2866` edge `0.058` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.5482` n `91` status `ready` deltaP `36.2866` edge `0.058` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6764` n `201` status `ready` deltaP `30.6281` edge `0.0582` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.5346` n `91` status `ready` deltaP `28.1627` edge `0.0328` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.5346` n `91` status `ready` deltaP `28.1627` edge `0.0328` maxDD `-0.0802`
- `risk_on_high->equity_24h` score `2.3145` n `91` status `ready` deltaP `20.4861` edge `0.0563` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.3145` n `91` status `ready` deltaP `20.4861` edge `0.0563` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.6012` n `201` status `ready` deltaP `17.0631` edge `0.0336` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.585` n `91` status `ready` deltaP `16.7296` edge `0.0299` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.585` n `91` status `ready` deltaP `16.7296` edge `0.0299` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
