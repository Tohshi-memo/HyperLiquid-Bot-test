# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T06:52:13.932675+00:00`
- Price records: `672`
- Market context records: `1819`
- Flow alert records: `7133`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

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

- `market_context_high->crypto_alt_4h` score `6.9465` n `185` status `ready` deltaP `22.6269` edge `0.5425` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8716` n `178` status `ready` deltaP `27.5905` edge `0.6313` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.5665` n `30` status `ready` deltaP `29.563` edge `0.4156` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.5232` n `185` status `ready` deltaP `26.5359` edge `0.4913` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.6899` n `185` status `ready` deltaP `17.388` edge `0.4773` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6382` n `178` status `ready` deltaP `17.8683` edge `0.3069` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.2914` n `30` status `ready` deltaP `25.02` edge `0.1392` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.007` n `185` status `ready` deltaP `15.9196` edge `0.2539` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.6322` n `178` status `ready` deltaP `17.6244` edge `0.5917` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.4761` n `178` status `ready` deltaP `13.6919` edge `0.6471` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9058` n `30` status `ready` deltaP `21.6362` edge `-0.0009` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8369` n `185` status `ready` deltaP `11.7057` edge `0.1006` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4254` n `192` status `ready` deltaP `6.0099` edge `0.094` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3567` n `192` status `ready` deltaP `6.5245` edge `0.0976` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.3201` n `30` status `ready` deltaP `9.3699` edge `0.0509` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.1312` n `192` status `ready` deltaP `4.1168` edge `0.041` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2033` n `178` status `ready` deltaP `17.9912` edge `0.7217` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.2561` n `178` status `ready` deltaP `10.9141` edge `0.0108` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.3986` n `192` status `ready` deltaP `0.0406` edge `0.0118` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4294` n `30` status `ready` deltaP `16.7066` edge `-0.1192` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
