# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T16:37:24.811528+00:00`
- Price records: `672`
- Market context records: `3400`
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

- `risk_on_high->crypto_major_24h` score `55.6862` n `32` status `ready` deltaP `58.3333` edge `4.2559` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.6862` n `32` status `ready` deltaP `58.3333` edge `4.2559` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.606` n `32` status `ready` deltaP `56.0764` edge `4.1918` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.606` n `32` status `ready` deltaP `56.0764` edge `4.1918` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.6233` n `32` status `ready` deltaP `56.0764` edge `3.4281` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.6233` n `32` status `ready` deltaP `56.0764` edge `3.4281` maxDD `0.0`
- `risk_on_high->index_24h` score `23.4743` n `32` status `ready` deltaP `51.3889` edge `1.6136` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.4743` n `32` status `ready` deltaP `51.3889` edge `1.6136` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `20.9511` n `155` status `ready` deltaP `17.2659` edge `2.4293` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `19.6443` n `155` status `ready` deltaP `24.0389` edge `2.3197` maxDD `-60.435`
- `market_context_high->equity_24h` score `19.4442` n `155` status `ready` deltaP `32.8506` edge `2.1034` maxDD `-45.1644`
- `risk_on_high->crypto_major_4h` score `15.271` n `32` status `ready` deltaP `28.2012` edge `1.1968` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.271` n `32` status `ready` deltaP `28.2012` edge `1.1968` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.6026` n `32` status `ready` deltaP `28.9931` edge `0.9664` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.6026` n `32` status `ready` deltaP `28.9931` edge `0.9664` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.1529` n `155` status `ready` deltaP `35.905` edge `1.0087` maxDD `-15.4929`
- `risk_on_high->crypto_alt_4h` score `6.9884` n `32` status `ready` deltaP `8.3079` edge `0.7114` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.9884` n `32` status `ready` deltaP `8.3079` edge `0.7114` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.0854` n `32` status `ready` deltaP `16.0823` edge `0.53` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.0854` n `32` status `ready` deltaP `16.0823` edge `0.53` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
