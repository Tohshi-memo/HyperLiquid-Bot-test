# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T05:22:24.881299+00:00`
- Price records: `672`
- Market context records: `3454`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_major_24h` score `56.5833` n `32` status `ready` deltaP `58.5069` edge `4.3295` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.5833` n `32` status `ready` deltaP `58.5069` edge `4.3295` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `56.2628` n `32` status `ready` deltaP `59.8958` edge `4.3044` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.2628` n `32` status `ready` deltaP `59.8958` edge `4.3044` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.9993` n `32` status `ready` deltaP `56.0764` edge `3.3761` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.9993` n `32` status `ready` deltaP `56.0764` edge `3.3761` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9387` n `32` status `ready` deltaP `51.3889` edge `1.6523` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9387` n `32` status `ready` deltaP `51.3889` edge `1.6523` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.3559` n `155` status `ready` deltaP `20.4402` edge `2.5268` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.3877` n `155` status `ready` deltaP `24.2125` edge `2.394` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.4118` n `155` status `ready` deltaP `32.8506` edge `2.0399` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `15.6443` n `32` status `ready` deltaP `29.2683` edge `1.2208` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.6443` n `32` status `ready` deltaP `29.2683` edge `1.2208` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.8066` n `32` status `ready` deltaP `28.9931` edge `0.9834` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.8066` n `32` status `ready` deltaP `28.9931` edge `0.9834` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.5653` n `155` status `ready` deltaP `35.905` edge `1.0294` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.5167` n `32` status `ready` deltaP `9.5274` edge `0.7473` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5167` n `32` status `ready` deltaP `9.5274` edge `0.7473` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.6279` n `32` status `ready` deltaP `19.436` edge `0.5772` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.6279` n `32` status `ready` deltaP `19.436` edge `0.5772` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
