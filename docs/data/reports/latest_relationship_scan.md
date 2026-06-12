# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T00:37:31.143008+00:00`
- Price records: `672`
- Market context records: `3636`
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

- `risk_on_high->crypto_major_24h` score `39.0853` n `32` status `ready` deltaP `44.0972` edge `2.9674` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `39.0853` n `32` status `ready` deltaP `44.0972` edge `2.9674` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `35.8208` n `32` status `ready` deltaP `46.1806` edge `2.6772` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `35.8208` n `32` status `ready` deltaP `46.1806` edge `2.6772` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `31.4359` n `32` status `ready` deltaP `43.2292` edge `2.3466` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `31.4359` n `32` status `ready` deltaP `43.2292` edge `2.3466` maxDD `-0.8779`
- `risk_on_high->index_24h` score `20.4836` n `32` status `ready` deltaP `46.1806` edge `1.3991` maxDD `0.0`
- `risk_on_and_context->index_24h` score `20.4836` n `32` status `ready` deltaP `46.1806` edge `1.3991` maxDD `0.0`
- `risk_on_high->metal_24h` score `12.6621` n `32` status `ready` deltaP `31.7708` edge `0.8695` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `12.6621` n `32` status `ready` deltaP `31.7708` edge `0.8695` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.097` n `32` status `ready` deltaP `21.6463` edge `0.976` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.097` n `32` status `ready` deltaP `21.6463` edge `0.976` maxDD `-5.9781`
- `market_context_high->equity_24h` score `11.5329` n `157` status `ready` deltaP `23.2507` edge `1.3725` maxDD `-35.3144`
- `market_context_high->index_24h` score `10.0876` n `157` status `ready` deltaP `31.5309` edge `0.802` maxDD `-11.3924`
- `market_context_high->crypto_major_24h` score `5.0803` n `157` status `ready` deltaP `10.2795` edge `1.0615` maxDD `-49.5335`
- `market_context_high->metal_24h` score `4.4494` n `157` status `ready` deltaP `26.0781` edge `0.7918` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `3.5652` n `32` status `ready` deltaP `2.0579` edge `0.4678` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.5652` n `32` status `ready` deltaP `2.0579` edge `0.4678` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.609` n `32` status `ready` deltaP `10.5945` edge `0.3773` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.609` n `32` status `ready` deltaP `10.5945` edge `0.3773` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
