# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T18:52:24.175771+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7098`

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

- `market_context_high->unknown_24h` score `1598.9928` n `134` status `ready` deltaP `-5.5685` edge `133.3295` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `125.0188` n `69` status `ready` deltaP `-1.6663` edge `10.4419` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `30.816` n `134` status `ready` deltaP `0.5688` edge `2.5775` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.0004` n `57` status `ready` deltaP `24.0666` edge `0.4626` maxDD `-1.5072`
- `market_context_high->equity_24h` score `5.1197` n `134` status `ready` deltaP `16.6589` edge `0.5913` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.5686` n `134` status `ready` deltaP `35.2638` edge `0.0806` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `1.1968` n `57` status `ready` deltaP `10.3337` edge `0.0646` maxDD `-0.7008`
- `market_context_high->equity_1h` score `0.4296` n `134` status `ready` deltaP `5.6797` edge `0.0855` maxDD `-2.3383`
- `market_context_high->metal_1h` score `0.4265` n `134` status `ready` deltaP `11.5024` edge `0.0159` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.4007` n `134` status `ready` deltaP `16.1358` edge `0.0334` maxDD `-1.8344`
- `news_risk_high->crypto_alt_1h` score `0.3118` n `69` status `ready` deltaP `4.0658` edge `0.0702` maxDD `-3.3726`
- `market_context_high->commodity_4h` score `0.2269` n `134` status `ready` deltaP `13.633` edge `0.0499` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.1833` n `134` status `ready` deltaP `3.3059` edge `0.1599` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0972` n `134` status `ready` deltaP `7.6146` edge `0.0601` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0855` n `134` status `ready` deltaP `3.8788` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2996` n `134` status `ready` deltaP `1.9439` edge `0.0135` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5046` n `134` status `ready` deltaP `-0.3208` edge `-0.0027` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.5775` n `69` status `ready` deltaP `-2.4256` edge `0.0183` maxDD `-0.6872`
- `market_context_high->index_1h` score `-0.7839` n `134` status `ready` deltaP `-1.6467` edge `0.0015` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8392` n `134` status `ready` deltaP `3.2979` edge `0.0569` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
