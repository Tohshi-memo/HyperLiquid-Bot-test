# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T23:37:28.138520+00:00`
- Price records: `672`
- Market context records: `3939`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11355`

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

- `risk_on_high->unknown_4h` score `88.5634` n `43` status `ready` deltaP `1.3933` edge `11.536` maxDD `-11.6138`
- `risk_on_and_context->unknown_4h` score `88.5634` n `43` status `ready` deltaP `1.3933` edge `11.536` maxDD `-11.6138`
- `market_context_high->unknown_4h` score `15.6938` n `179` status `ready` deltaP `-3.5827` edge `1.8726` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3767` n `40` status `ready` deltaP `42.0139` edge `0.5013` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3767` n `40` status `ready` deltaP `42.0139` edge `0.5013` maxDD `0.0`
- `market_context_high->unknown_24h` score `5.6497` n `165` status `ready` deltaP `-11.6636` edge `2.1413` maxDD `-112.4188`
- `risk_on_high->equity_4h` score `4.2179` n `43` status `ready` deltaP `37.8793` edge `0.1037` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.2179` n `43` status `ready` deltaP `37.8793` edge `0.1037` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.63` n `165` status `ready` deltaP `20.8018` edge `0.4668` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.4644` n `165` status `ready` deltaP `25.7923` edge `0.2307` maxDD `-7.1159`
- `risk_on_high->index_24h` score `3.0604` n `40` status `ready` deltaP `30.0347` edge `0.0548` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.0604` n `40` status `ready` deltaP `30.0347` edge `0.0548` maxDD `0.0`
- `market_context_high->metal_24h` score `2.827` n `165` status `ready` deltaP `15.4325` edge `0.2842` maxDD `-9.1203`
- `risk_on_high->crypto_major_4h` score `2.7618` n `43` status `ready` deltaP `24.571` edge `0.1329` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.7618` n `43` status `ready` deltaP `24.571` edge `0.1329` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.5068` n `179` status `ready` deltaP `17.1915` edge `0.1874` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.264` n `40` status `ready` deltaP `4.1667` edge `0.2895` maxDD `-12.6221`
- `risk_on_and_context->commodity_24h` score `1.264` n `40` status `ready` deltaP `4.1667` edge `0.2895` maxDD `-12.6221`
- `risk_on_high->equity_1h` score `1.0981` n `43` status `ready` deltaP `11.3042` edge `0.0555` maxDD `-0.8151`
- `risk_on_and_context->equity_1h` score `1.0981` n `43` status `ready` deltaP `11.3042` edge `0.0555` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
