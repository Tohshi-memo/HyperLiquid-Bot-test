# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T04:07:32.739071+00:00`
- Price records: `672`
- Market context records: `3548`
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

- `risk_on_high->crypto_major_24h` score `52.4398` n `32` status `ready` deltaP `57.5336` edge `3.9907` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `52.4398` n `32` status `ready` deltaP `57.5336` edge `3.9907` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `47.2609` n `32` status `ready` deltaP `57.187` edge `3.5723` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `47.2609` n `32` status `ready` deltaP `57.187` edge `3.5723` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.9298` n `32` status `ready` deltaP `54.5927` edge `3.3802` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.9298` n `32` status `ready` deltaP `54.5927` edge `3.3802` maxDD `0.0`
- `risk_on_high->index_24h` score `25.6168` n `32` status `ready` deltaP `53.8995` edge `1.7754` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.6168` n `32` status `ready` deltaP `53.8995` edge `1.7754` maxDD `0.0`
- `market_context_high->equity_24h` score `19.2859` n `156` status `ready` deltaP `31.5158` edge `2.0383` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6998` n `32` status `ready` deltaP `37.2075` edge `1.3364` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6998` n `32` status `ready` deltaP `37.2075` edge `1.3364` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `17.0058` n `156` status `ready` deltaP `22.8381` edge `2.038` maxDD `-54.8486`
- `risk_on_high->crypto_major_4h` score `14.4804` n `32` status `ready` deltaP `27.439` edge `1.136` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.4804` n `32` status `ready` deltaP `27.439` edge `1.136` maxDD `-5.9781`
- `market_context_high->index_24h` score `14.2321` n `156` status `ready` deltaP `38.5149` edge `1.1509` maxDD `-15.0661`
- `market_context_high->crypto_alt_24h` score `13.1737` n `156` status `ready` deltaP `17.3633` edge `1.7863` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6464` n `156` status `ready` deltaP `31.278` edge `1.2258` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `6.1104` n `32` status `ready` deltaP `7.6982` edge `0.6423` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.1104` n `32` status `ready` deltaP `7.6982` edge `0.6423` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.9581` n `32` status `ready` deltaP `16.8445` edge `0.5086` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
