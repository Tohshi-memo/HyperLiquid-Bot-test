# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T17:07:27.899420+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7080`

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

- `market_context_high->unknown_24h` score `1605.7932` n `134` status `ready` deltaP `-4.3533` edge `133.8881` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `149.6323` n `62` status `ready` deltaP `-1.0769` edge `12.4891` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.4166` n `134` status `ready` deltaP `1.0261` edge `2.6245` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.3053` n `50` status `ready` deltaP `23.5427` edge `0.4915` maxDD `-1.5072`
- `market_context_high->equity_24h` score `4.3169` n `134` status `ready` deltaP `16.6589` edge `0.5244` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.499` n `134` status `ready` deltaP `35.2638` edge `0.0748` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.1657` n `62` status `ready` deltaP `7.8665` edge `0.1158` maxDD `-3.3547`
- `news_risk_high->commodity_4h` score `0.7674` n `50` status `ready` deltaP `6.2866` edge `0.0558` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.3945` n `134` status `ready` deltaP `11.0533` edge `0.0148` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3803` n `134` status `ready` deltaP `15.9834` edge `0.0318` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3661` n `134` status `ready` deltaP `5.53` edge `0.0812` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2087` n `134` status `ready` deltaP `13.4806` edge `0.0494` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0983` n `134` status `ready` deltaP `7.7643` edge `0.0592` maxDD `-5.2213`
- `market_context_high->equity_4h` score `0.0367` n `134` status `ready` deltaP `3.3059` edge `0.1411` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.101` n `134` status `ready` deltaP `3.5794` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3415` n `134` status `ready` deltaP `1.4948` edge `0.013` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.503` n `134` status `ready` deltaP `-0.3208` edge `-0.0025` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.5529` n `62` status `ready` deltaP `-2.4773` edge `0.0207` maxDD `-0.6872`
- `news_risk_high->index_1h` score `-0.7382` n `62` status `ready` deltaP `-1.9461` edge `-0.0081` maxDD `-0.8852`
- `market_context_high->index_1h` score `-0.815` n `134` status `ready` deltaP `-1.9461` edge `0.0009` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
