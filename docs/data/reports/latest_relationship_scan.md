# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T03:07:24.854453+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7114`

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

- `market_context_high->unknown_24h` score `1585.3574` n `134` status `ready` deltaP `-5.2213` edge `132.1909` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `127.1978` n `94` status `ready` deltaP `-2.7679` edge `10.6469` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.4238` n `134` status `ready` deltaP `1.0261` edge `3.3751` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.932` n `88` status `ready` deltaP `25.887` edge `0.5545` maxDD `-3.6198`
- `market_context_high->equity_24h` score `7.3007` n `134` status `ready` deltaP `18.9159` edge `0.758` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.9063` n `134` status `ready` deltaP `37.5207` edge `0.0937` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.5059` n `94` status `ready` deltaP `11.1893` edge `0.1338` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4074` n `134` status `ready` deltaP `15.005` edge `0.0558` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3938` n `134` status `ready` deltaP `11.0533` edge `0.0147` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3335` n `134` status `ready` deltaP `15.0688` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2294` n `134` status `ready` deltaP `4.6318` edge `0.0758` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0372` n `134` status `ready` deltaP `7.3152` edge `0.0509` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0608` n `134` status `ready` deltaP `1.4766` edge `0.1408` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1088` n `134` status `ready` deltaP `3.4297` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2182` n `134` status `ready` deltaP `2.8421` edge `0.0143` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4721` n `134` status `ready` deltaP `0.289` edge `-0.0026` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6359` n `134` status `ready` deltaP `3.9257` edge `0.157` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.7947` n `134` status `ready` deltaP `-1.6467` edge `0.0006` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8817` n `94` status `ready` deltaP `1.5448` edge `-0.0038` maxDD `-1.3981`
- `news_risk_high->commodity_1h` score `-0.9466` n `94` status `ready` deltaP `-8.5425` edge `0.002` maxDD `-1.9789`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
