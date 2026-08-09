# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T12:22:26.303284+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9825`

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

- `market_context_high->equity_24h` score `3.8448` n `103` status `ready` deltaP `4.5729` edge `0.5959` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.5341` n `103` status `ready` deltaP `11.1701` edge `0.1943` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.0831` n `143` status `ready` deltaP `14.1374` edge `0.0633` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7797` n `143` status `ready` deltaP `10.6916` edge `0.028` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7302` n `103` status `ready` deltaP `21.4013` edge `0.0376` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.512` n `103` status `ready` deltaP `8.2322` edge `0.1639` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3337` n `143` status `ready` deltaP `3.8462` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.359` n `143` status `ready` deltaP `-0.3454` edge `-0.0048` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5187` n `143` status `ready` deltaP `5.3706` edge `-0.0037` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.648` n `143` status `ready` deltaP `-4.1392` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.7588` n `143` status `ready` deltaP `0.7612` edge `-0.0078` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8869` n `143` status `ready` deltaP `0.1121` edge `0.0082` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9496` n `143` status `ready` deltaP `-0.5937` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8305` n `143` status `ready` deltaP `-9.5348` edge `-0.0248` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3533` n `143` status `ready` deltaP `0.258` edge `-0.0641` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0896` n `143` status `ready` deltaP `-10.2383` edge `-0.057` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.5233` n `143` status `ready` deltaP `-6.2948` edge `-0.086` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.7432` n `103` status `ready` deltaP `3.2683` edge `-0.0843` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.797` n `103` status `ready` deltaP `-16.0919` edge `-0.2315` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7226` n `143` status `ready` deltaP `-5.0459` edge `-0.5652` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
