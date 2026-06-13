# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T16:22:29.690821+00:00`
- Price records: `672`
- Market context records: `3807`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13352`

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

- `risk_on_high->crypto_major_24h` score `31.1842` n `32` status `ready` deltaP `32.8125` edge `2.3842` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `31.1842` n `32` status `ready` deltaP `32.8125` edge `2.3842` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.5949` n `32` status `ready` deltaP `41.1458` edge `1.8586` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.5949` n `32` status `ready` deltaP `41.1458` edge `1.8586` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2827` n `32` status `ready` deltaP `31.9444` edge `1.7424` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2827` n `32` status `ready` deltaP `31.9444` edge `1.7424` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4076` n `32` status `ready` deltaP `31.25` edge `0.7423` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4076` n `32` status `ready` deltaP `31.25` edge `0.7423` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.294` n `32` status `ready` deltaP `14.3293` edge `0.7912` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.294` n `32` status `ready` deltaP `14.3293` edge `0.7912` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.3796` n `150` status `ready` deltaP `20.4791` edge `0.7532` maxDD `-13.6477`
- `market_context_high->crypto_major_24h` score `5.5837` n `150` status `ready` deltaP `7.2708` edge `0.8632` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.3697` n `150` status `ready` deltaP `26.5833` edge `0.3842` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.279` n `150` status `ready` deltaP `26.1528` edge `0.3254` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.7643` n `184` status `ready` deltaP `14.0576` edge `0.3267` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.438` n `32` status `ready` deltaP `7.5457` edge `0.2475` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.438` n `32` status `ready` deltaP `7.5457` edge `0.2475` maxDD `-5.7426`
- `risk_on_high->commodity_4h` score `1.4147` n `32` status `ready` deltaP `16.997` edge `0.0913` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `1.4147` n `32` status `ready` deltaP `16.997` edge `0.0913` maxDD `-3.6044`
- `risk_on_high->metal_24h` score `1.3269` n `32` status `ready` deltaP `14.2361` edge `0.0418` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
