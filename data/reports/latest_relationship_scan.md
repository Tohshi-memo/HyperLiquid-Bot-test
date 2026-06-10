# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T16:37:32.216356+00:00`
- Price records: `672`
- Market context records: `3499`
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

- `risk_on_high->crypto_major_24h` score `54.3564` n `32` status `ready` deltaP `57.8802` edge `4.1481` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `54.3564` n `32` status `ready` deltaP `57.8802` edge `4.1481` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `51.1983` n `32` status `ready` deltaP `57.8802` edge `3.8958` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `51.1983` n `32` status `ready` deltaP `57.8802` edge `3.8958` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.4801` n `32` status `ready` deltaP `55.286` edge `3.3381` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.4801` n `32` status `ready` deltaP `55.286` edge `3.3381` maxDD `0.0`
- `risk_on_high->index_24h` score `24.3995` n `32` status `ready` deltaP `50.9532` edge `1.6936` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.3995` n `32` status `ready` deltaP `50.9532` edge `1.6936` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `19.1608` n `155` status `ready` deltaP `23.5858` edge `2.2126` maxDD `-54.8486`
- `market_context_high->equity_24h` score `18.8926` n `155` status `ready` deltaP `32.0602` edge `2.0019` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `17.2914` n `155` status `ready` deltaP `18.4246` edge `2.1182` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `16.1296` n `32` status `ready` deltaP `31.315` edge `1.1615` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.1296` n `32` status `ready` deltaP `31.315` edge `1.1615` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `14.8281` n `32` status `ready` deltaP `28.1107` edge `1.1605` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.8281` n `32` status `ready` deltaP `28.1107` edge `1.1605` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.026` n `155` status `ready` deltaP `35.4693` edge `1.0707` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.1361` n `32` status `ready` deltaP `8.985` edge `0.7192` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.1361` n `32` status `ready` deltaP `8.985` edge `0.7192` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.0577` n `155` status `ready` deltaP `25.7908` edge `1.0587` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.9244` n `32` status `ready` deltaP `16.7666` edge `0.5048` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
