# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T16:22:40.308128+00:00`
- Price records: `672`
- Market context records: `3399`
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

- `risk_on_high->crypto_major_24h` score `55.6802` n `32` status `ready` deltaP `58.3333` edge `4.2554` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.6802` n `32` status `ready` deltaP `58.3333` edge `4.2554` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.5472` n `32` status `ready` deltaP `56.0764` edge `4.1869` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.5472` n `32` status `ready` deltaP `56.0764` edge `4.1869` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.5729` n `32` status `ready` deltaP `56.0764` edge `3.4239` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.5729` n `32` status `ready` deltaP `56.0764` edge `3.4239` maxDD `0.0`
- `risk_on_high->index_24h` score `23.4263` n `32` status `ready` deltaP `51.3889` edge `1.6096` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.4263` n `32` status `ready` deltaP `51.3889` edge `1.6096` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `20.8923` n `155` status `ready` deltaP `17.2659` edge `2.4244` maxDD `-56.8787`
- `market_context_high->crypto_major_24h` score `19.6383` n `155` status `ready` deltaP `24.0389` edge `2.3192` maxDD `-60.435`
- `market_context_high->equity_24h` score `19.3938` n `155` status `ready` deltaP `32.8506` edge `2.0992` maxDD `-45.1644`
- `risk_on_high->crypto_major_4h` score `15.2578` n `32` status `ready` deltaP `28.2012` edge `1.1957` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.2578` n `32` status `ready` deltaP `28.2012` edge `1.1957` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.6086` n `32` status `ready` deltaP `28.9931` edge `0.9669` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.6086` n `32` status `ready` deltaP `28.9931` edge `0.9669` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.1049` n `155` status `ready` deltaP `35.905` edge `1.0047` maxDD `-15.4929`
- `risk_on_high->crypto_alt_4h` score `6.9752` n `32` status `ready` deltaP `8.3079` edge `0.7103` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.9752` n `32` status `ready` deltaP `8.3079` edge `0.7103` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.0361` n `155` status `ready` deltaP `23.4689` edge `0.8694` maxDD `-29.6733`
- `risk_on_high->equity_4h` score `4.0135` n `32` status `ready` deltaP `15.9299` edge `0.5218` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
