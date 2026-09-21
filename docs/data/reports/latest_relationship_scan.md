# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T07:07:32.873717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9154`

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

- `market_context_high->unknown_4h` score `32.6605` n `58` status `ready` deltaP `1.23` edge `2.7285` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `23.6574` n `100` status `ready` deltaP `11.6667` edge `2.5795` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.4505` n `100` status `ready` deltaP `12.1111` edge `1.9449` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.3601` n `101` status `ready` deltaP `19.3763` edge `0.3551` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.9865` n `101` status `ready` deltaP `21.358` edge `0.3156` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7078` n `101` status `ready` deltaP `16.0817` edge `0.165` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1192` n `101` status `ready` deltaP `18.1775` edge `0.1077` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1144` n `100` status `ready` deltaP `22.8681` edge `0.121` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.9805` n `58` status `ready` deltaP `7.356` edge `0.058` maxDD `-0.36`
- `market_context_high->index_1h` score `0.7879` n `58` status `ready` deltaP `11.4753` edge `0.0147` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6017` n `101` status `ready` deltaP `14.4483` edge `0.014` maxDD `-0.8144`
- `market_context_high->index_4h` score `0.3714` n `58` status `ready` deltaP `15.3911` edge `0.0087` maxDD `-1.0949`
- `news_risk_high->metal_4h` score `0.3634` n `101` status `ready` deltaP `15.2695` edge `0.0339` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.3331` n `58` status `ready` deltaP `8.6259` edge `0.0059` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.3238` n `58` status `ready` deltaP `5.9984` edge `0.0178` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.1931` n `101` status `ready` deltaP `8.4883` edge `0.0231` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.0944` n `101` status `ready` deltaP `2.9688` edge `0.0129` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1657` n `58` status `ready` deltaP `-1.6415` edge `0.069` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.216` n `101` status `ready` deltaP `2.9925` edge `0.0064` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.3446` n `100` status `ready` deltaP `10.3264` edge `-0.0286` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
