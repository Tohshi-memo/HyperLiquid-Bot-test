# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T20:07:29.750163+00:00`
- Price records: `672`
- Market context records: `3515`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13184`

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

- `risk_on_high->crypto_major_24h` score `53.8164` n `32` status `ready` deltaP `57.8802` edge `4.1031` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.8164` n `32` status `ready` deltaP `57.8802` edge `4.1031` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `50.0066` n `32` status `ready` deltaP `57.5336` edge `3.7988` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `50.0066` n `32` status `ready` deltaP `57.5336` edge `3.7988` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.2806` n `32` status `ready` deltaP `54.5927` edge `3.3261` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.2806` n `32` status `ready` deltaP `54.5927` edge `3.3261` maxDD `0.0`
- `risk_on_high->index_24h` score `24.5454` n `32` status `ready` deltaP `51.4731` edge `1.7023` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.5454` n `32` status `ready` deltaP `51.4731` edge `1.7023` maxDD `0.0`
- `market_context_high->equity_24h` score `18.6367` n `156` status `ready` deltaP `31.5158` edge `1.9842` maxDD `-40.9667`
- `market_context_high->crypto_major_24h` score `18.3823` n `156` status `ready` deltaP `23.1847` edge `2.1504` maxDD `-54.8486`
- `risk_on_high->metal_24h` score `17.0245` n `32` status `ready` deltaP `33.7413` edge `1.2199` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.0245` n `32` status `ready` deltaP `33.7413` edge `1.2199` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `15.9195` n `156` status `ready` deltaP `17.7099` edge `2.0128` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `15.0717` n `32` status `ready` deltaP `28.1107` edge `1.1808` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.0717` n `32` status `ready` deltaP `28.1107` edge `1.1808` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1608` n `156` status `ready` deltaP `36.0885` edge `1.0778` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.4139` n `32` status `ready` deltaP `9.4416` edge `0.7393` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4139` n `32` status `ready` deltaP `9.4416` edge `0.7393` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.5574` n `156` status `ready` deltaP `27.8118` edge `1.1093` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.8133` n `32` status `ready` deltaP `16.3099` edge `0.4936` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
