# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T05:52:29.680740+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11409`

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

- `market_context_high->unknown_24h` score `1415.0906` n `132` status `ready` deltaP `13.9362` edge `117.8365` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.3293` n `82` status `ready` deltaP `-3.6038` edge `32.0103` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `23.9534` n `59` status `ready` deltaP `54.505` edge `1.7228` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `23.0127` n `80` status `ready` deltaP `42.3611` edge `1.6583` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.0127` n `80` status `ready` deltaP `42.3611` edge `1.6583` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.4775` n `132` status `ready` deltaP `36.4899` edge `1.4626` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.4646` n `59` status `ready` deltaP `29.967` edge `1.3044` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.0898` n `59` status `ready` deltaP `33.5894` edge `0.7934` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0279` n `80` status `ready` deltaP `36.9792` edge `0.5058` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0279` n `80` status `ready` deltaP `36.9792` edge `0.5058` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7063` n `132` status `ready` deltaP `36.9792` edge `0.479` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.1597` n `59` status `ready` deltaP `51.0417` edge `0.3397` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.1273` n `80` status `ready` deltaP `43.4756` edge `0.4246` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1273` n `80` status `ready` deltaP `43.4756` edge `0.4246` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9321` n `59` status `ready` deltaP `51.4713` edge `0.3272` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `6.0397` n `80` status `ready` deltaP `29.7866` edge `0.3906` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.0397` n `80` status `ready` deltaP `29.7866` edge `0.3906` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `5.5831` n `80` status `ready` deltaP `20.0347` edge `0.989` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `5.5831` n `80` status `ready` deltaP `20.0347` edge `0.989` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.1481` n `80` status `ready` deltaP `51.1111` edge `0.0925` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
