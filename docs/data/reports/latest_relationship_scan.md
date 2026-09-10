# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T16:52:31.160416+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11967`

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

- `risk_on_high->crypto_alt_24h` score `19.2884` n `91` status `ready` deltaP `36.1722` edge `1.3892` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `19.2884` n `91` status `ready` deltaP `36.1722` edge `1.3892` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `14.6997` n `201` status `ready` deltaP `27.7364` edge `1.1228` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.2018` n `91` status `ready` deltaP `43.3178` edge `0.5152` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.2018` n `91` status `ready` deltaP `43.3178` edge `0.5152` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.8423` n `91` status `ready` deltaP `33.2686` edge `0.5176` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8423` n `91` status `ready` deltaP `33.2686` edge `0.5176` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.0677` n `91` status `ready` deltaP `25.021` edge `1.1461` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.0677` n `91` status `ready` deltaP `25.021` edge `1.1461` maxDD `-24.5429`
- `market_context_high->equity_24h` score `5.1897` n `201` status `ready` deltaP `22.9167` edge `0.2797` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9082` n `91` status `ready` deltaP `38.7172` edge `0.0718` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.9082` n `91` status `ready` deltaP `38.7172` edge `0.0718` maxDD `-0.0051`
- `risk_on_high->equity_24h` score `3.5961` n `91` status `ready` deltaP `22.9167` edge `0.1469` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.5961` n `91` status `ready` deltaP `22.9167` edge `0.1469` maxDD `0.0`
- `market_context_high->index_24h` score `3.0365` n `201` status `ready` deltaP `33.0587` edge `0.072` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.9968` n `91` status `ready` deltaP `30.1444` edge `0.0581` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.9968` n `91` status `ready` deltaP `30.1444` edge `0.0581` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.8711` n `201` status `ready` deltaP `23.305` edge `0.0861` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.5441` n `91` status `ready` deltaP `6.197` edge `0.1226` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.5441` n `91` status `ready` deltaP `6.197` edge `0.1226` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
