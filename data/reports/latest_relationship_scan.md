# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T14:22:40.308395+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6938`

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

- `market_context_high->unknown_24h` score `1617.6355` n `134` status `ready` deltaP `-2.9644` edge `134.8657` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `197.2748` n `51` status `ready` deltaP `-0.8512` edge `16.4578` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.0102` n `134` status `ready` deltaP `1.6359` edge `2.6699` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `8.3865` n `39` status `ready` deltaP `24.8163` edge `0.5681` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.4162` n `134` status `ready` deltaP `35.2638` edge `0.0679` maxDD `-0.1315`
- `market_context_high->equity_24h` score `3.2273` n `134` status `ready` deltaP `16.6589` edge `0.4336` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `0.3989` n `51` status `ready` deltaP `5.7708` edge `0.0746` maxDD `-2.9541`
- `market_context_high->metal_1h` score `0.3945` n `134` status `ready` deltaP `11.0533` edge `0.0148` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3434` n `134` status `ready` deltaP `15.6785` edge `0.0291` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2198` n `134` status `ready` deltaP `4.9312` edge `0.073` maxDD `-2.3383`
- `news_risk_high->commodity_4h` score `0.1904` n `39` status `ready` deltaP `0.6996` edge `0.0535` maxDD `-0.7008`
- `market_context_high->commodity_4h` score `0.1675` n `134` status `ready` deltaP `13.1757` edge `0.048` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.1283` n `134` status `ready` deltaP `7.7643` edge `0.0617` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0512` n `134` status `ready` deltaP `4.4776` edge `-0.0006` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.1008` n `134` status `ready` deltaP `3.001` edge `0.1255` maxDD `-6.008`
- `news_risk_high->index_1h` score `-0.3304` n `51` status `ready` deltaP `4.6172` edge `-0.0038` maxDD `-0.5475`
- `market_context_high->commodity_1h` score `-0.3415` n `134` status `ready` deltaP `1.4948` edge `0.013` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5085` n `134` status `ready` deltaP `-0.3208` edge `-0.0032` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8142` n `134` status `ready` deltaP `3.2979` edge `0.0601` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8462` n `134` status `ready` deltaP `-2.2455` edge `0.0003` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
