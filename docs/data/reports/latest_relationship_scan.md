# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T17:55:16.037879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7074`

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

- `market_context_high->unknown_24h` score `1602.7839` n `134` status `ready` deltaP `-4.8741` edge `133.6408` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `132.1785` n `65` status `ready` deltaP `-2.3193` edge `11.0429` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.239` n `134` status `ready` deltaP `1.0261` edge `2.6097` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.4297` n `53` status `ready` deltaP `24.5571` edge `0.4951` maxDD `-1.5072`
- `market_context_high->equity_24h` score `4.6553` n `134` status `ready` deltaP `16.6589` edge `0.5526` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.5278` n `134` status `ready` deltaP `35.2638` edge `0.0772` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `1.0981` n `53` status `ready` deltaP `8.8904` edge `0.066` maxDD `-0.7008`
- `news_risk_high->crypto_alt_1h` score `0.995` n `65` status `ready` deltaP `7.0981` edge `0.1067` maxDD `-3.3547`
- `market_context_high->metal_1h` score `0.4148` n `134` status `ready` deltaP `11.3527` edge `0.0154` maxDD `-0.3659`
- `market_context_high->equity_1h` score `0.4104` n `134` status `ready` deltaP `5.6797` edge `0.0839` maxDD `-2.3383`
- `market_context_high->metal_4h` score `0.3937` n `134` status `ready` deltaP `16.1358` edge `0.0325` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.2027` n `134` status `ready` deltaP `13.4806` edge `0.0489` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.0983` n `134` status `ready` deltaP `3.3059` edge `0.149` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.084` n `134` status `ready` deltaP `7.6146` edge `0.059` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0855` n `134` status `ready` deltaP `3.8788` edge `-0.001` maxDD `-0.1986`
- `news_risk_high->commodity_1h` score `-0.3299` n `65` status `ready` deltaP `-0.1704` edge `0.0239` maxDD `-0.6872`
- `market_context_high->commodity_1h` score `-0.3571` n `134` status `ready` deltaP `1.3451` edge `0.0127` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4958` n `134` status `ready` deltaP `-0.1683` edge `-0.0026` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.7875` n `134` status `ready` deltaP `-1.6467` edge `0.0012` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8368` n `134` status `ready` deltaP `3.2979` edge `0.0572` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
