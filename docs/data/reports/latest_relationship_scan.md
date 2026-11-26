# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T09:07:31.005745+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3419`

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

- `news_risk_high->unknown_4h` score `3262.7983` n `31` status `ready` deltaP `3.4815` edge `271.8823` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3235.5805` n `31` status `ready` deltaP `1.6322` edge `269.6384` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `105.2886` n `31` status `ready` deltaP `1.6322` edge `8.7726` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `38.7833` n `31` status `ready` deltaP `45.4861` edge `2.9287` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.7115` n `31` status `ready` deltaP `46.3542` edge `2.8336` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.0712` n `31` status `ready` deltaP `45.6597` edge `2.3682` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.0338` n `31` status `ready` deltaP `27.8275` edge `0.821` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.7728` n `31` status `ready` deltaP `39.3588` edge `0.6834` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.3057` n `31` status `ready` deltaP `32.0341` edge `0.5894` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9761` n `31` status `ready` deltaP `19.0647` edge `0.909` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.4044` n `31` status `ready` deltaP `46.875` edge `0.2212` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2316` n `31` status `ready` deltaP `44.4893` edge `0.1522` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.777` n `31` status `ready` deltaP `20.5862` edge `0.1962` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5671` n `31` status `ready` deltaP `38.2917` edge `0.068` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7477` n `31` status `ready` deltaP `32.4416` edge `0.0212` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4883` n `31` status `ready` deltaP `10.0106` edge `0.2984` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2978` n `31` status `ready` deltaP `13.304` edge `0.2416` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.097` n `31` status `ready` deltaP `26.6572` edge `0.0255` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5134` n `31` status `ready` deltaP `29.5827` edge `0.0247` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1086` n `31` status `ready` deltaP `16.7781` edge `0.086` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
