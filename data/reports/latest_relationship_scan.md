# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T15:22:38.341674+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7030`

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

- `market_context_high->unknown_24h` score `1612.8238` n `134` status `ready` deltaP `-3.4852` edge `134.4682` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `166.5795` n `55` status `ready` deltaP `-0.1524` edge `13.8952` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.808` n `134` status `ready` deltaP `1.1785` edge `2.6561` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.7371` n `43` status `ready` deltaP `22.5503` edge `0.5341` maxDD `-1.5072`
- `market_context_high->equity_24h` score `3.5945` n `134` status `ready` deltaP `16.6589` edge `0.4642` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.4462` n `134` status `ready` deltaP `35.2638` edge `0.0704` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.1966` n `55` status `ready` deltaP `7.368` edge `0.1217` maxDD `-3.3547`
- `market_context_high->metal_1h` score `0.4031` n `134` status `ready` deltaP `11.203` edge `0.0149` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3733` n `134` status `ready` deltaP `15.9834` edge `0.0309` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2821` n `134` status `ready` deltaP `5.2306` edge `0.0762` maxDD `-2.3383`
- `news_risk_high->commodity_4h` score `0.2354` n `43` status `ready` deltaP `0.9713` edge `0.0469` maxDD `-0.7008`
- `market_context_high->commodity_4h` score `0.1905` n `134` status `ready` deltaP `13.3281` edge `0.0489` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0768` n `134` status `ready` deltaP `7.6146` edge `0.0584` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0436` n `134` status `ready` deltaP `3.3059` edge `0.1308` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0753` n `134` status `ready` deltaP `4.0285` edge `-0.0007` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3439` n `134` status `ready` deltaP `1.4948` edge `0.0128` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.345` n `55` status `ready` deltaP `4.2678` edge `-0.0028` maxDD `-0.5909`
- `market_context_high->fx_4h` score `-0.5046` n `134` status `ready` deltaP `-0.3208` edge `-0.0027` maxDD `-0.4545`
- `market_context_high->index_1h` score `-0.8306` n `134` status `ready` deltaP `-2.0958` edge `0.0006` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8555` n `134` status `ready` deltaP `3.1482` edge `0.0558` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
