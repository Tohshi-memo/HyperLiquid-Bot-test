# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T20:22:40.380984+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2662`

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

- `market_context_high->unknown_1h` score `11996.6457` n `108` status `ready` deltaP `0.8373` edge `999.7347` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7535.224` n `107` status `ready` deltaP `-0.0071` edge `627.9638` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.1956` n `88` status `ready` deltaP `43.0239` edge `1.7888` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.903` n `88` status `ready` deltaP `25.0947` edge `1.498` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.6896` n `107` status `ready` deltaP `3.6286` edge `0.3985` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.0371` n `107` status `ready` deltaP `4.6957` edge `0.2627` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.5096` n `88` status `ready` deltaP `19.0656` edge `0.2242` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.3136` n `107` status `ready` deltaP `16.9905` edge `0.0421` maxDD `-6.0054`
- `market_context_high->crypto_major_1h` score `-0.2921` n `108` status `ready` deltaP `4.2471` edge `0.0739` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3137` n `108` status `ready` deltaP `2.5172` edge `0.0042` maxDD `-1.2295`
- `market_context_high->metal_1h` score `-0.3388` n `108` status `ready` deltaP `3.7425` edge `0.0133` maxDD `-2.6517`
- `market_context_high->crypto_alt_1h` score `-0.7885` n `108` status `ready` deltaP `-2.5338` edge `0.038` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.4037` n `108` status `ready` deltaP `5.5944` edge `0.0236` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6564` n `108` status `ready` deltaP `-11.9982` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-2.0613` n `107` status `ready` deltaP `-4.2654` edge `-0.009` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.4007` n `108` status `ready` deltaP `-9.6696` edge `-0.0274` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.4057` n `107` status `ready` deltaP `-15.335` edge `-0.0046` maxDD `-1.794`
- `market_context_high->fx_24h` score `-7.2608` n `88` status `ready` deltaP `-24.9842` edge `-0.0112` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1265` n `107` status `ready` deltaP `-29.3139` edge `-0.1125` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.0317` n `107` status `ready` deltaP `-8.7133` edge `-0.1102` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
