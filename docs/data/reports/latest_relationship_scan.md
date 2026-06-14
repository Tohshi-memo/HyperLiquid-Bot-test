# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T16:22:29.104664+00:00`
- Price records: `672`
- Market context records: `3908`
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

- `risk_on_high->unknown_4h` score `47.7301` n `71` status `ready` deltaP `3.7831` edge `6.3082` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.7301` n `71` status `ready` deltaP `3.7831` edge `6.3082` maxDD `-13.467`
- `risk_on_high->equity_24h` score `22.3115` n `40` status `ready` deltaP `42.0139` edge `1.5792` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.3115` n `40` status `ready` deltaP `42.0139` edge `1.5792` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.2629` n `40` status `ready` deltaP `14.7569` edge `1.8915` maxDD `-7.4379`
- `risk_on_and_context->crypto_major_24h` score `22.2629` n `40` status `ready` deltaP `14.7569` edge `1.8915` maxDD `-7.4379`
- `risk_on_high->crypto_alt_24h` score `10.4262` n `40` status `ready` deltaP `12.6736` edge `0.9987` maxDD `-13.814`
- `risk_on_and_context->crypto_alt_24h` score `10.4262` n `40` status `ready` deltaP `12.6736` edge `0.9987` maxDD `-13.814`
- `risk_on_high->index_24h` score `9.1384` n `40` status `ready` deltaP `30.0347` edge `0.5613` maxDD `0.0`
- `risk_on_and_context->index_24h` score `9.1384` n `40` status `ready` deltaP `30.0347` edge `0.5613` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.7249` n `207` status `ready` deltaP `-1.7895` edge `1.415` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `6.1732` n `71` status `ready` deltaP `21.5261` edge `0.4714` maxDD `-5.3713`
- `risk_on_and_context->crypto_major_4h` score `6.1732` n `71` status `ready` deltaP `21.5261` edge `0.4714` maxDD `-5.3713`
- `market_context_high->equity_24h` score `6.1728` n `165` status `ready` deltaP `20.8018` edge `0.6787` maxDD `-14.5715`
- `market_context_high->index_24h` score `4.6368` n `165` status `ready` deltaP `25.7923` edge `0.3284` maxDD `-7.1159`
- `risk_on_high->equity_4h` score `2.9415` n `71` status `ready` deltaP `26.1229` edge `0.173` maxDD `-5.1621`
- `risk_on_and_context->equity_4h` score `2.9415` n `71` status `ready` deltaP `26.1229` edge `0.173` maxDD `-5.1621`
- `market_context_high->crypto_major_4h` score `2.8773` n `207` status `ready` deltaP `17.328` edge `0.3007` maxDD `-9.4488`
- `market_context_high->metal_24h` score `2.8473` n `165` status `ready` deltaP `18.8921` edge `0.2545` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.2452` n `207` status `ready` deltaP `14.0797` edge `0.1803` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
