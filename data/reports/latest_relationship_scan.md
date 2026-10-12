# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T02:22:25.401837+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9558`

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

- `market_context_high->unknown_24h` score `811.1278` n `49` status `ready` deltaP `-17.9776` edge `67.7502` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `36.7111` n `114` status `ready` deltaP `-8.098` edge `3.1838` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.471` n `49` status `ready` deltaP `31.8063` edge `0.6201` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.9961` n `49` status `ready` deltaP `50.5634` edge `0.1669` maxDD `-0.012`
- `market_context_high->crypto_major_24h` score `5.4197` n `49` status `ready` deltaP `-6.0197` edge `0.8066` maxDD `-17.8526`
- `risk_on_high->crypto_major_4h` score `5.1725` n `35` status `ready` deltaP `29.0113` edge `0.3229` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.1725` n `35` status `ready` deltaP `29.0113` edge `0.3229` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.0945` n `35` status `ready` deltaP `23.027` edge `0.3158` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0945` n `35` status `ready` deltaP `23.027` edge `0.3158` maxDD `-1.9151`
- `risk_on_high->metal_4h` score `3.1544` n `35` status `ready` deltaP `28.7805` edge `0.0942` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.1544` n `35` status `ready` deltaP `28.7805` edge `0.0942` maxDD `-0.1896`
- `risk_on_high->metal_1h` score `1.4336` n `47` status `ready` deltaP `17.6679` edge `0.0256` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.4336` n `47` status `ready` deltaP `17.6679` edge `0.0256` maxDD `-0.2466`
- `risk_on_high->crypto_major_1h` score `1.0912` n `47` status `ready` deltaP `11.1033` edge `0.0822` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.0912` n `47` status `ready` deltaP `11.1033` edge `0.0822` maxDD `-3.2233`
- `market_context_high->fx_24h` score `1.0884` n `49` status `ready` deltaP `16.656` edge `0.0211` maxDD `-0.3151`
- `risk_on_high->crypto_alt_1h` score `0.6168` n `47` status `ready` deltaP `7.8099` edge `0.0867` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.6168` n `47` status `ready` deltaP `7.8099` edge `0.0867` maxDD `-2.4421`
- `risk_on_high->equity_4h` score `0.5763` n `35` status `ready` deltaP `4.6646` edge `0.0809` maxDD `-1.0489`
- `risk_on_and_context->equity_4h` score `0.5763` n `35` status `ready` deltaP `4.6646` edge `0.0809` maxDD `-1.0489`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
