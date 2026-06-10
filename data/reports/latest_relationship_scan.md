# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T05:52:24.096218+00:00`
- Price records: `672`
- Market context records: `3456`
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

- `risk_on_high->crypto_major_24h` score `56.6277` n `32` status `ready` deltaP `58.5069` edge `4.3332` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.6277` n `32` status `ready` deltaP `58.5069` edge `4.3332` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `56.1872` n `32` status `ready` deltaP `59.8958` edge `4.2981` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.1872` n `32` status `ready` deltaP `59.8958` edge `4.2981` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.0185` n `32` status `ready` deltaP `56.0764` edge `3.3777` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.0185` n `32` status `ready` deltaP `56.0764` edge `3.3777` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9783` n `32` status `ready` deltaP `51.3889` edge `1.6556` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9783` n `32` status `ready` deltaP `51.3889` edge `1.6556` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.2803` n `155` status `ready` deltaP `20.4402` edge `2.5205` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.4321` n `155` status `ready` deltaP `24.2125` edge `2.3977` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.431` n `155` status `ready` deltaP `32.8506` edge `2.0415` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `15.7239` n `32` status `ready` deltaP `29.5732` edge `1.2254` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.7239` n `32` status `ready` deltaP `29.5732` edge `1.2254` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.8798` n `32` status `ready` deltaP `28.9931` edge `0.9895` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.8798` n `32` status `ready` deltaP `28.9931` edge `0.9895` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.6049` n `155` status `ready` deltaP `35.905` edge `1.0327` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.6071` n `32` status `ready` deltaP `9.8323` edge `0.7528` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.6071` n `32` status `ready` deltaP `9.8323` edge `0.7528` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.649` n `32` status `ready` deltaP `19.436` edge `0.5799` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.649` n `32` status `ready` deltaP `19.436` edge `0.5799` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
