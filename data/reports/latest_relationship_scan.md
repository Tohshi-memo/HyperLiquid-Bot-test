# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T21:07:30.818849+00:00`
- Price records: `672`
- Market context records: `3519`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13194`

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

- `risk_on_high->crypto_major_24h` score `53.7768` n `32` status `ready` deltaP `57.8802` edge `4.0998` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.7768` n `32` status `ready` deltaP `57.8802` edge `4.0998` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `49.8002` n `32` status `ready` deltaP `57.5336` edge `3.7816` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `49.8002` n `32` status `ready` deltaP `57.5336` edge `3.7816` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.3874` n `32` status `ready` deltaP `54.5927` edge `3.335` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.3874` n `32` status `ready` deltaP `54.5927` edge `3.335` maxDD `0.0`
- `risk_on_high->index_24h` score `24.716` n `32` status `ready` deltaP `51.8198` edge `1.7142` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.716` n `32` status `ready` deltaP `51.8198` edge `1.7142` maxDD `0.0`
- `market_context_high->equity_24h` score `18.7435` n `156` status `ready` deltaP `31.5158` edge `1.9931` maxDD `-40.9667`
- `market_context_high->crypto_major_24h` score `18.3427` n `156` status `ready` deltaP `23.1847` edge `2.1471` maxDD `-54.8486`
- `risk_on_high->metal_24h` score `17.3764` n `32` status `ready` deltaP `34.4346` edge `1.2446` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.3764` n `32` status `ready` deltaP `34.4346` edge `1.2446` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `15.7131` n `156` status `ready` deltaP `17.7099` edge `1.9956` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `15.1462` n `32` status `ready` deltaP `28.2012` edge `1.1864` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1462` n `32` status `ready` deltaP `28.2012` edge `1.1864` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.3313` n `156` status `ready` deltaP `36.4352` edge `1.0897` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.5301` n `32` status `ready` deltaP `9.6799` edge `0.7474` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5301` n `32` status `ready` deltaP `9.6799` edge `0.7474` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.7861` n `156` status `ready` deltaP `28.5051` edge `1.134` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.8219` n `32` status `ready` deltaP `16.2348` edge `0.4952` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
