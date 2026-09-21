# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T07:37:33.762165+00:00`
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

- `market_context_high->unknown_4h` score `32.8393` n `58` status `ready` deltaP `1.23` edge `2.7434` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `23.4433` n `101` status `ready` deltaP `11.6164` edge `2.562` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.2917` n `101` status `ready` deltaP `12.0015` edge `1.9324` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.3045` n `101` status `ready` deltaP `19.0715` edge `0.3525` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.9805` n `101` status `ready` deltaP `21.358` edge `0.3151` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.709` n `101` status `ready` deltaP `16.0817` edge `0.1651` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1348` n `101` status `ready` deltaP `18.3272` edge `0.108` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.0618` n `101` status `ready` deltaP `22.5024` edge `0.1167` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.9397` n `58` status `ready` deltaP `7.0566` edge `0.0566` maxDD `-0.36`
- `market_context_high->index_1h` score `0.7615` n `58` status `ready` deltaP `11.1759` edge `0.0145` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.573` n `101` status `ready` deltaP `14.1489` edge `0.0136` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.355` n `101` status `ready` deltaP `15.2695` edge `0.0332` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.3525` n `58` status `ready` deltaP `15.0862` edge `0.0083` maxDD `-1.0949`
- `market_context_high->fx_1h` score `0.3211` n `58` status `ready` deltaP `8.4762` edge `0.0059` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.295` n `58` status `ready` deltaP `5.699` edge `0.0174` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.1931` n `101` status `ready` deltaP `8.4883` edge `0.0231` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.1351` n `101` status `ready` deltaP `2.6694` edge `0.0115` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1502` n `58` status `ready` deltaP `-1.4918` edge `0.0693` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.228` n `101` status `ready` deltaP `2.8428` edge `0.0064` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.3986` n `101` status `ready` deltaP `9.6036` edge `-0.0307` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
