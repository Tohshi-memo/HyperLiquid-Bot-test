# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T07:52:27.078384+00:00`
- Price records: `672`
- Market context records: `3362`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `57.2156` n `32` status `ready` deltaP `60.5903` edge `4.3683` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `57.2156` n `32` status `ready` deltaP `60.5903` edge `4.3683` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.7789` n `32` status `ready` deltaP `55.3819` edge `4.1275` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.7789` n `32` status `ready` deltaP `55.3819` edge `4.1275` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.1301` n `32` status `ready` deltaP `56.7708` edge `3.4657` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.1301` n `32` status `ready` deltaP `56.7708` edge `3.4657` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1926` n `32` status `ready` deltaP `50.8681` edge `1.5936` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1926` n `32` status `ready` deltaP `50.8681` edge `1.5936` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `15.4548` n `32` status `ready` deltaP `28.3537` edge `1.2111` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.4548` n `32` status `ready` deltaP `28.3537` edge `1.2111` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `15.3113` n `32` status `ready` deltaP `33.5069` edge `1.0787` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.3113` n `32` status `ready` deltaP `33.5069` edge `1.0787` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `12.7151` n `162` status `ready` deltaP `17.1489` edge `2.4473` maxDD `-67.1851`
- `market_context_high->index_24h` score `12.1213` n `162` status `ready` deltaP `36.0533` edge `1.0252` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.7237` n `162` status `ready` deltaP `31.4622` edge `2.0067` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.373` n `32` status `ready` deltaP `8.7652` edge `0.7404` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.373` n `32` status `ready` deltaP `8.7652` edge `0.7404` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5731` n `32` status `ready` deltaP `14.4055` edge `0.4755` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5731` n `32` status `ready` deltaP `14.4055` edge `0.4755` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.9894` n `32` status `ready` deltaP `6.2687` edge `0.3202` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
