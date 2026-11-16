# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T22:52:25.895504+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4392`

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

- `market_context_high->unknown_24h` score `1087.4195` n `43` status `ready` deltaP `3.4483` edge `90.5953` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.0058` n `50` status `ready` deltaP `59.2069` edge `4.1764` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.0354` n `50` status `ready` deltaP `37.8276` edge `2.4308` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.658` n `50` status `ready` deltaP `45.0776` edge `1.034` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.2958` n `43` status `ready` deltaP `47.2695` edge `1.7165` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.1443` n `43` status `ready` deltaP `17.9832` edge `1.5915` maxDD `-8.6878`
- `news_risk_high->crypto_alt_24h` score `9.477` n `50` status `ready` deltaP `22.4483` edge `1.5159` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0711` n `50` status `ready` deltaP `50.2414` edge `0.368` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.6871` n `50` status `ready` deltaP `42.4138` edge `0.2745` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4253` n `50` status `ready` deltaP `47.796` edge `0.1711` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5622` n `50` status `ready` deltaP `22.5449` edge `0.2929` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5394` n `50` status `ready` deltaP `26.7519` edge `0.3435` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3846` n `50` status `ready` deltaP `21.9696` edge `0.3565` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1219` n `50` status `ready` deltaP `37.2511` edge `0.1205` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2266` n `50` status `ready` deltaP `30.207` edge `0.1025` maxDD `-0.7999`
- `market_context_high->metal_24h` score `2.6219` n `43` status `ready` deltaP `26.8564` edge `0.1633` maxDD `-5.575`
- `news_risk_high->metal_1h` score `2.3372` n `50` status `ready` deltaP `26.0419` edge `0.0466` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5886` n `50` status `ready` deltaP `20.1916` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8722` n `50` status `ready` deltaP `18.3448` edge `0.2068` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8396` n `50` status `ready` deltaP `17.5928` edge `0.0883` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
