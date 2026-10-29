# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T21:52:30.689789+00:00`
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

- `market_context_high->unknown_24h` score `1612.2827` n `134` status `ready` deltaP `-2.2699` edge `134.415` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `60.0378` n `134` status `ready` deltaP `5.7517` edge `4.9781` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.3844` n `134` status `ready` deltaP `28.6666` edge `0.0259` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.3119` n `134` status `ready` deltaP `10.1551` edge `0.0102` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.0807` n `134` status `ready` deltaP `13.087` edge `0.0127` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.0478` n `134` status `ready` deltaP `11.4989` edge `0.0492` maxDD `-1.0837`
- `market_context_high->fx_1h` score `-0.1182` n `134` status `ready` deltaP `3.28` edge `-0.0012` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.2253` n `134` status `ready` deltaP `5.6685` edge `0.0462` maxDD `-5.2213`
- `market_context_high->equity_1h` score `-0.2742` n `134` status `ready` deltaP `2.2366` edge `0.0498` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3715` n `134` status `ready` deltaP `1.0457` edge `0.0135` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.548` n `134` status `ready` deltaP `-0.9305` edge `-0.0042` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.9514` n `134` status `ready` deltaP `2.6991` edge `0.0465` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.9516` n `134` status `ready` deltaP `-3.2934` edge `-0.0015` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.1634` n `134` status `ready` deltaP `3.7987` edge `0.0108` maxDD `-0.9792`
- `market_context_high->equity_4h` score `-1.297` n `134` status `ready` deltaP `-2.1819` edge `0.0067` maxDD `-6.008`
- `market_context_high->metal_24h` score `-1.6249` n `134` status `ready` deltaP `3.9257` edge `0.0302` maxDD `-10.5088`
- `market_context_high->equity_24h` score `-1.9667` n `134` status `ready` deltaP `11.1034` edge `0.0378` maxDD `-14.0571`
- `market_context_high->index_4h` score `-2.3765` n `134` status `ready` deltaP `-6.5868` edge `-0.0221` maxDD `-3.5621`
- `market_context_high->crypto_major_4h` score `-2.4187` n `134` status `ready` deltaP `5.4173` edge `-0.0167` maxDD `-19.0267`
- `market_context_high->commodity_24h` score `-4.3151` n `134` status `ready` deltaP `2.6405` edge `-0.0118` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
