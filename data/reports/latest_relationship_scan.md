# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T14:37:26.411731+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7444`

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

- `news_risk_high->unknown_1h` score `3419.0412` n `31` status `ready` deltaP `2.231` edge `284.9228` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3245.0181` n `31` status `ready` deltaP `3.634` edge `270.3996` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `24.4721` n `31` status `ready` deltaP `36.7418` edge `1.7944` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.2962` n `31` status `ready` deltaP `34.662` edge `1.2936` maxDD `0.0`
- `news_risk_high->equity_24h` score `13.07` n `31` status `ready` deltaP `29.2894` edge `0.8939` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.3072` n `31` status `ready` deltaP `24.1689` edge `0.7015` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.9053` n `31` status `ready` deltaP `18.3025` edge `0.7768` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.8196` n `31` status `ready` deltaP `32.1942` edge `0.3184` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0888` n `31` status `ready` deltaP `41.969` edge `0.1571` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9614` n `31` status `ready` deltaP `17.0403` edge `0.244` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.6024` n `31` status `ready` deltaP `31.7369` edge `0.0313` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4561` n `31` status `ready` deltaP `26.5165` edge `0.0279` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3678` n `31` status `ready` deltaP `28.9985` edge `0.0125` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2695` n `31` status `ready` deltaP `14.8976` edge `0.1085` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.1181` n `31` status `ready` deltaP `7.316` edge `0.2689` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9767` n `31` status `ready` deltaP `10.9088` edge `0.2164` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1621` n `31` status `ready` deltaP `25.0917` edge `0.0096` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.6866` n `51` status `ready` deltaP `11.3941` edge `0.0224` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4497` n `31` status `ready` deltaP `10.5035` edge `0.0274` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.3903` n `63` status `ready` deltaP `10.6169` edge `0.0014` maxDD `-0.1042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
