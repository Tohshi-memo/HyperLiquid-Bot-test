# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T15:52:43.469333+00:00`
- Price records: `672`
- Market context records: `3397`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13074`

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

- `risk_on_high->crypto_major_24h` score `55.625` n `32` status `ready` deltaP `58.3333` edge `4.2508` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.625` n `32` status `ready` deltaP `58.3333` edge `4.2508` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.3545` n `32` status `ready` deltaP `55.9028` edge `4.172` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.3545` n `32` status `ready` deltaP `55.9028` edge `4.172` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.4709` n `32` status `ready` deltaP `56.0764` edge `3.4154` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.4709` n `32` status `ready` deltaP `56.0764` edge `3.4154` maxDD `0.0`
- `risk_on_high->index_24h` score `23.3327` n `32` status `ready` deltaP `51.3889` edge `1.6018` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.3327` n `32` status `ready` deltaP `51.3889` edge `1.6018` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.0669` n `154` status `ready` deltaP `17.4694` edge `2.4376` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `20.0236` n `154` status `ready` deltaP `24.4453` edge `2.3486` maxDD `-60.435`
- `market_context_high->equity_24h` score `19.7265` n `154` status `ready` deltaP `33.3491` edge `2.1236` maxDD `-45.1644`
- `risk_on_high->crypto_major_4h` score `15.1966` n `32` status `ready` deltaP `28.2012` edge `1.1906` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1966` n `32` status `ready` deltaP `28.2012` edge `1.1906` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.6254` n `32` status `ready` deltaP `28.9931` edge `0.9683` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.6254` n `32` status `ready` deltaP `28.9931` edge `0.9683` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.2688` n `154` status `ready` deltaP `36.4538` edge `1.0147` maxDD `-15.4929`
- `risk_on_high->crypto_alt_4h` score `6.8982` n `32` status `ready` deltaP `8.1555` edge `0.7049` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.8982` n `32` status `ready` deltaP `8.1555` edge `0.7049` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.1533` n `154` status `ready` deltaP `23.8795` edge `0.8817` maxDD `-29.6733`
- `risk_on_high->equity_4h` score `3.8799` n `32` status `ready` deltaP `15.625` edge `0.5067` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
