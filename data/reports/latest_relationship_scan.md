# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T10:49:28.469571+00:00`
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

- `market_context_high->equity_24h` score `3.8052` n `103` status `ready` deltaP `4.5729` edge `0.5926` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6246` n `103` status `ready` deltaP `12.2118` edge `0.1949` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.1134` n `143` status `ready` deltaP `14.4423` edge `0.0638` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7773` n `143` status `ready` deltaP `10.6916` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7481` n `103` status `ready` deltaP `21.4013` edge `0.0399` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5512` n `103` status `ready` deltaP `8.9266` edge `0.1643` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3205` n `143` status `ready` deltaP `3.9959` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.391` n `143` status `ready` deltaP `-0.9442` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4919` n `143` status `ready` deltaP `5.6755` edge `-0.0035` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6651` n `143` status `ready` deltaP `-4.4386` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.81` n `143` status `ready` deltaP `0.1514` edge `-0.008` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8737` n `143` status `ready` deltaP `0.2618` edge `0.0083` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9726` n `143` status `ready` deltaP `-1.051` edge `-0.0168` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8269` n `143` status `ready` deltaP `-9.5348` edge `-0.0245` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4457` n `143` status `ready` deltaP `-0.6566` edge `-0.0657` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0764` n `143` status `ready` deltaP `-10.0886` edge `-0.0569` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.4881` n `143` status `ready` deltaP `-5.9899` edge `-0.0851` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.5483` n `103` status `ready` deltaP `4.31` edge `-0.075` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.4593` n `103` status `ready` deltaP `-15.0503` edge `-0.2103` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7741` n `143` status `ready` deltaP `-5.6447` edge `-0.5655` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
