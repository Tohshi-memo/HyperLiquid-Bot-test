# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T14:22:29.131796+00:00`
- Price records: `672`
- Market context records: `3900`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11356`

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

- `risk_on_high->unknown_4h` score `47.1621` n `72` status `ready` deltaP `4.9796` edge `6.2274` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.1621` n `72` status `ready` deltaP `4.9796` edge `6.2274` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `33.6987` n `33` status `ready` deltaP `32.3075` edge `2.6072` maxDD `-0.4819`
- `risk_on_and_context->crypto_major_24h` score `33.6987` n `33` status `ready` deltaP `32.3075` edge `2.6072` maxDD `-0.4819`
- `risk_on_high->equity_24h` score `26.5919` n `33` status `ready` deltaP `42.0139` edge `1.9359` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.5919` n `33` status `ready` deltaP `42.0139` edge `1.9359` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.589` n `33` status `ready` deltaP `30.2241` edge `1.7106` maxDD `-1.7075`
- `risk_on_and_context->crypto_alt_24h` score `22.589` n `33` status `ready` deltaP `30.2241` edge `1.7106` maxDD `-1.7075`
- `risk_on_high->index_24h` score `11.0548` n `33` status `ready` deltaP `30.0347` edge `0.721` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.0548` n `33` status `ready` deltaP `30.0347` edge `0.721` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.5084` n `209` status `ready` deltaP `-1.6791` edge `1.3865` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4954` n `160` status `ready` deltaP `20.1389` edge `0.71` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.6446` n `72` status `ready` deltaP `20.0711` edge `0.4488` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.6446` n `72` status `ready` deltaP `20.0711` edge `0.4488` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.8638` n `160` status `ready` deltaP `25.6597` edge `0.3482` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.2723` n `160` status `ready` deltaP `21.9097` edge `0.2698` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5857` n `72` status `ready` deltaP `24.9492` edge `0.1626` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5857` n `72` status `ready` deltaP `24.9492` edge `0.1626` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.5418` n `209` status `ready` deltaP `16.2234` edge `0.2801` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.0799` n `160` status `ready` deltaP `4.6181` edge `0.5889` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
