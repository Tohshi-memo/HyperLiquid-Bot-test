# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T06:52:27.407413+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3698`

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

- `news_risk_high->unknown_1h` score `3361.1353` n `31` status `ready` deltaP `1.4825` edge `280.1023` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3225.5325` n `31` status `ready` deltaP `3.634` edge `268.7758` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.2779` n `31` status `ready` deltaP `31.3692` edge `1.4807` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.2448` n `31` status `ready` deltaP `29.2894` edge `0.9918` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.7676` n `31` status `ready` deltaP `25.13` edge `0.8131` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.8795` n `31` status `ready` deltaP `20.6628` edge `0.6059` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2019` n `31` status `ready` deltaP `28.6881` edge `0.2903` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8781` n `31` status `ready` deltaP `14.644` edge `0.6695` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.7732` n `31` status `ready` deltaP `38.8495` edge `0.1516` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.4987` n `31` status `ready` deltaP `13.4008` edge `0.2297` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.3127` n `31` status `ready` deltaP `28.3997` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.2713` n `31` status `ready` deltaP `28.0783` edge `0.0281` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2631` n `31` status `ready` deltaP `25.3033` edge `0.0199` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1664` n `31` status `ready` deltaP `14.4485` edge `0.1029` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8437` n `31` status `ready` deltaP `5.5196` edge `0.2457` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7117` n `31` status `ready` deltaP `8.813` edge `0.1964` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1161` n `31` status `ready` deltaP `24.3432` edge `0.0087` maxDD `-0.2315`
- `market_context_high->fx_1h` score `0.5065` n `32` status `ready` deltaP `8.9259` edge `0.0041` maxDD `-0.0451`
- `market_context_high->equity_1h` score `0.3597` n `32` status `ready` deltaP `9.2066` edge `0.0256` maxDD `-1.2685`
- `news_risk_high->commodity_4h` score `0.3001` n `31` status `ready` deltaP `7.9121` edge `0.0255` maxDD `-0.5151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
