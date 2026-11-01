# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T02:22:32.410989+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6225`

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

- `market_context_high->unknown_24h` score `4759.4161` n `73` status `ready` deltaP `-5.9052` edge `396.6823` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `201.8649` n `73` status `ready` deltaP `0.9251` edge `16.8292` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `81.4624` n `108` status `ready` deltaP `-5.0454` edge `6.8508` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.7157` n `92` status `ready` deltaP `35.0921` edge `1.1097` maxDD `-6.3871`
- `market_context_high->equity_24h` score `13.0917` n `73` status `ready` deltaP `25.5351` edge `1.1322` maxDD `-10.9165`
- `news_risk_high->crypto_alt_4h` score `5.4812` n `108` status `ready` deltaP `20.7317` edge `0.4572` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.3733` n `73` status `ready` deltaP `46.1972` edge `0.1581` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.8705` n `73` status `ready` deltaP `28.8464` edge `0.0803` maxDD `-0.3387`
- `market_context_high->fx_1h` score `0.9835` n `73` status `ready` deltaP `15.0275` edge `0.0002` maxDD `-0.1407`
- `news_risk_high->crypto_alt_1h` score `0.8313` n `108` status `ready` deltaP `8.727` edge `0.1065` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.7443` n `73` status `ready` deltaP `14.2374` edge `0.043` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.6731` n `73` status `ready` deltaP `9.63` edge `0.0209` maxDD `-0.3209`
- `market_context_high->commodity_24h` score `0.5211` n `73` status `ready` deltaP `26.2081` edge `0.1039` maxDD `-10.9452`
- `market_context_high->fx_4h` score `0.4773` n `73` status `ready` deltaP `11.4873` edge `0.0023` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.3466` n `73` status `ready` deltaP `2.2045` edge `0.1173` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.2809` n `73` status `ready` deltaP `-5.5546` edge `0.2014` maxDD `-4.2683`
- `market_context_high->crypto_major_1h` score `-0.2138` n `73` status `ready` deltaP `1.5831` edge `0.0648` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.4332` n `73` status `ready` deltaP `-0.4307` edge `0.0182` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.458` n `73` status `ready` deltaP `-0.6849` edge `0.0017` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.553` n `73` status `ready` deltaP `0.1907` edge `0.0861` maxDD `-5.9953`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
