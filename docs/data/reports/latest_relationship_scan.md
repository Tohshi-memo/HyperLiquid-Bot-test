# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T13:52:30.184375+00:00`
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

- `risk_on_high->crypto_alt_24h` score `18.3318` n `91` status `ready` deltaP `35.8249` edge `1.3118` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.3318` n `91` status `ready` deltaP `35.8249` edge `1.3118` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `13.7431` n `201` status `ready` deltaP `27.3891` edge `1.0454` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.6465` n `91` status `ready` deltaP `41.641` edge `0.4801` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6465` n `91` status `ready` deltaP `41.641` edge `0.4801` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.1703` n `91` status `ready` deltaP `31.4393` edge `0.4738` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.1703` n `91` status `ready` deltaP `31.4393` edge `0.4738` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.662` n `91` status `ready` deltaP `24.6738` edge `1.0964` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.662` n `91` status `ready` deltaP `24.6738` edge `1.0964` maxDD `-24.5429`
- `market_context_high->equity_24h` score `4.1327` n `201` status `ready` deltaP `20.8333` edge `0.2055` maxDD `0.0`
- `risk_on_high->index_24h` score `3.6047` n `91` status `ready` deltaP `36.6339` edge `0.0604` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.6047` n `91` status `ready` deltaP `36.6339` edge `0.0604` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.733` n `201` status `ready` deltaP `30.9754` edge `0.0606` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.643` n `91` status `ready` deltaP `28.4676` edge `0.0398` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.643` n `91` status `ready` deltaP `28.4676` edge `0.0398` maxDD `-0.0802`
- `risk_on_high->equity_24h` score `2.5271` n `91` status `ready` deltaP `20.8333` edge `0.0717` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.5271` n `91` status `ready` deltaP `20.8333` edge `0.0717` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.5326` n `201` status `ready` deltaP `16.7159` edge `0.0302` maxDD `-0.1139`
- `market_context_high->equity_4h` score `1.5166` n `201` status `ready` deltaP `21.6282` edge `0.068` maxDD `-2.8642`
- `risk_on_high->commodity_24h` score `1.5164` n `91` status `ready` deltaP `16.3824` edge `0.0265` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
