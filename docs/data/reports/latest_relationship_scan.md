# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T21:37:33.705139+00:00`
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

- `market_context_high->unknown_4h` score `25.8019` n `58` status `ready` deltaP `1.6874` edge `2.1539` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `13.5594` n `101` status `ready` deltaP `2.0678` edge `1.802` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `8.4666` n `101` status `ready` deltaP `2.4529` edge `1.1773` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4879` n `101` status `ready` deltaP `16.7849` edge `0.2997` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.5806` n `101` status `ready` deltaP `18.0044` edge `0.2208` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4896` n `101` status `ready` deltaP `15.3332` edge `0.1518` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.234` n `101` status `ready` deltaP `29.0996` edge `0.223` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.739` n `101` status `ready` deltaP `16.6805` edge `0.086` maxDD `-2.8494`
- `market_context_high->index_24h` score `1.0438` n `44` status `ready` deltaP `-2.8251` edge `0.1847` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.6234` n `58` status `ready` deltaP `4.362` edge `0.0482` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5382` n `101` status `ready` deltaP `13.8495` edge `0.0127` maxDD `-0.8144`
- `market_context_high->equity_24h` score `0.5204` n `44` status `ready` deltaP `-6.8182` edge `0.3919` maxDD `-17.7117`
- `market_context_high->index_1h` score `0.5076` n `58` status `ready` deltaP `8.3316` edge `0.0123` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4456` n `58` status `ready` deltaP `9.9732` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3683` n `101` status `ready` deltaP `10.3175` edge `0.0255` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2603` n `58` status `ready` deltaP `5.3996` edge `0.0165` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.2065` n `101` status `ready` deltaP `13.5927` edge `0.032` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.0809` n `58` status `ready` deltaP `11.1228` edge `-0.0001` maxDD `-1.0949`
- `market_context_high->metal_24h` score `0.0313` n `44` status `ready` deltaP `13.9046` edge `-0.0667` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `-0.1034` n `101` status `ready` deltaP `4.3398` edge `0.0068` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
