# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T22:22:28.810102+00:00`
- Price records: `672`
- Market context records: `3933`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11443`

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

- `risk_on_high->unknown_4h` score `77.2031` n `48` status `ready` deltaP `-3.6585` edge `10.1364` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `77.2031` n `48` status `ready` deltaP `-3.6585` edge `10.1364` maxDD `-13.467`
- `market_context_high->unknown_4h` score `14.6543` n `184` status `ready` deltaP `-4.202` edge `1.7901` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `10.3283` n `40` status `ready` deltaP `42.0139` edge `0.5806` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.3283` n `40` status `ready` deltaP `42.0139` edge `0.5806` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.1626` n `48` status `ready` deltaP `38.3638` edge `0.1792` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `5.1626` n `48` status `ready` deltaP `38.3638` edge `0.1792` maxDD `-0.0458`
- `risk_on_high->index_24h` score `3.9232` n `40` status `ready` deltaP `30.0347` edge `0.1267` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.9232` n `40` status `ready` deltaP `30.0347` edge `0.1267` maxDD `0.0`
- `market_context_high->equity_24h` score `3.8076` n `165` status `ready` deltaP `20.8018` edge `0.4816` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.6252` n `165` status `ready` deltaP `25.7923` edge `0.2441` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `3.4338` n `48` status `ready` deltaP `25.3049` edge `0.184` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.4338` n `48` status `ready` deltaP `25.3049` edge `0.184` maxDD `-2.6576`
- `market_context_high->metal_24h` score `2.4802` n `165` status `ready` deltaP `15.4325` edge `0.2553` maxDD `-9.1203`
- `market_context_high->unknown_24h` score `2.1394` n `165` status `ready` deltaP `-13.8258` edge `2.0572` maxDD `-126.2732`
- `market_context_high->crypto_major_4h` score `1.8568` n `184` status `ready` deltaP `17.6962` edge `0.2132` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.7677` n `40` status `ready` deltaP `4.1667` edge `0.306` maxDD `-11.9177`
- `risk_on_and_context->commodity_24h` score `1.7677` n `40` status `ready` deltaP `4.1667` edge `0.306` maxDD `-11.9177`
- `market_context_high->equity_4h` score `1.3861` n `184` status `ready` deltaP `15.9001` edge `0.1799` maxDD `-8.2982`
- `risk_on_high->equity_1h` score `0.9558` n `48` status `ready` deltaP `8.4456` edge `0.0627` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
