# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T00:52:31.869607+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `13990.5871` n `94` status `ready` deltaP `0.7548` edge `1165.8934` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8948.0765` n `94` status `ready` deltaP `-0.8886` edge `745.7095` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1363.4302` n `31` status `ready` deltaP `3.8777` edge `113.6109` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1198.5702` n `31` status `ready` deltaP `4.3962` edge `99.8572` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.9624` n `31` status `ready` deltaP `39.3588` edge `0.7827` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0117` n `31` status `ready` deltaP `25.5409` edge `0.8344` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6656` n `31` status `ready` deltaP `14.3391` edge `0.9007` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0398` n `31` status `ready` deltaP `19.8377` edge `0.2231` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.5864` n `31` status `ready` deltaP `37.3771` edge `0.0757` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7382` n `31` status `ready` deltaP `31.9925` edge `0.0234` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4868` n `31` status `ready` deltaP `9.8609` edge `0.2992` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0916` n `31` status `ready` deltaP `8.5136` edge `0.2471` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6168` n `31` status `ready` deltaP `21.961` edge `0.1166` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5921` n `31` status `ready` deltaP `29.8821` edge `0.0328` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7708` n `31` status `ready` deltaP `17.6682` edge `0.0208` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0346` n `31` status `ready` deltaP `1.6805` edge `0.0121` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.617` n `94` status `ready` deltaP `6.104` edge `0.01` maxDD `-1.05`
- `market_context_high->index_1h` score `-0.6883` n `94` status `ready` deltaP `-0.7804` edge `-0.005` maxDD `-1.1061`
- `market_context_high->metal_1h` score `-0.8313` n `94` status `ready` deltaP `0.3695` edge `-0.0068` maxDD `-2.5283`
- `market_context_high->fx_1h` score `-1.1905` n `94` status `ready` deltaP `-8.5425` edge `-0.0007` maxDD `-0.325`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
