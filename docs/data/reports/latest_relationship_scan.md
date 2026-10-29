# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T22:22:26.324493+00:00`
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

- `market_context_high->unknown_24h` score `1611.0225` n `134` status `ready` deltaP `-2.6172` edge `134.3123` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `59.2134` n `134` status `ready` deltaP `5.7517` edge `4.9094` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.4266` n `134` status `ready` deltaP `29.0138` edge `0.0271` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2956` n `134` status `ready` deltaP `9.8557` edge `0.0101` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.0586` n `134` status `ready` deltaP `12.7822` edge `0.0119` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0526` n `134` status `ready` deltaP `11.4989` edge `0.0496` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1189` n `134` status `ready` deltaP `3.28` edge `-0.0013` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.2229` n `134` status `ready` deltaP `5.6685` edge `0.0464` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.2514` n `134` status `ready` deltaP `2.3863` edge `0.0507` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3715` n `134` status `ready` deltaP `1.0457` edge `0.0135` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5654` n `134` status `ready` deltaP `-1.2354` edge `-0.0044` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.9327` n `134` status `ready` deltaP `2.6991` edge `0.0489` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9385` n `134` status `ready` deltaP `-3.1437` edge `-0.0014` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.196` n `134` status `ready` deltaP `3.4515` edge `0.0104` maxDD `-0.9792`
- `market_context_high->equity_4h` score `-1.2117` n `134` status `ready` deltaP `-1.8771` edge `0.0156` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6132` n `134` status `ready` deltaP `3.9257` edge `0.0317` maxDD `-10.5088`
- `market_context_high->equity_24h` score `-1.7445` n `134` status `ready` deltaP `11.4506` edge `0.054` maxDD `-14.0571`
- `market_context_high->crypto_major_4h` score `-2.3209` n `134` status `ready` deltaP `5.7222` edge `-0.0062` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.3583` n `134` status `ready` deltaP `-6.4343` edge `-0.0216` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.276` n `134` status `ready` deltaP `2.9877` edge `-0.0091` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
