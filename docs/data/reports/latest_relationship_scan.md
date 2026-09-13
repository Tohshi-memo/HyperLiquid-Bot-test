# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T15:52:32.642614+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13438`

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

- `market_context_high->unknown_24h` score `17834.8025` n `56` status `ready` deltaP `8.596` edge `1486.1964` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `9191.7181` n `35` status `ready` deltaP `13.596` edge `765.8916` maxDD `-0.1252`
- `risk_on_and_context->unknown_24h` score `9191.7181` n `35` status `ready` deltaP `13.596` edge `765.8916` maxDD `-0.1252`
- `news_risk_high->unknown_1h` score `423.6147` n `82` status `ready` deltaP `-4.8014` edge `35.3754` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.4753` n `82` status `ready` deltaP `35.3406` edge `1.3528` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.376` n `82` status `ready` deltaP `38.0236` edge `1.4249` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.7318` n `82` status `ready` deltaP `25.3743` edge `0.7365` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.8985` n `82` status `ready` deltaP `49.1463` edge `0.2649` maxDD `-0.0797`
- `risk_on_high->crypto_alt_24h` score `4.7878` n `35` status `ready` deltaP `18.1281` edge `0.5653` maxDD `-4.1195`
- `risk_on_and_context->crypto_alt_24h` score `4.7878` n `35` status `ready` deltaP `18.1281` edge `0.5653` maxDD `-4.1195`
- `news_risk_high->metal_24h` score `4.575` n `82` status `ready` deltaP `24.4155` edge `0.2639` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.2206` n `35` status `ready` deltaP `39.8276` edge `0.0862` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.2206` n `35` status `ready` deltaP `39.8276` edge `0.0862` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2158` n `56` status `ready` deltaP `39.8276` edge `0.0858` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `4.1205` n `56` status `ready` deltaP `13.1281` edge `0.5581` maxDD `-6.7217`
- `market_context_high->metal_24h` score `1.973` n `56` status `ready` deltaP `15.4433` edge `0.1288` maxDD `-1.0538`
- `risk_on_high->index_24h` score `1.2567` n `35` status `ready` deltaP `33.5714` edge `0.0206` maxDD `-2.9964`
- `risk_on_and_context->index_24h` score `1.2567` n `35` status `ready` deltaP `33.5714` edge `0.0206` maxDD `-2.9964`
- `market_context_high->index_24h` score `0.9171` n `56` status `ready` deltaP `32.8571` edge `0.0274` maxDD `-4.3097`
- `risk_on_high->metal_24h` score `0.6068` n `35` status `ready` deltaP `4.7291` edge `0.1033` maxDD `-0.8956`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
