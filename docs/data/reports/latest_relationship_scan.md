# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T19:37:20.011658+00:00`
- Price records: `672`
- Market context records: `1969`
- Flow alert records: `7561`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7583`

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

- `market_context_high->crypto_alt_4h` score `7.328` n `234` status `ready` deltaP `22.5649` edge `0.5747` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7422` n `234` status `ready` deltaP `26.1987` edge `0.5118` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4169` n `234` status `ready` deltaP `13.5906` edge `0.3132` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.3514` n `234` status `ready` deltaP `14.8205` edge `0.2066` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.4773` n `199` status `ready` deltaP `16.7627` edge `0.5434` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.1567` n `199` status `ready` deltaP `14.3844` edge `0.2431` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `1.0112` n `234` status `ready` deltaP `9.4017` edge `0.1202` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.8399` n `234` status `ready` deltaP `8.5445` edge `0.1244` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.6581` n `199` status `ready` deltaP `13.0628` edge `0.4576` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3925` n `199` status `ready` deltaP `4.1922` edge `0.1276` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.2442` n `234` status `ready` deltaP `8.2878` edge `0.074` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0203` n `234` status `ready` deltaP `5.5479` edge `0.0407` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2` n `199` status `ready` deltaP `10.446` edge `0.0186` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.5705` n `234` status `ready` deltaP `0.7844` edge `0.0104` maxDD `-1.7205`
- `market_context_high->crypto_major_24h` score `-0.5799` n `199` status `ready` deltaP `17.6043` edge `0.6929` maxDD `-62.3533`
- `market_context_high->fx_1h` score `-0.6849` n `234` status `ready` deltaP `-3.612` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1183` n `234` status `ready` deltaP `-7.6871` edge `-0.0033` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.2257` n `234` status `ready` deltaP `3.6965` edge `0.0068` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.5803` n `234` status `ready` deltaP `0.5093` edge `-0.0399` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.8877` n `234` status `ready` deltaP `2.1585` edge `-0.0006` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
