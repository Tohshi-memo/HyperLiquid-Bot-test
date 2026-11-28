# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T10:22:27.714559+00:00`
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

- `news_risk_high->unknown_1h` score `3385.3896` n `31` status `ready` deltaP `2.0813` edge `282.1195` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3252.0286` n `31` status `ready` deltaP `3.7864` edge `270.9828` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `22.1856` n `31` status `ready` deltaP `33.7955` edge `1.6235` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.9989` n `31` status `ready` deltaP `31.7158` edge `1.1218` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.3324` n `31` status `ready` deltaP `27.2097` edge `0.8463` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.492` n `31` status `ready` deltaP `22.0348` edge `0.6478` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4015` n `31` status `ready` deltaP `29.9076` edge `0.2988` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.3467` n `31` status `ready` deltaP `16.3208` edge `0.7184` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9895` n `31` status `ready` deltaP `41.1025` edge `0.1546` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.7941` n `31` status `ready` deltaP `15.6539` edge `0.2393` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.4222` n `31` status `ready` deltaP `29.7551` edge `0.0295` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3419` n `31` status `ready` deltaP `25.8232` edge `0.023` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2876` n `31` status `ready` deltaP `28.1003` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.0969` n `31` status `ready` deltaP `13.8497` edge `0.1011` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8959` n `31` status `ready` deltaP `6.4178` edge `0.2464` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.707` n `31` status `ready` deltaP `8.813` edge `0.1958` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1309` n `31` status `ready` deltaP `24.6426` edge `0.0086` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3951` n `31` status `ready` deltaP `9.5889` edge `0.0265` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3389` n `31` status `ready` deltaP `11.4427` edge `0.0229` maxDD `-0.7918`
- `market_context_high->fx_4h` score `0.2962` n `34` status `ready` deltaP `8.9759` edge `0.0166` maxDD `-0.0772`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
