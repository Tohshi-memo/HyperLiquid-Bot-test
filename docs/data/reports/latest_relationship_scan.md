# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T04:37:26.191780+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6618`

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

- `market_context_high->unknown_24h` score `1696.9406` n `134` status `ready` deltaP `-2.7908` edge `141.4733` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `35.7639` n `134` status `ready` deltaP `4.5322` edge `2.9634` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.9229` n `134` status `ready` deltaP `32.8332` edge `0.043` maxDD `-0.1315`
- `market_context_high->equity_24h` score `0.7531` n `134` status `ready` deltaP `15.7909` edge `0.2332` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3151` n `134` status `ready` deltaP `10.0054` edge `0.0116` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.1813` n `134` status `ready` deltaP `14.0017` edge `0.0195` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1307` n `134` status `ready` deltaP `12.566` edge `0.049` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.0767` n `134` status `ready` deltaP `6.5667` edge `0.0526` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.0944` n `134` status `ready` deltaP `3.1348` edge `0.0588` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1018` n `134` status `ready` deltaP `3.5794` edge `-0.0011` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3236` n `134` status `ready` deltaP `1.6445` edge `0.0135` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3564` n `134` status `ready` deltaP `1.4766` edge `0.1029` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5702` n `134` status `ready` deltaP `-1.3878` edge `-0.004` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7651` n `134` status `ready` deltaP `3.5973` edge `0.0644` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9013` n `134` status `ready` deltaP `-2.8443` edge `-0.0003` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.4369` n `134` status `ready` deltaP `3.9257` edge `0.0543` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.4987` n `134` status `ready` deltaP `8.6185` edge `0.0799` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.609` n `134` status `ready` deltaP `-0.5416` edge `0.0026` maxDD `-0.9792`
- `market_context_high->index_4h` score `-1.9662` n `134` status `ready` deltaP `-2.9282` edge `-0.0123` maxDD `-3.5621`
- `market_context_high->crypto_alt_4h` score `-3.8409` n `134` status `ready` deltaP `1.5563` edge `0.0847` maxDD `-37.0003`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
