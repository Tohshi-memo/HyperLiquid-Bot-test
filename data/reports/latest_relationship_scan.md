# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T22:07:32.985095+00:00`
- Price records: `672`
- Market context records: `5082`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10338`

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

- `market_context_high->unknown_24h` score `11.9526` n `75` status `ready` deltaP `27.1805` edge `0.8491` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `10.7185` n `105` status `ready` deltaP `1.4828` edge `0.9471` maxDD `-2.769`
- `market_context_high->unknown_4h` score `9.2325` n `93` status `ready` deltaP `21.4496` edge `0.7286` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.5304` n `93` status `ready` deltaP `18.7844` edge `0.5409` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.7599` n `93` status `ready` deltaP `17.2436` edge `0.5341` maxDD `-9.1918`
- `market_context_high->equity_4h` score `2.2204` n `93` status `ready` deltaP `11.4427` edge `0.2219` maxDD `-6.3852`
- `market_context_high->equity_1h` score `1.1194` n `105` status `ready` deltaP `10.2994` edge `0.0778` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.921` n `105` status `ready` deltaP `7.6205` edge `0.1286` maxDD `-5.2121`
- `market_context_high->crypto_alt_1h` score `0.8582` n `105` status `ready` deltaP `6.3815` edge `0.11` maxDD `-3.8153`
- `market_context_high->metal_1h` score `0.8534` n `105` status `ready` deltaP `12.4907` edge `0.0375` maxDD `-1.3057`
- `market_context_high->metal_4h` score `0.7336` n `93` status `ready` deltaP `10.1741` edge `0.1012` maxDD `-1.9651`
- `market_context_high->index_1h` score `0.3926` n `105` status `ready` deltaP `6.8435` edge `0.0169` maxDD `-0.3843`
- `market_context_high->index_4h` score `0.344` n `93` status `ready` deltaP `8.8021` edge `0.0461` maxDD `-1.0893`
- `market_context_high->commodity_4h` score `-0.4688` n `93` status `ready` deltaP `8.9217` edge `0.0093` maxDD `-3.6276`
- `market_context_high->fx_24h` score `-0.6287` n `75` status `ready` deltaP `-0.0903` edge `-0.0038` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.6751` n `105` status `ready` deltaP `0.8169` edge `0.0044` maxDD `-1.2883`
- `market_context_high->fx_4h` score `-1.2244` n `93` status `ready` deltaP `-7.2941` edge `-0.0063` maxDD `-1.497`
- `market_context_high->commodity_24h` score `-1.7103` n `75` status `ready` deltaP `10.3333` edge `0.0376` maxDD `-16.7268`
- `market_context_high->fx_1h` score `-1.8067` n `105` status `ready` deltaP `-12.217` edge `-0.0053` maxDD `-0.7713`
- `market_context_high->metal_24h` score `-4.3583` n `75` status `ready` deltaP `-3.7014` edge `0.0114` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
