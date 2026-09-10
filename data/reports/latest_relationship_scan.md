# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T11:52:28.421028+00:00`
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

- `risk_on_high->crypto_alt_24h` score `17.1827` n `91` status `ready` deltaP `34.4361` edge `1.2253` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.1827` n `91` status `ready` deltaP `34.4361` edge `1.2253` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `12.594` n `201` status `ready` deltaP `26.0003` edge `0.9589` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.1109` n `91` status `ready` deltaP `40.4215` edge `0.4436` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1109` n `91` status `ready` deltaP `40.4215` edge `0.4436` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.4332` n `91` status `ready` deltaP `30.2198` edge `0.4205` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.4332` n `91` status `ready` deltaP `30.2198` edge `0.4205` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.9323` n `91` status `ready` deltaP `23.2849` edge `1.0121` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.9323` n `91` status `ready` deltaP `23.2849` edge `1.0121` maxDD `-24.5429`
- `market_context_high->equity_24h` score `3.4156` n `201` status `ready` deltaP `19.4444` edge `0.155` maxDD `0.0`
- `risk_on_high->index_24h` score `3.4024` n `91` status `ready` deltaP `35.245` edge `0.0528` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.4024` n `91` status `ready` deltaP `35.245` edge `0.0528` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.5307` n `201` status `ready` deltaP `29.5865` edge `0.053` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.2106` n `91` status `ready` deltaP `27.2481` edge `0.0119` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.2106` n `91` status `ready` deltaP `27.2481` edge `0.0119` maxDD `-0.0802`
- `risk_on_high->equity_24h` score `1.81` n `91` status `ready` deltaP `19.4444` edge `0.0212` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.81` n `91` status `ready` deltaP `19.4444` edge `0.0212` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.7913` n `201` status `ready` deltaP `18.1048` edge `0.0425` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.7751` n `91` status `ready` deltaP `17.7713` edge `0.0388` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.7751` n `91` status `ready` deltaP `17.7713` edge `0.0388` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
