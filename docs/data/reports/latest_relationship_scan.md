# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T01:52:32.781455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3230`

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

- `news_risk_high->unknown_1h` score `3309.6097` n `31` status `ready` deltaP `1.6322` edge `275.8075` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3174.0079` n `31` status `ready` deltaP `3.4815` edge `264.4831` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.6882` n `31` status `ready` deltaP `27.9029` edge `1.288` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.29` n `31` status `ready` deltaP `26.1698` edge `0.8497` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.4089` n `31` status `ready` deltaP `23.9168` edge `0.7913` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.3469` n `31` status `ready` deltaP `18.986` edge `0.5727` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.1479` n `31` status `ready` deltaP `28.6881` edge `0.2858` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7078` n `31` status `ready` deltaP `38.6762` edge `0.1473` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.6232` n `31` status `ready` deltaP `13.8818` edge `0.6419` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.356` n `31` status `ready` deltaP `12.1877` edge `0.2259` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.2337` n `31` status `ready` deltaP `27.7734` edge `0.027` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2265` n `31` status `ready` deltaP `27.3518` edge `0.0117` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.2035` n `31` status `ready` deltaP `14.7479` edge `0.104` maxDD `-0.1621`
- `news_risk_high->index_24h` score `2.1632` n `31` status `ready` deltaP `24.6101` edge `0.0162` maxDD `0.0`
- `news_risk_high->crypto_major_1h` score `1.8134` n `31` status `ready` deltaP `4.9208` edge `0.2458` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6416` n `31` status `ready` deltaP `8.0645` edge `0.1924` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1169` n `31` status `ready` deltaP `24.3432` edge `0.0088` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3492` n `31` status `ready` deltaP `8.8267` edge `0.0257` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2419` n `31` status `ready` deltaP `10.0708` edge `0.0196` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3567` n `31` status `ready` deltaP `-2.3614` edge `0.0122` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
