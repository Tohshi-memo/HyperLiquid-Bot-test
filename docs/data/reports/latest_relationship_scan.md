# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T17:22:28.062916+00:00`
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

- `market_context_high->unknown_24h` score `1604.5949` n `134` status `ready` deltaP `-4.5269` edge `133.7894` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `143.2829` n `63` status `ready` deltaP `-2.4594` edge `11.9692` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.3386` n `134` status `ready` deltaP `1.0261` edge `2.618` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.3315` n `51` status `ready` deltaP `23.9` edge `0.4913` maxDD `-1.5072`
- `market_context_high->equity_24h` score `4.4261` n `134` status `ready` deltaP `16.6589` edge `0.5335` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.5086` n `134` status `ready` deltaP `35.2638` edge `0.0756` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.2047` n `63` status `ready` deltaP `8.4593` edge `0.1151` maxDD `-3.3547`
- `news_risk_high->commodity_4h` score `0.9032` n `51` status `ready` deltaP `7.1886` edge `0.0611` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.3953` n `134` status `ready` deltaP `11.0533` edge `0.0149` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3819` n `134` status `ready` deltaP `15.9834` edge `0.032` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3745` n `134` status `ready` deltaP `5.53` edge `0.0819` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2051` n `134` status `ready` deltaP `13.4806` edge `0.0491` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0804` n `134` status `ready` deltaP `7.6146` edge `0.0587` maxDD `-5.2213`
- `market_context_high->equity_4h` score `0.0539` n `134` status `ready` deltaP `3.3059` edge `0.1433` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.101` n `134` status `ready` deltaP `3.5794` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3415` n `134` status `ready` deltaP `1.4948` edge `0.013` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.4709` n `63` status `ready` deltaP `-1.6325` edge `0.0219` maxDD `-0.6872`
- `market_context_high->fx_4h` score `-0.5038` n `134` status `ready` deltaP `-0.3208` edge `-0.0026` maxDD `-0.4545`
- `news_risk_high->index_1h` score `-0.7903` n `63` status `ready` deltaP `-2.7398` edge `-0.0088` maxDD `-0.9406`
- `market_context_high->index_1h` score `-0.815` n `134` status `ready` deltaP `-1.9461` edge `0.0009` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
