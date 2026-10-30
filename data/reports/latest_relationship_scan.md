# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T10:52:30.433953+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7046`

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

- `market_context_high->unknown_24h` score `1787.4458` n `134` status `ready` deltaP `-2.7908` edge `149.0154` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `246.4735` n `37` status `ready` deltaP `-3.3419` edge `20.5743` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.4523` n `134` status `ready` deltaP `3.6176` edge `2.8602` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.1314` n `134` status `ready` deltaP `33.3541` edge `0.0569` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `2.1145` n `37` status `ready` deltaP `13.6511` edge `0.1269` maxDD `-1.669`
- `market_context_high->equity_24h` score `2.0296` n `134` status `ready` deltaP `16.3117` edge `0.3361` maxDD `-14.0571`
- `news_risk_high->index_1h` score `0.5432` n `37` status `ready` deltaP `14.873` edge `-0.0002` maxDD `-0.3451`
- `market_context_high->metal_1h` score `0.3595` n `134` status `ready` deltaP `10.6042` edge `0.0133` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2917` n `134` status `ready` deltaP `15.3736` edge `0.0245` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1117` n `134` status `ready` deltaP `12.7184` edge `0.0464` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.0915` n `134` status `ready` deltaP `4.1827` edge `0.0673` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0251` n `134` status `ready` deltaP `6.7164` edge `0.0559` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1213` n `134` status `ready` deltaP `3.28` edge `-0.0016` maxDD `-0.1986`
- `news_risk_high->commodity_1h` score `-0.1913` n `37` status `ready` deltaP `-3.605` edge `0.0297` maxDD `-0.4158`
- `market_context_high->commodity_1h` score `-0.3727` n `134` status `ready` deltaP `1.1954` edge `0.0124` maxDD `-0.4475`
- `news_risk_high->fx_1h` score `-0.3799` n `37` status `ready` deltaP `0.1538` edge `0.0017` maxDD `-0.1142`
- `market_context_high->equity_4h` score `-0.445` n `134` status `ready` deltaP `0.8668` edge `0.0956` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.6176` n `134` status `ready` deltaP `-2.15` edge `-0.005` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8625` n `134` status `ready` deltaP `2.6991` edge `0.0579` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8881` n `134` status `ready` deltaP `-2.6946` edge `-0.0002` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
