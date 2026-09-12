# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T13:07:28.734253+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12058`

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

- `market_context_high->unknown_24h` score `4237.2069` n `103` status `ready` deltaP `13.5097` edge `353.0157` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `1350.3925` n `55` status `ready` deltaP `15.4514` edge `112.4297` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `1350.3925` n `55` status `ready` deltaP `15.4514` edge `112.4297` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.3054` n `82` status `ready` deltaP `-4.6517` edge `32.0153` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.5049` n `59` status `ready` deltaP `54.6786` edge `1.7676` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `18.5506` n `55` status `ready` deltaP `39.5202` edge `1.3054` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.5506` n `55` status `ready` deltaP `39.5202` edge `1.3054` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.5798` n `59` status `ready` deltaP `29.967` edge `1.314` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `16.0221` n `103` status `ready` deltaP `33.0771` edge `1.1974` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.368` n `59` status `ready` deltaP `34.4574` edge `0.8108` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.9006` n `55` status `ready` deltaP `37.8472` edge `0.4894` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.9006` n `55` status `ready` deltaP `37.8472` edge `0.4894` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.7411` n `55` status `ready` deltaP `42.8687` edge `0.4798` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.7411` n `55` status `ready` deltaP `42.8687` edge `0.4798` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.6498` n `103` status `ready` deltaP `37.8472` edge `0.4685` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.4174` n `59` status `ready` deltaP `53.9931` edge `0.3415` maxDD `0.0`
- `news_risk_high->index_24h` score `7.922` n `59` status `ready` deltaP `51.6449` edge `0.3252` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8745` n `55` status `ready` deltaP `49.5802` edge `0.0799` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8745` n `55` status `ready` deltaP `49.5802` edge `0.0799` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.2153` n `55` status `ready` deltaP `37.5444` edge `0.1103` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
