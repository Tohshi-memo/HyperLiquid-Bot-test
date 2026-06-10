# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T20:52:23.964540+00:00`
- Price records: `672`
- Market context records: `3518`
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

- `risk_on_high->crypto_major_24h` score `53.7636` n `32` status `ready` deltaP `57.8802` edge `4.0987` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.7636` n `32` status `ready` deltaP `57.8802` edge `4.0987` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `49.8242` n `32` status `ready` deltaP `57.5336` edge `3.7836` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `49.8242` n `32` status `ready` deltaP `57.5336` edge `3.7836` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.349` n `32` status `ready` deltaP `54.5927` edge `3.3318` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.349` n `32` status `ready` deltaP `54.5927` edge `3.3318` maxDD `0.0`
- `risk_on_high->index_24h` score `24.6649` n `32` status `ready` deltaP `51.6464` edge `1.7111` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.6649` n `32` status `ready` deltaP `51.6464` edge `1.7111` maxDD `0.0`
- `market_context_high->equity_24h` score `18.7051` n `156` status `ready` deltaP `31.5158` edge `1.9899` maxDD `-40.9667`
- `market_context_high->crypto_major_24h` score `18.3295` n `156` status `ready` deltaP `23.1847` edge `2.146` maxDD `-54.8486`
- `risk_on_high->metal_24h` score `17.2845` n `32` status `ready` deltaP `34.2613` edge `1.2381` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.2845` n `32` status `ready` deltaP `34.2613` edge `1.2381` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `15.7371` n `156` status `ready` deltaP `17.7099` edge `1.9976` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `15.1198` n `32` status `ready` deltaP `28.2012` edge `1.1842` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.1198` n `32` status `ready` deltaP `28.2012` edge `1.1842` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.2802` n `156` status `ready` deltaP `36.2618` edge `1.0866` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.4905` n `32` status `ready` deltaP `9.6799` edge `0.7441` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4905` n `32` status `ready` deltaP `9.6799` edge `0.7441` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.7264` n `156` status `ready` deltaP `28.3318` edge `1.1275` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.8094` n `32` status `ready` deltaP `16.2348` edge `0.4936` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
