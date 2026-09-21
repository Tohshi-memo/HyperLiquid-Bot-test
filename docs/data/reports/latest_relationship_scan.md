# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T22:07:30.374898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9868`

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

- `market_context_high->unknown_4h` score `25.1419` n `58` status `ready` deltaP `1.6874` edge `2.0989` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `13.0613` n `101` status `ready` deltaP `1.7206` edge `1.7628` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `8.1005` n `101` status `ready` deltaP `2.1057` edge `1.1491` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4192` n `101` status `ready` deltaP `16.48` edge `0.296` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.4806` n `101` status `ready` deltaP `17.6995` edge `0.2145` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4716` n `101` status `ready` deltaP `15.1835` edge `0.1513` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.2903` n `101` status `ready` deltaP `29.4468` edge `0.2279` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.7079` n `101` status `ready` deltaP `16.5308` edge `0.0844` maxDD `-2.8494`
- `market_context_high->index_24h` score `1.2491` n `46` status `ready` deltaP `-1.789` edge `0.1949` maxDD `-1.644`
- `market_context_high->equity_24h` score `1.0009` n `46` status `ready` deltaP `-5.782` edge `0.4466` maxDD `-17.7117`
- `market_context_high->crypto_major_24h` score `0.9241` n `46` status `ready` deltaP `0.9888` edge `0.7777` maxDD `-48.5989`
- `market_context_high->equity_1h` score `0.621` n `58` status `ready` deltaP `4.362` edge `0.048` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5262` n `101` status `ready` deltaP `13.6998` edge `0.0127` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4956` n `58` status `ready` deltaP `8.1819` edge `0.0123` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4325` n `58` status `ready` deltaP `9.8235` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3829` n `101` status `ready` deltaP `10.47` edge `0.0257` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2483` n `58` status `ready` deltaP `5.2499` edge `0.0165` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.1919` n `101` status `ready` deltaP `13.4403` edge `0.0318` maxDD `-2.0994`
- `market_context_high->metal_24h` score `0.0948` n `46` status `ready` deltaP `14.8928` edge `-0.068` maxDD `-0.2042`
- `market_context_high->index_4h` score `0.0824` n `58` status `ready` deltaP `11.1228` edge `0.0001` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
