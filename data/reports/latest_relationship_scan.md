# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T03:22:12.407960+00:00`
- Price records: `672`
- Market context records: `935`
- Flow alert records: `2618`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1386`

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

- `risk_on_high->crypto_major_24h` score `21.7228` n `32` status `ready` deltaP `32.4653` edge `1.5938` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `21.7228` n `32` status `ready` deltaP `32.4653` edge `1.5938` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.8494` n `169` status `ready` deltaP `29.5067` edge `0.9908` maxDD `-1.3382`
- `risk_on_high->crypto_alt_24h` score `12.8711` n `32` status `ready` deltaP `5.7292` edge `1.0344` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `12.8711` n `32` status `ready` deltaP `5.7292` edge `1.0344` maxDD `0.0`
- `risk_on_high->equity_24h` score `12.7976` n `32` status `ready` deltaP `25.0` edge `0.8998` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `12.7976` n `32` status `ready` deltaP `25.0` edge `0.8998` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.8159` n `169` status `ready` deltaP `5.7292` edge `0.5298` maxDD `0.0`
- `risk_on_high->index_24h` score `3.9533` n `32` status `ready` deltaP `26.7361` edge `0.1512` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9533` n `32` status `ready` deltaP `26.7361` edge `0.1512` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `3.2503` n `32` status `ready` deltaP `23.7043` edge `0.1333` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.2503` n `32` status `ready` deltaP `23.7043` edge `0.1333` maxDD `-0.6377`
- `risk_on_high->equity_4h` score `3.1467` n `32` status `ready` deltaP `5.1067` edge `0.2647` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.1467` n `32` status `ready` deltaP `5.1067` edge `0.2647` maxDD `-0.9217`
- `risk_on_high->crypto_major_4h` score `2.8362` n `32` status `ready` deltaP `21.0366` edge `0.1333` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.8362` n `32` status `ready` deltaP `21.0366` edge `0.1333` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.1667` n `32` status `ready` deltaP `9.9848` edge `0.1228` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.1667` n `32` status `ready` deltaP `9.9848` edge `0.1228` maxDD `-0.038`
- `risk_on_high->metal_1h` score `0.9934` n `32` status `ready` deltaP `11.5644` edge `0.0287` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `0.9934` n `32` status `ready` deltaP `11.5644` edge `0.0287` maxDD `-0.5074`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
