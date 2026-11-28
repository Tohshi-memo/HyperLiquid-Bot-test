# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T07:22:23.283383+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3716`

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

- `news_risk_high->unknown_1h` score `3355.6309` n `31` status `ready` deltaP `1.4825` edge `279.6436` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3232.9785` n `31` status `ready` deltaP `3.634` edge `269.3963` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `20.4845` n `31` status `ready` deltaP `31.7158` edge `1.4956` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.4345` n `31` status `ready` deltaP `29.636` edge `1.0053` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.8241` n `31` status `ready` deltaP `25.4766` edge `0.8155` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.9119` n `31` status `ready` deltaP `20.6628` edge `0.6086` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.2007` n `31` status `ready` deltaP `28.6881` edge `0.2902` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.889` n `31` status `ready` deltaP `14.644` edge `0.6709` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.8082` n `31` status `ready` deltaP `39.1961` edge `0.1522` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.5233` n `31` status `ready` deltaP `13.5741` edge `0.2306` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.2996` n `31` status `ready` deltaP `28.25` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->index_4h` score `2.2725` n `31` status `ready` deltaP `28.0783` edge `0.0282` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2667` n `31` status `ready` deltaP `25.3033` edge `0.0202` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.1304` n `31` status `ready` deltaP `14.1491` edge `0.1019` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8274` n `31` status `ready` deltaP `5.5196` edge `0.2436` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6712` n `31` status `ready` deltaP `8.5136` edge `0.1932` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0982` n `31` status `ready` deltaP `24.0438` edge `0.0084` maxDD `-0.2315`
- `market_context_high->fx_1h` score `0.4684` n `34` status `ready` deltaP `8.5241` edge `0.0036` maxDD `-0.0451`
- `market_context_high->equity_1h` score `0.462` n `34` status `ready` deltaP `11.1131` edge `0.026` maxDD `-1.2685`
- `news_risk_high->commodity_4h` score `0.2993` n `31` status `ready` deltaP `7.9121` edge `0.0254` maxDD `-0.5151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
