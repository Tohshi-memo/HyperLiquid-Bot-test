# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T13:37:32.445913+00:00`
- Price records: `672`
- Market context records: `3897`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11118`

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

- `risk_on_high->unknown_4h` score `47.2795` n `72` status `ready` deltaP `5.437` edge `6.2394` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.2795` n `72` status `ready` deltaP `5.437` edge `6.2394` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `35.0257` n `32` status `ready` deltaP `34.7222` edge `2.6916` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `35.0257` n `32` status `ready` deltaP `34.7222` edge `2.6916` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `27.1727` n `32` status `ready` deltaP `42.0139` edge `1.9843` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `27.1727` n `32` status `ready` deltaP `42.0139` edge `1.9843` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.913` n `32` status `ready` deltaP `32.6389` edge `1.7903` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.913` n `32` status `ready` deltaP `32.6389` edge `1.7903` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3284` n `32` status `ready` deltaP `30.0347` edge `0.7438` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3284` n `32` status `ready` deltaP `30.0347` edge `0.7438` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.6258` n `209` status `ready` deltaP `-1.2217` edge `1.3985` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4847` n `157` status `ready` deltaP `19.7209` edge `0.7119` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.5096` n `72` status `ready` deltaP `19.6138` edge `0.4406` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.5096` n `72` status `ready` deltaP `19.6138` edge `0.4406` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.9111` n `157` status `ready` deltaP `25.5761` edge `0.3527` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3824` n `157` status `ready` deltaP `22.3858` edge `0.2758` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5132` n `72` status `ready` deltaP `24.4918` edge `0.1596` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5132` n `72` status `ready` deltaP `24.4918` edge `0.1596` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.4068` n `209` status `ready` deltaP `15.7661` edge `0.2719` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.1431` n `157` status `ready` deltaP `5.3631` edge `0.5892` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
