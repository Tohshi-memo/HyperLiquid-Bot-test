# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T10:37:30.282754+00:00`
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

- `news_risk_high->unknown_1h` score `3385.0596` n `31` status `ready` deltaP `2.0813` edge `282.092` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3255.0154` n `31` status `ready` deltaP `3.7864` edge `271.2317` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.3591` n `31` status `ready` deltaP `33.9688` edge `1.6368` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.1483` n `31` status `ready` deltaP `31.8891` edge `1.1331` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.393` n `31` status `ready` deltaP `27.383` edge `0.8502` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.5594` n `31` status `ready` deltaP `22.1872` edge `0.6524` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4317` n `31` status `ready` deltaP `30.06` edge `0.3003` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.4069` n `31` status `ready` deltaP `16.4732` edge `0.7251` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9919` n `31` status `ready` deltaP `41.1025` edge `0.1548` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8164` n `31` status `ready` deltaP `15.8272` edge `0.24` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4368` n `31` status `ready` deltaP `29.9076` edge `0.0297` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3467` n `31` status `ready` deltaP `25.8232` edge `0.0234` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2876` n `31` status `ready` deltaP `28.1003` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.0837` n `31` status `ready` deltaP `13.7` edge `0.101` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.9099` n `31` status `ready` deltaP `6.5675` edge `0.2472` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.707` n `31` status `ready` deltaP `8.813` edge `0.1958` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1231` n `31` status `ready` deltaP `24.4929` edge `0.0086` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3943` n `31` status `ready` deltaP `9.5889` edge `0.0264` maxDD `-0.5151`
- `market_context_high->metal_4h` score `0.3408` n `35` status `ready` deltaP `7.2953` edge `0.0362` maxDD `-0.2914`
- `news_risk_high->metal_4h` score `0.3405` n `31` status `ready` deltaP `11.4427` edge `0.0231` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
