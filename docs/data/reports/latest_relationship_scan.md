# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T05:07:32.808678+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6618`

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

- `market_context_high->unknown_24h` score `1704.4454` n `134` status `ready` deltaP `-2.7908` edge `142.0987` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `35.5695` n `134` status `ready` deltaP `4.5322` edge `2.9472` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.9639` n `134` status `ready` deltaP `33.1804` edge `0.0441` maxDD `-0.1315`
- `market_context_high->equity_24h` score `0.9081` n `134` status `ready` deltaP `16.1381` edge `0.2438` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3182` n `134` status `ready` deltaP `10.0054` edge `0.012` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1947` n `134` status `ready` deltaP `14.1541` edge `0.0202` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1259` n `134` status `ready` deltaP `12.566` edge `0.0486` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.0827` n `134` status `ready` deltaP `6.5667` edge `0.0521` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.086` n `134` status `ready` deltaP `3.1348` edge `0.0595` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.094` n `134` status `ready` deltaP `3.7291` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3092` n `134` status `ready` deltaP `1.7942` edge `0.0137` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3478` n `134` status `ready` deltaP `1.4766` edge `0.104` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5694` n `134` status `ready` deltaP `-1.3878` edge `-0.0039` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.776` n `134` status `ready` deltaP `3.5973` edge `0.063` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9037` n `134` status `ready` deltaP `-2.8443` edge `-0.0005` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.4213` n `134` status `ready` deltaP `3.9257` edge `0.0563` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.5338` n `134` status `ready` deltaP `8.6185` edge `0.0754` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.644` n `134` status `ready` deltaP `-0.8888` edge `0.002` maxDD `-0.9792`
- `market_context_high->index_4h` score `-1.965` n `134` status `ready` deltaP `-2.9282` edge `-0.0122` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.8792` n `134` status `ready` deltaP `1.5563` edge `0.0798` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
