# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T22:37:29.430774+00:00`
- Price records: `672`
- Market context records: `3526`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13196`

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

- `risk_on_high->crypto_major_24h` score `53.5644` n `32` status `ready` deltaP `57.8802` edge `4.0821` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.5644` n `32` status `ready` deltaP `57.8802` edge `4.0821` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `49.3226` n `32` status `ready` deltaP `57.5336` edge `3.7418` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `49.3226` n `32` status `ready` deltaP `57.5336` edge `3.7418` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.6142` n `32` status `ready` deltaP `54.5927` edge `3.3539` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.6142` n `32` status `ready` deltaP `54.5927` edge `3.3539` maxDD `0.0`
- `risk_on_high->index_24h` score `25.038` n `32` status `ready` deltaP `52.8596` edge `1.7341` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.038` n `32` status `ready` deltaP `52.8596` edge `1.7341` maxDD `0.0`
- `market_context_high->equity_24h` score `18.9703` n `156` status `ready` deltaP `31.5158` edge `2.012` maxDD `-40.9667`
- `market_context_high->crypto_major_24h` score `18.1303` n `156` status `ready` deltaP `23.1847` edge `2.1294` maxDD `-54.8486`
- `risk_on_high->metal_24h` score `17.9155` n `32` status `ready` deltaP `35.4744` edge `1.2826` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.9155` n `32` status `ready` deltaP `35.4744` edge `1.2826` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `15.2355` n `156` status `ready` deltaP `17.7099` edge `1.9558` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `14.9806` n `32` status `ready` deltaP `28.2012` edge `1.1726` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.9806` n `32` status `ready` deltaP `28.2012` edge `1.1726` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.6533` n `156` status `ready` deltaP `37.475` edge `1.1096` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.3357` n `32` status `ready` deltaP `9.6799` edge `0.7312` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3357` n `32` status `ready` deltaP `9.6799` edge `0.7312` maxDD `-11.7537`
- `market_context_high->metal_24h` score `7.1366` n `156` status `ready` deltaP `29.5449` edge `1.172` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.9039` n `32` status `ready` deltaP `16.3872` edge `0.5047` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
