# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T08:07:19.872353+00:00`
- Price records: `672`
- Market context records: `1927`
- Flow alert records: `7446`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7534`

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

- `market_context_high->crypto_alt_4h` score `7.4994` n `206` status `ready` deltaP `23.5821` edge `0.5822` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.0037` n `206` status `ready` deltaP `28.7015` edge `0.5169` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.6369` n `206` status `ready` deltaP `17.2153` edge `0.3907` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2997` n `206` status `ready` deltaP `14.3234` edge `0.2056` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.6828` n `218` status `ready` deltaP `8.1168` edge `0.1014` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.6364` n `196` status `ready` deltaP `13.9916` edge `0.4918` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.4882` n `218` status `ready` deltaP `7.0881` edge `0.1048` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3678` n `196` status `ready` deltaP `12.2626` edge `0.1915` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.2935` n `206` status `ready` deltaP `9.0235` edge `0.0732` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.1946` n `196` status `ready` deltaP `4.2233` edge `0.1109` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1949` n `218` status `ready` deltaP `4.4608` edge `0.0334` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2405` n `196` status `ready` deltaP `10.1793` edge `0.017` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6645` n `218` status `ready` deltaP `-3.3703` edge `0.0005` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6653` n `218` status `ready` deltaP `-0.0247` edge `0.0079` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6672` n `218` status `ready` deltaP `4.7465` edge `0.0164` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.8899` n `206` status `ready` deltaP `-3.7148` edge `-0.0005` maxDD `-1.1056`
- `market_context_high->metal_4h` score `-0.9873` n `206` status `ready` deltaP `9.9011` edge `0.1209` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.2281` n `218` status `ready` deltaP `1.9118` edge `-0.0199` maxDD `-3.6151`
- `market_context_high->equity_24h` score `-1.3218` n `196` status `ready` deltaP `6.7638` edge `0.3346` maxDD `-33.1875`
- `market_context_high->commodity_1h` score `-2.0004` n `218` status `ready` deltaP `1.0864` edge `-0.0079` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
