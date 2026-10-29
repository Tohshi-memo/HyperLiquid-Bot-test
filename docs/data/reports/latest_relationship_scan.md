# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T23:22:26.413889+00:00`
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

- `market_context_high->unknown_24h` score `1620.9278` n `134` status `ready` deltaP `-2.7908` edge `135.1389` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `54.4242` n `134` status `ready` deltaP `5.7517` edge `4.5103` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.5097` n `134` status `ready` deltaP `29.7082` edge `0.0294` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.28` n `134` status `ready` deltaP `9.5563` edge `0.0101` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.0719` n `134` status `ready` deltaP `11.6513` edge `0.0502` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0404` n `134` status `ready` deltaP `12.4773` edge `0.0116` maxDD `-1.8344`
- `market_context_high->fx_1h` score `-0.1353` n `134` status `ready` deltaP `2.9806` edge `-0.0014` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1702` n `134` status `ready` deltaP `5.9679` edge `0.0488` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.2514` n `134` status `ready` deltaP `2.3863` edge `0.0507` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3439` n `134` status `ready` deltaP `1.3451` edge `0.0138` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5907` n `134` status `ready` deltaP `-1.6927` edge `-0.0046` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.9109` n `134` status `ready` deltaP `2.8488` edge `0.0507` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9397` n `134` status `ready` deltaP `-3.1437` edge `-0.0015` maxDD `-1.1344`
- `market_context_high->equity_4h` score `-1.0326` n `134` status `ready` deltaP `-1.2673` edge `0.0345` maxDD `-6.008`
- `market_context_high->fx_24h` score `-1.2611` n `134` status `ready` deltaP `2.7571` edge `0.0096` maxDD `-0.9792`
- `market_context_high->equity_24h` score `-1.3086` n `134` status `ready` deltaP `12.145` edge `0.0857` maxDD `-14.0571`
- `market_context_high->metal_24h` score `-1.5929` n `134` status `ready` deltaP `3.9257` edge `0.0343` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-2.1067` n `134` status `ready` deltaP `6.3319` edge `0.0172` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.3207` n `134` status `ready` deltaP `-6.1295` edge `-0.0205` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.1985` n `134` status `ready` deltaP `3.6821` edge `-0.0038` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
