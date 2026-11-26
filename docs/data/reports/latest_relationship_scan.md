# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T22:52:33.293214+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3348`

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

- `news_risk_high->unknown_1h` score `3216.8496` n `31` status `ready` deltaP `2.0813` edge `268.0745` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3193.1118` n `31` status `ready` deltaP `4.3962` edge `266.069` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `27.7556` n `31` status `ready` deltaP `36.8056` edge `2.0676` maxDD `0.0`
- `news_risk_high->equity_24h` score `24.8122` n `31` status `ready` deltaP `35.9375` edge `1.8281` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.6029` n `31` status `ready` deltaP `36.1111` edge `1.5595` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.7832` n `31` status `ready` deltaP `23.864` edge `0.7432` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.4287` n `31` status `ready` deltaP `35.243` edge `0.5155` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.3964` n `31` status `ready` deltaP `22.8327` edge `0.4083` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.3081` n `31` status `ready` deltaP `16.7781` edge `0.8386` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.0068` n `31` status `ready` deltaP `42.5795` edge `0.1462` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.3865` n `31` status `ready` deltaP `37.3264` edge `0.1167` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.1689` n `31` status `ready` deltaP `18.6401` edge `0.1585` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.9863` n `31` status `ready` deltaP `33.5661` edge `0.0511` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5488` n `31` status `ready` deltaP `30.4955` edge `0.0176` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2725` n `31` status `ready` deltaP `7.9148` edge `0.2847` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0585` n `31` status `ready` deltaP `11.0585` edge `0.2259` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3576` n `31` status `ready` deltaP `27.4869` edge `0.0187` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.6898` n `31` status `ready` deltaP `13.1196` edge `0.0567` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2518` n `31` status `ready` deltaP `9.8938` edge `0.0061` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4047` n `31` status `ready` deltaP `-2.2117` edge `0.0072` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
