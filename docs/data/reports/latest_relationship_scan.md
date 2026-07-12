# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T19:52:24.979502+00:00`
- Price records: `672`
- Market context records: `6533`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `news_risk_high->crypto_alt_24h` score `13.6378` n `32` status `ready` deltaP `36.9042` edge `0.9052` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.6` n `32` status `ready` deltaP `54.4194` edge `0.1872` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3019` n `144` status `ready` deltaP `11.8934` edge `0.7759` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.966` n `32` status `ready` deltaP `21.6042` edge `0.5706` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7121` n `38` status `ready` deltaP `39.3213` edge `0.0518` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.1115` n `193` status `ready` deltaP `-6.2005` edge `0.3074` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `1.9844` n `32` status `ready` deltaP `22.1566` edge `0.0382` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.7784` n `38` status `ready` deltaP `22.3133` edge `0.0175` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.5654` n `144` status `ready` deltaP `14.1705` edge `0.2228` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7048` n `181` status `ready` deltaP `14.6206` edge `0.0289` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5808` n `38` status `ready` deltaP `5.2001` edge `0.0935` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.4063` n `181` status `ready` deltaP `10.6396` edge `0.1183` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0937` n `38` status `ready` deltaP `1.7334` edge `0.0514` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2052` n `32` status `ready` deltaP `8.2431` edge `0.0059` maxDD `-2.3058`
- `market_context_high->crypto_major_4h` score `-0.3479` n `181` status `ready` deltaP `13.6118` edge `0.0937` maxDD `-12.6576`
- `market_context_high->equity_4h` score `-0.3679` n `181` status `ready` deltaP `9.5733` edge `0.0589` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4078` n `193` status `ready` deltaP `0.0062` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.451` n `193` status `ready` deltaP `1.8592` edge `-0.0019` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.5413` n `193` status `ready` deltaP `6.3728` edge `0.0147` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.5604` n `193` status `ready` deltaP `6.0966` edge `0.0188` maxDD `-5.8368`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
