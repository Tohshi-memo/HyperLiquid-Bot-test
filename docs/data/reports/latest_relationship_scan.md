# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T21:07:30.728624+00:00`
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

- `market_context_high->unknown_4h` score `27.0187` n `58` status `ready` deltaP `1.6874` edge `2.2553` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `14.0624` n `101` status `ready` deltaP `2.4151` edge `1.8416` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `8.8496` n `101` status `ready` deltaP `2.8001` edge `1.2069` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.5579` n `101` status `ready` deltaP `17.0898` edge `0.3035` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.6818` n `101` status `ready` deltaP `18.3093` edge `0.2272` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5075` n `101` status `ready` deltaP `15.4829` edge `0.1523` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.1754` n `101` status `ready` deltaP `28.7524` edge `0.2178` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.7582` n `101` status `ready` deltaP `16.8302` edge `0.0866` maxDD `-2.8494`
- `market_context_high->index_24h` score `0.8196` n `42` status `ready` deltaP `-3.993` edge `0.1738` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.6497` n `58` status `ready` deltaP `4.6614` edge `0.0484` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5514` n `101` status `ready` deltaP `13.9992` edge `0.0128` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5076` n `58` status `ready` deltaP `8.3316` edge `0.0123` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4576` n `58` status `ready` deltaP `10.1229` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3683` n `101` status `ready` deltaP `10.3175` edge `0.0255` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2734` n `58` status `ready` deltaP `5.5493` edge `0.0166` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.2223` n `101` status `ready` deltaP `13.7451` edge `0.0323` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.0793` n `58` status `ready` deltaP `11.1228` edge `-0.0003` maxDD `-1.0949`
- `market_context_high->equity_24h` score `-0.0333` n `42` status `ready` deltaP `-7.9861` edge `0.3287` maxDD `-17.7117`
- `market_context_high->metal_24h` score `-0.0516` n `42` status `ready` deltaP `12.8224` edge `-0.0664` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `-0.0914` n `101` status `ready` deltaP `4.4895` edge `0.0068` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
