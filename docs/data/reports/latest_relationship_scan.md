# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T04:22:28.467464+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6624`

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

- `market_context_high->unknown_24h` score `1693.2278` n `134` status `ready` deltaP `-2.7908` edge `141.1639` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `35.9667` n `134` status `ready` deltaP `4.5322` edge `2.9803` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.903` n `134` status `ready` deltaP `32.6596` edge `0.0425` maxDD `-0.1315`
- `market_context_high->equity_24h` score `0.684` n `134` status `ready` deltaP `15.6173` edge `0.2286` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3065` n `134` status `ready` deltaP `9.8557` edge `0.0115` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1695` n `134` status `ready` deltaP `13.8492` edge `0.019` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1307` n `134` status `ready` deltaP `12.566` edge `0.049` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.0695` n `134` status `ready` deltaP `6.5667` edge `0.0532` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.092` n `134` status `ready` deltaP `3.1348` edge `0.059` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1096` n `134` status `ready` deltaP `3.4297` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3367` n `134` status `ready` deltaP `1.4948` edge `0.0134` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3689` n `134` status `ready` deltaP `1.4766` edge `0.1013` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.571` n `134` status `ready` deltaP `-1.3878` edge `-0.0041` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7589` n `134` status `ready` deltaP `3.5973` edge `0.0652` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9001` n `134` status `ready` deltaP `-2.8443` edge `-0.0002` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.4447` n `134` status `ready` deltaP `3.9257` edge `0.0533` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.4792` n `134` status `ready` deltaP `8.6185` edge `0.0824` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.5915` n `134` status `ready` deltaP `-0.3679` edge `0.0029` maxDD `-0.9792`
- `market_context_high->index_4h` score `-1.9808` n `134` status `ready` deltaP `-3.0807` edge `-0.0125` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.8183` n `134` status `ready` deltaP `1.5563` edge `0.0876` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
