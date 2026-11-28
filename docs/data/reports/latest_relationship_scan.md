# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T06:37:24.898161+00:00`
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

- `news_risk_high->unknown_1h` score `3361.1233` n `31` status `ready` deltaP `1.4825` edge `280.1013` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3221.0817` n `31` status `ready` deltaP `3.634` edge `268.4049` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.1321` n `31` status `ready` deltaP `31.1958` edge `1.4697` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.1133` n `31` status `ready` deltaP `29.1161` edge `0.982` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.7249` n `31` status `ready` deltaP `24.9567` edge `0.8107` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.8241` n `31` status `ready` deltaP `20.5104` edge `0.6023` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.1801` n `31` status `ready` deltaP `28.5356` edge `0.2895` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.8429` n `31` status `ready` deltaP `14.4915` edge `0.666` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.7558` n `31` status `ready` deltaP `38.6762` edge `0.1513` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.4776` n `31` status `ready` deltaP `13.2275` edge `0.2291` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.2996` n `31` status `ready` deltaP `28.25` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2607` n `31` status `ready` deltaP `25.3033` edge `0.0197` maxDD `0.0`
- `news_risk_high->index_4h` score `2.2579` n `31` status `ready` deltaP `27.9259` edge `0.028` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.158` n `31` status `ready` deltaP `14.4485` edge `0.1022` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8211` n `31` status `ready` deltaP `5.5196` edge `0.2428` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7008` n `31` status `ready` deltaP `8.813` edge `0.195` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1154` n `31` status `ready` deltaP `24.3432` edge `0.0086` maxDD `-0.2315`
- `market_context_high->fx_1h` score `0.416` n `31` status `ready` deltaP `7.7651` edge `0.0043` maxDD `-0.0451`
- `news_risk_high->commodity_4h` score `0.3009` n `31` status `ready` deltaP `7.9121` edge `0.0256` maxDD `-0.5151`
- `market_context_high->equity_1h` score `0.2859` n `31` status `ready` deltaP `7.9969` edge `0.0242` maxDD `-1.2685`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
