# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T17:22:31.434951+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7473`

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

- `market_context_high->unknown_24h` score `2755.0391` n `102` status `ready` deltaP `-8.8542` edge `229.6886` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `79.356` n `102` status `ready` deltaP `1.0641` edge `6.6192` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.115` n `108` status `ready` deltaP `-6.2431` edge `6.4965` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.5159` n `63` status `ready` deltaP `45.4365` edge `1.2452` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.1351` n `102` status `ready` deltaP `26.7055` edge `1.0256` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `4.9116` n `103` status `ready` deltaP `17.8413` edge `0.429` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8987` n `102` status `ready` deltaP `43.7909` edge `0.1346` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.7377` n `102` status `ready` deltaP `21.5238` edge `0.0438` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.2381` n `102` status `ready` deltaP `7.0809` edge `0.1953` maxDD `-4.48`
- `market_context_high->metal_1h` score `0.8737` n `102` status `ready` deltaP `12.5132` edge `0.0184` maxDD `-0.3209`
- `market_context_high->crypto_major_1h` score `0.6425` n `102` status `ready` deltaP `10.0358` edge `0.0894` maxDD `-5.2213`
- `news_risk_high->crypto_alt_1h` score `0.6214` n `108` status `ready` deltaP `7.6791` edge `0.096` maxDD `-3.9659`
- `market_context_high->equity_1h` score `0.4908` n `102` status `ready` deltaP `7.6934` edge `0.0992` maxDD `-2.3383`
- `market_context_high->fx_1h` score `0.2158` n `102` status `ready` deltaP `8.2394` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.2043` n `102` status `ready` deltaP `8.3453` edge `0.0005` maxDD `-0.1285`
- `market_context_high->metal_24h` score `0.122` n `102` status `ready` deltaP `14.2259` edge `0.1855` maxDD `-10.5088`
- `market_context_high->commodity_4h` score `0.0993` n `102` status `ready` deltaP `11.6751` edge `0.0559` maxDD `-1.014`
- `market_context_high->crypto_major_4h` score `0.0214` n `102` status `ready` deltaP `17.2345` edge `0.1609` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.3025` n `102` status `ready` deltaP `4.2357` edge `0.0024` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.3359` n `102` status `ready` deltaP `-0.8601` edge `0.0141` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
