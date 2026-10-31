# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T22:36:46.411261+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6607`

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

- `market_context_high->unknown_24h` score `3554.2046` n `88` status `ready` deltaP `-11.5057` edge `296.3034` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `107.0352` n `88` status `ready` deltaP `1.1086` edge `8.9255` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `80.0788` n `108` status `ready` deltaP `-5.1951` edge `6.7365` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.392` n `84` status `ready` deltaP `43.4772` edge `1.2505` maxDD `-0.2812`
- `market_context_high->equity_24h` score `10.6731` n `88` status `ready` deltaP `22.8062` edge `1.0131` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.5694` n `108` status `ready` deltaP `21.189` edge `0.4615` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9841` n `88` status `ready` deltaP `44.0025` edge `0.1403` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.4507` n `88` status `ready` deltaP `18.0571` edge `0.043` maxDD `-0.7323`
- `market_context_high->commodity_4h` score `1.4108` n `88` status `ready` deltaP `17.9047` edge `0.0665` maxDD `-0.4639`
- `news_risk_high->crypto_alt_1h` score `0.8397` n `108` status `ready` deltaP `8.8767` edge `0.1062` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.7772` n `88` status `ready` deltaP `11.1867` edge `0.0192` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.5921` n `88` status `ready` deltaP `13.0128` edge `0.0017` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.5077` n `88` status `ready` deltaP `12.5272` edge `0.0` maxDD `-0.1407`
- `market_context_high->equity_4h` score `0.4212` n `88` status `ready` deltaP `0.6791` edge `0.1888` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.37` n `88` status `ready` deltaP `4.5455` edge `0.1047` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.1972` n `88` status `ready` deltaP `6.9679` edge `0.0816` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.4068` n `88` status `ready` deltaP `-2.3884` edge `0.0152` maxDD `-0.4475`
- `market_context_high->metal_24h` score `-0.4891` n `88` status `ready` deltaP `6.9128` edge `0.1559` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.5936` n `88` status `ready` deltaP `0.6873` edge `0.0018` maxDD `-1.1344`
- `market_context_high->crypto_major_4h` score `-0.6956` n `88` status `ready` deltaP `13.775` edge `0.093` maxDD `-14.5879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
