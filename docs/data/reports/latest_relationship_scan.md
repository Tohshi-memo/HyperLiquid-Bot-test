# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T16:07:32.617462+00:00`
- Price records: `672`
- Market context records: `7581`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14513`

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

- `market_context_high->commodity_4h` score `0.2439` n `161` status `ready` deltaP `9.7698` edge `0.0312` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.021` n `161` status `ready` deltaP `5.3476` edge `0.0105` maxDD `-0.9072`
- `market_context_high->commodity_1h` score `-0.0967` n `161` status `ready` deltaP `6.4741` edge `0.006` maxDD `-1.5775`
- `market_context_high->commodity_24h` score `-0.1076` n `153` status `ready` deltaP `12.4024` edge `0.0667` maxDD `-7.0012`
- `market_context_high->index_4h` score `-0.4833` n `161` status `ready` deltaP `11.1564` edge `0.0363` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.524` n `161` status `ready` deltaP `0.9998` edge `-0.0004` maxDD `-0.6615`
- `market_context_high->unknown_24h` score `-0.6564` n `154` status `ready` deltaP `8.446` edge `0.0958` maxDD `-9.234`
- `market_context_high->metal_1h` score `-0.6855` n `161` status `ready` deltaP `0.5207` edge `0.0132` maxDD `-1.0307`
- `market_context_high->crypto_alt_1h` score `-0.7058` n `161` status `ready` deltaP `-0.1609` edge `0.0022` maxDD `-4.9959`
- `market_context_high->equity_1h` score `-0.7545` n `161` status `ready` deltaP `4.7265` edge `0.0413` maxDD `-8.8965`
- `market_context_high->crypto_major_1h` score `-0.7905` n `161` status `ready` deltaP `5.3018` edge `0.0009` maxDD `-7.3409`
- `market_context_high->fx_24h` score `-0.8907` n `153` status `ready` deltaP `6.9004` edge `0.0144` maxDD `-3.7699`
- `market_context_high->unknown_1h` score `-0.9538` n `161` status `ready` deltaP `0.2659` edge `-0.0617` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.378` n `161` status `ready` deltaP `1.0841` edge `0.0413` maxDD `-11.3487`
- `market_context_high->metal_4h` score `-1.5159` n `161` status `ready` deltaP `0.2765` edge `0.052` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.5266` n `161` status `ready` deltaP `3.5406` edge `0.2174` maxDD `-21.9375`
- `market_context_high->crypto_major_4h` score `-2.0807` n `161` status `ready` deltaP `5.2682` edge `0.043` maxDD `-19.9239`
- `market_context_high->fx_4h` score `-2.1807` n `161` status `ready` deltaP `-1.8386` edge `-0.001` maxDD `-2.1439`
- `market_context_high->unknown_4h` score `-2.3181` n `161` status `ready` deltaP `9.6548` edge `-0.1259` maxDD `-6.1862`
- `market_context_high->metal_24h` score `-3.322` n `154` status `ready` deltaP `-4.7393` edge `0.0813` maxDD `-14.382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
