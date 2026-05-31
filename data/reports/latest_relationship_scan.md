# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T12:22:15.878832+00:00`
- Price records: `672`
- Market context records: `2456`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `20.6352` n `39` status `ready` deltaP `45.6998` edge `1.4738` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `20.1439` n `39` status `ready` deltaP `55.2484` edge `1.3543` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `16.1709` n `39` status `ready` deltaP `29.554` edge `1.182` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.6887` n `39` status `ready` deltaP `20.7132` edge `0.8107` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.4451` n `39` status `ready` deltaP `24.6928` edge `0.4784` maxDD `-1.4744`
- `news_risk_high->index_24h` score `6.6418` n `39` status `ready` deltaP `17.0406` edge `0.4651` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.7963` n `110` status `ready` deltaP `21.8024` edge `0.3705` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.2836` n `132` status `ready` deltaP `19.8401` edge `0.4057` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.1604` n `132` status `ready` deltaP `20.4592` edge `0.4782` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.6637` n `39` status `ready` deltaP `38.2612` edge `0.0687` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1221` n `39` status `ready` deltaP `26.7433` edge `0.2891` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.4622` n `110` status `ready` deltaP `11.8087` edge `0.6262` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.0266` n `39` status `ready` deltaP `25.6762` edge `0.0161` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `1.9001` n `39` status `ready` deltaP `22.7123` edge `0.0501` maxDD `-1.4536`
- `market_context_high->unknown_4h` score `1.7281` n `132` status `ready` deltaP `10.4721` edge `0.1664` maxDD `-2.7098`
- `news_risk_high->unknown_4h` score `1.4485` n `39` status `ready` deltaP `14.4348` edge `0.0968` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.2329` n `110` status `ready` deltaP `6.2247` edge `0.1077` maxDD `-0.7163`
- `news_risk_high->fx_1h` score `0.8757` n `39` status `ready` deltaP `13.0547` edge `0.0116` maxDD `-0.0524`
- `market_context_high->crypto_major_1h` score `0.8453` n `136` status `ready` deltaP `9.0833` edge `0.1293` maxDD `-4.2199`
- `news_risk_high->metal_4h` score `0.7594` n `39` status `ready` deltaP `4.3581` edge `0.2249` maxDD `-7.1939`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
