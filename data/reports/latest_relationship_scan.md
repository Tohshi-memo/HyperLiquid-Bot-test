# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T20:52:36.522201+00:00`
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

- `market_context_high->unknown_4h` score `27.5443` n `58` status `ready` deltaP `1.6874` edge `2.2991` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `14.3127` n `101` status `ready` deltaP `2.5887` edge `1.8613` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `9.0411` n `101` status `ready` deltaP `2.9737` edge `1.2217` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.5735` n `101` status `ready` deltaP `17.0898` edge `0.3048` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.7348` n `101` status `ready` deltaP `18.4617` edge `0.2306` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5147` n `101` status `ready` deltaP `15.4829` edge `0.1529` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.1453` n `101` status `ready` deltaP `28.5788` edge `0.2151` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.7846` n `101` status `ready` deltaP `16.9799` edge `0.0878` maxDD `-2.8494`
- `market_context_high->index_24h` score `0.8478` n `42` status `ready` deltaP `-3.8194` edge `0.175` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.6497` n `58` status `ready` deltaP `4.6614` edge `0.0484` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5514` n `101` status `ready` deltaP `13.9992` edge `0.0128` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5196` n `58` status `ready` deltaP `8.4813` edge `0.0123` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4456` n `58` status `ready` deltaP `9.9732` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.367` n `101` status `ready` deltaP `10.3175` edge `0.0254` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2734` n `58` status `ready` deltaP `5.5493` edge `0.0166` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.2357` n `101` status `ready` deltaP `13.8976` edge `0.0324` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.0785` n `58` status `ready` deltaP `11.1228` edge `-0.0004` maxDD `-1.0949`
- `market_context_high->equity_24h` score `0.0303` n `42` status `ready` deltaP `-7.8125` edge `0.3357` maxDD `-17.7117`
- `market_context_high->metal_24h` score `-0.0528` n `42` status `ready` deltaP `12.8224` edge `-0.0665` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `-0.1034` n `101` status `ready` deltaP `4.3398` edge `0.0068` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
