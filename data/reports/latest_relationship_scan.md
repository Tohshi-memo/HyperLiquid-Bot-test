# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T00:37:29.926791+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1638.563` n `134` status `ready` deltaP `-2.7908` edge `136.6085` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `44.8302` n `134` status `ready` deltaP `5.7517` edge `3.7108` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.6224` n `134` status `ready` deltaP `30.5763` edge `0.033` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2894` n `134` status `ready` deltaP `9.706` edge `0.0103` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1303` n `134` status `ready` deltaP `12.2611` edge `0.051` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0531` n `134` status `ready` deltaP `12.6297` edge `0.0122` maxDD `-1.8344`
- `market_context_high->crypto_major_1h` score `0.0181` n `134` status `ready` deltaP `6.7164` edge `0.0595` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1532` n `134` status `ready` deltaP `2.6812` edge `-0.0017` maxDD `-0.1986`
- `market_context_high->equity_1h` score `-0.1603` n `134` status `ready` deltaP `2.8354` edge `0.0553` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3571` n `134` status `ready` deltaP `1.1954` edge `0.0137` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.6081` n `134` status `ready` deltaP `-1.9976` edge `-0.0048` maxDD `-0.4545`
- `market_context_high->equity_24h` score `-0.7111` n `134` status `ready` deltaP `13.0131` edge `0.1297` maxDD `-14.0571`
- `market_context_high->crypto_alt_1h` score `-0.7659` n `134` status `ready` deltaP `3.5973` edge `0.0643` maxDD `-8.251`
- `market_context_high->equity_4h` score `-0.7995` n `134` status `ready` deltaP `-0.5051` edge `0.0593` maxDD `-6.008`
- `market_context_high->index_1h` score `-0.9121` n `134` status `ready` deltaP `-2.8443` edge `-0.0012` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.3474` n `134` status `ready` deltaP `1.889` edge `0.0082` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5625` n `134` status `ready` deltaP `3.9257` edge `0.0382` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.8089` n `134` status `ready` deltaP `7.0941` edge `0.0503` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.2345` n `134` status `ready` deltaP `-5.3673` edge `-0.0184` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.1042` n `134` status `ready` deltaP `4.5502` edge `0.0025` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
