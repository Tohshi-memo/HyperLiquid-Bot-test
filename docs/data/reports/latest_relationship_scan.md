# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T19:07:34.366898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6816`

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

- `market_context_high->unknown_24h` score `1618.1277` n `134` status `ready` deltaP `-1.4019` edge `134.8963` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `63.4378` n `134` status `ready` deltaP `6.0566` edge `5.2594` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.1572` n `134` status `ready` deltaP `26.7568` edge `0.0197` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3127` n `134` status `ready` deltaP `10.1551` edge `0.0103` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1375` n `134` status `ready` deltaP `12.2611` edge `0.0516` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0838` n `134` status `ready` deltaP `13.087` edge `0.0131` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.0777` n `134` status `ready` deltaP `4.0285` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3547` n `134` status `ready` deltaP `1.1954` edge `0.0139` maxDD `-0.4475`
- `market_context_high->crypto_major_1h` score `-0.4472` n `134` status `ready` deltaP `5.2194` edge `0.0307` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.4637` n `134` status `ready` deltaP `1.6378` edge `0.038` maxDD `-2.3383`
- `market_context_high->fx_4h` score `-0.4775` n `134` status `ready` deltaP `0.289` edge `-0.0033` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.9806` n `134` status `ready` deltaP `5.7084` edge `0.0133` maxDD `-0.9792`
- `market_context_high->index_1h` score `-0.9984` n `134` status `ready` deltaP `-3.7425` edge `-0.0024` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-1.1565` n `134` status `ready` deltaP `2.1003` edge `0.0242` maxDD `-8.251`
- `market_context_high->equity_4h` score `-1.5886` n `134` status `ready` deltaP `-2.9441` edge `-0.0256` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.692` n `134` status `ready` deltaP `3.9257` edge `0.0216` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4626` n `134` status `ready` deltaP `-7.349` edge `-0.0242` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.7876` n `134` status `ready` deltaP `4.5027` edge `-0.0579` maxDD `-19.0267`
- `market_context_high->equity_24h` score `-2.9871` n `134` status `ready` deltaP `9.1937` edge `-0.0345` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.515` n `134` status `ready` deltaP `0.7307` edge `-0.0247` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
