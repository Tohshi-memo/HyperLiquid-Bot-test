# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T12:07:26.311457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7034`

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

- `market_context_high->unknown_24h` score `1805.189` n `134` status `ready` deltaP `-2.7908` edge `150.494` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `232.8343` n `42` status `ready` deltaP `-3.7924` edge `19.4407` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.6527` n `134` status `ready` deltaP `3.0078` edge `2.7143` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `9.2489` n `30` status `ready` deltaP `26.9716` edge `0.6256` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.2187` n `134` status `ready` deltaP `33.8749` edge `0.0607` maxDD `-0.1315`
- `market_context_high->equity_24h` score `2.3956` n `134` status `ready` deltaP `16.3117` edge `0.3666` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `2.2889` n `42` status `ready` deltaP `13.8651` edge `0.14` maxDD `-1.669`
- `news_risk_high->commodity_4h` score `0.553` n `30` status `ready` deltaP `4.5528` edge `0.0743` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.3704` n `134` status `ready` deltaP `10.7539` edge `0.0137` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2956` n `134` status `ready` deltaP `15.3736` edge `0.025` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1142` n `134` status `ready` deltaP `4.3324` edge `0.0682` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.0765` n `134` status `ready` deltaP `12.4135` edge `0.0455` maxDD `-1.0837`
- `news_risk_high->metal_4h` score `0.0421` n `30` status `ready` deltaP `10.4979` edge `0.0044` maxDD `-1.5193`
- `market_context_high->crypto_major_1h` score `0.0025` n `134` status `ready` deltaP `7.0158` edge `0.0562` maxDD `-5.2213`
- `news_risk_high->index_1h` score `-0.0649` n `42` status `ready` deltaP `6.9789` edge `-0.0032` maxDD `-0.4652`
- `market_context_high->fx_1h` score `-0.1205` n `134` status `ready` deltaP `3.28` edge `-0.0015` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.3282` n `134` status `ready` deltaP `1.629` edge `0.1055` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3583` n `134` status `ready` deltaP `1.3451` edge `0.0126` maxDD `-0.4475`
- `news_risk_high->commodity_1h` score `-0.3886` n `42` status `ready` deltaP `-6.5441` edge `0.024` maxDD `-0.4158`
- `market_context_high->fx_4h` score `-0.5843` n `134` status `ready` deltaP `-1.5403` edge `-0.0048` maxDD `-0.4545`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
