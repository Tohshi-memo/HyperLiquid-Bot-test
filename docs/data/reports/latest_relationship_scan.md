# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T16:07:27.086523+00:00`
- Price records: `672`
- Market context records: `3498`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13142`

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

- `risk_on_high->crypto_major_24h` score `54.456` n `32` status `ready` deltaP `57.9861` edge `4.1557` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `54.456` n `32` status `ready` deltaP `57.9861` edge `4.1557` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `51.3983` n `32` status `ready` deltaP `58.1597` edge `3.9106` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `51.3983` n `32` status `ready` deltaP `58.1597` edge `3.9106` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.6336` n `32` status `ready` deltaP `55.5556` edge `3.3491` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.6336` n `32` status `ready` deltaP `55.5556` edge `3.3491` maxDD `0.0`
- `risk_on_high->index_24h` score `24.478` n `32` status `ready` deltaP `51.2153` edge `1.6984` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.478` n `32` status `ready` deltaP `51.2153` edge `1.6984` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `19.2604` n `155` status `ready` deltaP `23.6917` edge `2.2202` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.0462` n `155` status `ready` deltaP `32.3298` edge `2.0129` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `17.4914` n `155` status `ready` deltaP `18.7041` edge `2.133` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `16.0841` n `32` status `ready` deltaP `31.0764` edge `1.1593` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0841` n `32` status `ready` deltaP `31.0764` edge `1.1593` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `14.875` n `32` status `ready` deltaP `28.2012` edge `1.1638` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.875` n `32` status `ready` deltaP `28.2012` edge `1.1638` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1046` n `155` status `ready` deltaP `35.7314` edge `1.0755` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.1874` n `32` status `ready` deltaP `9.0701` edge `0.7229` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.1874` n `32` status `ready` deltaP `9.0701` edge `0.7229` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.0281` n `155` status `ready` deltaP `25.5522` edge `1.0565` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.966` n `32` status `ready` deltaP `16.997` edge `0.5086` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
