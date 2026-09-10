# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T12:07:33.731259+00:00`
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

- `risk_on_high->crypto_alt_24h` score `17.3466` n `91` status `ready` deltaP `34.6097` edge `1.2378` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.3466` n `91` status `ready` deltaP `34.6097` edge `1.2378` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `12.7579` n `201` status `ready` deltaP `26.1739` edge `0.9714` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `8.1675` n `91` status `ready` deltaP `40.5739` edge `0.4473` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1675` n `91` status `ready` deltaP `40.5739` edge `0.4473` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `6.5162` n `91` status `ready` deltaP `30.3722` edge `0.4264` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.5162` n `91` status `ready` deltaP `30.3722` edge `0.4264` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `6.0388` n `91` status `ready` deltaP `23.4585` edge `1.0246` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.0388` n `91` status `ready` deltaP `23.4585` edge `1.0246` maxDD `-24.5429`
- `market_context_high->equity_24h` score `3.5026` n `201` status `ready` deltaP `19.6181` edge `0.1611` maxDD `0.0`
- `risk_on_high->index_24h` score `3.4271` n `91` status `ready` deltaP `35.4186` edge `0.0537` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `3.4271` n `91` status `ready` deltaP `35.4186` edge `0.0537` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.5554` n `201` status `ready` deltaP `29.7601` edge `0.0539` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.2588` n `91` status `ready` deltaP `27.4005` edge `0.0149` maxDD `-0.0802`
- `risk_on_and_context->equity_4h` score `2.2588` n `91` status `ready` deltaP `27.4005` edge `0.0149` maxDD `-0.0802`
- `risk_on_high->equity_24h` score `1.897` n `91` status `ready` deltaP `19.6181` edge `0.0273` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.897` n `91` status `ready` deltaP `19.6181` edge `0.0273` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.757` n `201` status `ready` deltaP `17.9312` edge `0.0408` maxDD `-0.1139`
- `risk_on_high->commodity_24h` score `1.7409` n `91` status `ready` deltaP `17.5977` edge `0.0371` maxDD `-0.0811`
- `risk_on_and_context->commodity_24h` score `1.7409` n `91` status `ready` deltaP `17.5977` edge `0.0371` maxDD `-0.0811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
