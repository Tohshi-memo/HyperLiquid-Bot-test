# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T12:52:28.819448+00:00`
- Price records: `672`
- Market context records: `3893`
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

- `risk_on_high->unknown_4h` score `47.3554` n `72` status `ready` deltaP `5.7418` edge `6.2471` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.3554` n `72` status `ready` deltaP `5.7418` edge `6.2471` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.7225` n `32` status `ready` deltaP `34.2014` edge `2.6698` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.7225` n `32` status `ready` deltaP `34.2014` edge `2.6698` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `27.0467` n `32` status `ready` deltaP `42.0139` edge `1.9738` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `27.0467` n `32` status `ready` deltaP `42.0139` edge `1.9738` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.6314` n `32` status `ready` deltaP `32.1181` edge `1.7703` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.6314` n `32` status `ready` deltaP `32.1181` edge `1.7703` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2624` n `32` status `ready` deltaP `30.0347` edge `0.7383` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2624` n `32` status `ready` deltaP `30.0347` edge `0.7383` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.7017` n `209` status `ready` deltaP `-0.9169` edge `1.4062` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4236` n `154` status `ready` deltaP `19.2866` edge `0.7097` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.3938` n `72` status `ready` deltaP `19.1565` edge `0.434` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.3938` n `72` status `ready` deltaP `19.1565` edge `0.434` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.9462` n `154` status `ready` deltaP `25.4892` edge `0.3562` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.4989` n `154` status `ready` deltaP `23.0023` edge `0.2814` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4626` n `72` status `ready` deltaP `24.3394` edge `0.1564` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4626` n `72` status `ready` deltaP `24.3394` edge `0.1564` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.291` n `209` status `ready` deltaP `15.3088` edge `0.2653` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.209` n `154` status `ready` deltaP `6.1576` edge `0.5894` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
