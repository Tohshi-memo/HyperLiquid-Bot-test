# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T19:22:23.644242+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10858`

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

- `market_context_high->equity_24h` score `1.7786` n `113` status `ready` deltaP `2.8208` edge `0.4354` maxDD `-21.1456`
- `market_context_high->metal_24h` score `1.6605` n `113` status `ready` deltaP `7.8555` edge `0.1436` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2458` n `143` status `ready` deltaP `15.6618` edge `0.0667` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8435` n `144` status `ready` deltaP `11.398` edge `0.0286` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5948` n `113` status `ready` deltaP `20.208` edge `0.0282` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.1558` n `113` status `ready` deltaP `5.7768` edge `0.1346` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.4397` n `144` status `ready` deltaP `-1.8213` edge `-0.0053` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.487` n `144` status `ready` deltaP `1.9752` edge `-0.0042` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6814` n `144` status `ready` deltaP `-4.7072` edge `-0.0064` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7294` n `143` status `ready` deltaP `2.9316` edge `-0.005` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.9598` n `143` status `ready` deltaP `-1.5254` edge `-0.0093` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.0256` n `143` status `ready` deltaP `-1.9657` edge `-0.0175` maxDD `-2.7373`
- `market_context_high->equity_1h` score `-1.0449` n `144` status `ready` deltaP `-1.5178` edge `0.0059` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-2.0535` n `144` status `ready` deltaP `-11.1069` edge `-0.0329` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6118` n `143` status `ready` deltaP `-2.0286` edge `-0.0704` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.3181` n `144` status `ready` deltaP `-12.1715` edge `-0.0629` maxDD `-7.2638`
- `market_context_high->crypto_alt_4h` score `-4.1112` n `143` status `ready` deltaP `-9.0387` edge `-0.1167` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.3817` n `113` status `ready` deltaP `0.8819` edge `-0.1216` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.0766` n `113` status `ready` deltaP `-17.5163` edge `-0.2453` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8849` n `144` status `ready` deltaP `-6.6991` edge `-0.5677` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
