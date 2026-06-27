# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T23:22:26.168338+00:00`
- Price records: `672`
- Market context records: `4983`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `12.3224` n `90` status `ready` deltaP `4.0586` edge `1.0499` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.3047` n `88` status `ready` deltaP `17.0732` edge `0.5424` maxDD `-7.1331`
- `market_context_high->unknown_24h` score `5.8671` n `77` status `ready` deltaP `28.1521` edge `0.3355` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.2808` n `88` status `ready` deltaP `13.7334` edge `0.4879` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `2.3232` n `88` status `ready` deltaP `22.561` edge `0.1243` maxDD `-4.1549`
- `market_context_high->metal_4h` score `1.1431` n `88` status `ready` deltaP `11.5577` edge `0.1261` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.6724` n `88` status `ready` deltaP `5.9175` edge `0.1849` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5439` n `88` status `ready` deltaP `7.3725` edge `0.0434` maxDD `-0.7781`
- `market_context_high->equity_1h` score `0.5327` n `90` status `ready` deltaP `7.1158` edge `0.0782` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.4374` n `90` status `ready` deltaP `4.7904` edge `0.121` maxDD `-5.0821`
- `market_context_high->crypto_alt_1h` score `0.1339` n `90` status `ready` deltaP `4.3812` edge `0.0902` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1329` n `90` status `ready` deltaP `3.5296` edge `0.0372` maxDD `-1.3057`
- `market_context_high->fx_24h` score `-0.2956` n `77` status `ready` deltaP `5.3098` edge `0.0029` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.3815` n `90` status `ready` deltaP `1.7731` edge `0.0136` maxDD `-0.6131`
- `market_context_high->commodity_1h` score `-0.4253` n `90` status `ready` deltaP `0.7718` edge `0.0063` maxDD `-1.278`
- `market_context_high->fx_4h` score `-0.8571` n `88` status `ready` deltaP `-1.7462` edge `-0.0012` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2274` n `88` status `ready` deltaP `4.2267` edge `-0.0052` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.5629` n `90` status `ready` deltaP `-10.0399` edge `-0.0035` maxDD `-0.4511`
- `market_context_high->commodity_24h` score `-3.6653` n `77` status `ready` deltaP `10.4054` edge `-0.0284` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.4156` n `77` status `ready` deltaP `-3.8578` edge `0.0051` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
