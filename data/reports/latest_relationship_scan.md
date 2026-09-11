# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T23:22:32.544462+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11275`

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

- `news_risk_high->unknown_1h` score `421.8211` n `79` status `ready` deltaP `-3.1608` edge `35.215` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.7195` n `91` status `ready` deltaP `43.1166` edge `1.7955` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.7195` n `91` status `ready` deltaP `43.1166` edge `1.7955` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `22.1765` n `38` status `ready` deltaP `50.7584` edge `1.5997` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `21.81` n `151` status `ready` deltaP `38.0151` edge `1.6468` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `12.714` n `38` status `ready` deltaP `19.6637` edge `0.9772` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `10.2803` n `38` status `ready` deltaP `31.716` edge `0.6551` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.3855` n `91` status `ready` deltaP `36.9792` edge `0.5356` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3855` n `91` status `ready` deltaP `36.9792` edge `0.5356` maxDD `0.0`
- `market_context_high->equity_24h` score `9.0963` n `151` status `ready` deltaP `36.9792` edge `0.5115` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.79` n `91` status `ready` deltaP `43.1654` edge `0.4819` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.79` n `91` status `ready` deltaP `43.1654` edge `0.4819` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.0085` n `38` status `ready` deltaP `51.0417` edge `0.3271` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `7.7619` n `91` status `ready` deltaP `25.021` edge `1.2351` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.7619` n `91` status `ready` deltaP `25.021` edge `1.2351` maxDD `-24.5429`
- `news_risk_high->index_24h` score `7.7019` n `38` status `ready` deltaP `49.5979` edge `0.3205` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.7197` n `91` status `ready` deltaP `31.8966` edge `0.4332` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.7197` n `91` status `ready` deltaP `31.8966` edge `0.4332` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.356` n `91` status `ready` deltaP `51.5644` edge `0.1068` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.356` n `91` status `ready` deltaP `51.5644` edge `0.1068` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
