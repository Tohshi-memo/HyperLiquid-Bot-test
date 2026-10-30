# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T17:37:27.888909+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7096`

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

- `market_context_high->unknown_24h` score `1603.6942` n `134` status `ready` deltaP `-4.7005` edge `133.7155` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `137.308` n `64` status `ready` deltaP `-2.3859` edge `11.4708` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.2606` n `134` status `ready` deltaP `1.0261` edge `2.6115` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.3309` n `52` status `ready` deltaP `24.2378` edge `0.489` maxDD `-1.5072`
- `market_context_high->equity_24h` score `4.5425` n `134` status `ready` deltaP `16.6589` edge `0.5432` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.5182` n `134` status `ready` deltaP `35.2638` edge `0.0764` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.0857` n `64` status `ready` deltaP `7.7657` edge `0.1098` maxDD `-3.3547`
- `news_risk_high->commodity_4h` score `1.0181` n `52` status `ready` deltaP `8.0558` edge `0.0649` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.4054` n `134` status `ready` deltaP `11.203` edge `0.0152` maxDD `-0.3659`
- `market_context_high->equity_1h` score `0.3889` n `134` status `ready` deltaP `5.53` edge `0.0831` maxDD `-2.3383`
- `market_context_high->metal_4h` score `0.3842` n `134` status `ready` deltaP `15.9834` edge `0.0323` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.2039` n `134` status `ready` deltaP `13.4806` edge `0.049` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0828` n `134` status `ready` deltaP `7.6146` edge `0.0589` maxDD `-5.2213`
- `market_context_high->equity_4h` score `0.0757` n `134` status `ready` deltaP `3.3059` edge `0.1461` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0933` n `134` status `ready` deltaP `3.7291` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3439` n `134` status `ready` deltaP `1.4948` edge `0.0128` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.3778` n `64` status `ready` deltaP `-0.814` edge `0.0242` maxDD `-0.6872`
- `market_context_high->fx_4h` score `-0.4951` n `134` status `ready` deltaP `-0.1683` edge `-0.0025` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.8007` n `134` status `ready` deltaP `-1.7964` edge `0.0011` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8402` n `64` status `ready` deltaP `-3.3589` edge `-0.0099` maxDD `-1.0344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
