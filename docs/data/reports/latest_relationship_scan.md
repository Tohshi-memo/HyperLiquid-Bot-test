# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T04:22:25.643156+00:00`
- Price records: `672`
- Market context records: `3549`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13200`

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

- `risk_on_high->crypto_major_24h` score `52.3084` n `32` status `ready` deltaP `57.3603` edge `3.9809` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `52.3084` n `32` status `ready` deltaP `57.3603` edge `3.9809` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `47.0982` n `32` status `ready` deltaP `57.0136` edge `3.5599` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `47.0982` n `32` status `ready` deltaP `57.0136` edge `3.5599` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.9034` n `32` status `ready` deltaP `54.5927` edge `3.378` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.9034` n `32` status `ready` deltaP `54.5927` edge `3.378` maxDD `0.0`
- `risk_on_high->index_24h` score `25.618` n `32` status `ready` deltaP `53.8995` edge `1.7755` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.618` n `32` status `ready` deltaP `53.8995` edge `1.7755` maxDD `0.0`
- `market_context_high->equity_24h` score `19.2595` n `156` status `ready` deltaP `31.5158` edge `2.0361` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6998` n `32` status `ready` deltaP `37.2075` edge `1.3364` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6998` n `32` status `ready` deltaP `37.2075` edge `1.3364` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `16.8743` n `156` status `ready` deltaP `22.6648` edge `2.0282` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `14.389` n `32` status `ready` deltaP `27.2866` edge `1.1294` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.389` n `32` status `ready` deltaP `27.2866` edge `1.1294` maxDD `-5.9781`
- `market_context_high->index_24h` score `14.2333` n `156` status `ready` deltaP `38.5149` edge `1.151` maxDD `-15.0661`
- `market_context_high->crypto_alt_24h` score `13.0111` n `156` status `ready` deltaP `17.1899` edge `1.7739` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6464` n `156` status `ready` deltaP `31.278` edge `1.2258` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `6.0106` n `32` status `ready` deltaP `7.5457` edge `0.635` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.0106` n `32` status `ready` deltaP `7.5457` edge `0.635` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.9377` n `32` status `ready` deltaP `16.6921` edge `0.507` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
