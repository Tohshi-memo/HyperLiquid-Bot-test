# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T18:52:26.221349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7639`

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

- `market_context_high->unknown_24h` score `2905.8675` n `99` status `ready` deltaP `-9.3592` edge `242.261` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `87.1706` n `99` status `ready` deltaP `0.8561` edge `7.2718` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.5985` n `108` status `ready` deltaP `-5.3448` edge `6.5308` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.282` n `69` status `ready` deltaP `45.7125` edge `1.3072` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.8945` n `99` status `ready` deltaP `25.9628` edge `1.0105` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.1179` n `108` status `ready` deltaP `19.0549` edge `0.4381` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8738` n `99` status `ready` deltaP `43.4344` edge `0.1349` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6592` n `99` status `ready` deltaP `20.5731` edge `0.0436` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8553` n `99` status `ready` deltaP `12.2528` edge `0.0186` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.7485` n `108` status `ready` deltaP `8.4276` edge `0.1016` maxDD `-3.9659`
- `market_context_high->equity_4h` score `0.7173` n `99` status `ready` deltaP `5.8035` edge `0.1926` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.473` n `99` status `ready` deltaP `7.2764` edge `0.0997` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.323` n `99` status `ready` deltaP `8.9972` edge `0.0842` maxDD `-5.2213`
- `market_context_high->fx_1h` score `0.2677` n `99` status `ready` deltaP `9.221` edge `-0.0004` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.2611` n `99` status `ready` deltaP `9.0247` edge `0.0007` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.1579` n `99` status `ready` deltaP `12.5108` edge `0.0574` maxDD `-0.978`
- `market_context_high->metal_24h` score `0.0026` n `99` status `ready` deltaP `12.7999` edge `0.1797` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.1588` n `99` status `ready` deltaP `16.3433` edge `0.1447` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.2066` n `99` status `ready` deltaP `4.0586` edge `0.0023` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.3524` n `99` status `ready` deltaP `-1.1024` edge `0.0136` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
