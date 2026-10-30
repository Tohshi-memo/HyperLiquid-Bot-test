# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T19:07:32.128454+00:00`
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

- `market_context_high->unknown_24h` score `1593.9581` n `134` status `ready` deltaP `-5.7422` edge `132.9111` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `123.0813` n `70` status `ready` deltaP `-1.4799` edge `10.2792` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `30.7872` n `134` status `ready` deltaP `0.5688` edge `2.5751` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `6.553` n `58` status `ready` deltaP `22.7659` edge `0.438` maxDD `-1.8283`
- `market_context_high->equity_24h` score `5.2313` n `134` status `ready` deltaP `16.6589` edge `0.6006` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.5782` n `134` status `ready` deltaP `35.2638` edge `0.0814` maxDD `-0.1315`
- `news_risk_high->commodity_4h` score `1.2633` n `58` status `ready` deltaP `11.0597` edge `0.0653` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.4265` n `134` status `ready` deltaP `11.5024` edge `0.0159` maxDD `-0.3659`
- `market_context_high->equity_1h` score `0.4236` n `134` status `ready` deltaP `5.6797` edge `0.085` maxDD `-2.3383`
- `market_context_high->metal_4h` score `0.4015` n `134` status `ready` deltaP `16.1358` edge `0.0335` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.2281` n `134` status `ready` deltaP `13.633` edge `0.05` maxDD `-1.0837`
- `market_context_high->equity_4h` score `0.1966` n `134` status `ready` deltaP `3.3059` edge `0.1616` maxDD `-6.008`
- `market_context_high->crypto_major_1h` score `0.0984` n `134` status `ready` deltaP `7.6146` edge `0.0602` maxDD `-5.2213`
- `news_risk_high->crypto_alt_1h` score `0.0573` n `70` status `ready` deltaP `3.3618` edge `0.0624` maxDD `-3.8643`
- `market_context_high->fx_1h` score `-0.0855` n `134` status `ready` deltaP `3.8788` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2984` n `134` status `ready` deltaP `1.9439` edge `0.0136` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5053` n `134` status `ready` deltaP `-0.3208` edge `-0.0028` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.5162` n `70` status `ready` deltaP `-1.6595` edge `0.0183` maxDD `-0.6872`
- `market_context_high->index_1h` score `-0.7839` n `134` status `ready` deltaP `-1.6467` edge `0.0015` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.8423` n `134` status `ready` deltaP `3.2979` edge `0.0565` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
