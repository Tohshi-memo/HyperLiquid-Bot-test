# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T09:37:29.051168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3431`

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

- `news_risk_high->unknown_4h` score `3259.2403` n `31` status `ready` deltaP `3.4815` edge `271.5858` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3234.5845` n `31` status `ready` deltaP `1.6322` edge `269.5554` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `104.2926` n `31` status `ready` deltaP `1.6322` edge `8.6896` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `38.3019` n `31` status `ready` deltaP `45.1389` edge `2.8909` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.403` n `31` status `ready` deltaP `46.0069` edge `2.8102` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.759` n `31` status `ready` deltaP `45.3125` edge `2.3445` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.0338` n `31` status `ready` deltaP `27.8275` edge `0.821` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.815` n `31` status `ready` deltaP `39.5112` edge `0.6859` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.1892` n `31` status `ready` deltaP `31.6869` edge `0.582` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `7.0068` n `31` status `ready` deltaP `19.3696` edge `0.9109` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.3382` n `31` status `ready` deltaP `46.5278` edge `0.218` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1966` n `31` status `ready` deltaP `44.142` edge `0.1516` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.783` n `31` status `ready` deltaP `20.5862` edge `0.1967` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.5975` n `31` status `ready` deltaP `38.5966` edge `0.0685` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7764` n `31` status `ready` deltaP `32.741` edge `0.0216` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4673` n `31` status `ready` deltaP `9.7112` edge `0.2977` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2736` n `31` status `ready` deltaP `13.0046` edge `0.2405` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.0702` n `31` status `ready` deltaP `26.3523` edge `0.0253` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5033` n `31` status `ready` deltaP `29.433` edge `0.0244` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1101` n `31` status `ready` deltaP `16.7781` edge `0.0862` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
