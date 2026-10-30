# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T13:07:28.965870+00:00`
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

- `market_context_high->unknown_24h` score `1819.4594` n `134` status `ready` deltaP `-2.7908` edge `151.6832` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `205.8554` n `46` status `ready` deltaP `-2.3431` edge `17.1828` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `32.2524` n `134` status `ready` deltaP `2.3981` edge `2.685` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `9.4493` n `34` status `ready` deltaP `29.7167` edge `0.624` maxDD `-1.4402`
- `market_context_high->index_24h` score `3.315` n `134` status `ready` deltaP `34.5693` edge `0.0641` maxDD `-0.1315`
- `market_context_high->equity_24h` score `2.7479` n `134` status `ready` deltaP `16.4853` edge `0.3948` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `1.8339` n `46` status `ready` deltaP `10.863` edge `0.1221` maxDD `-1.669`
- `market_context_high->metal_1h` score `0.3844` n `134` status `ready` deltaP `10.9036` edge `0.0145` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3247` n `134` status `ready` deltaP `15.6785` edge `0.0267` maxDD `-1.8344`
- `news_risk_high->commodity_4h` score `0.305` n `34` status `ready` deltaP `1.5244` edge `0.0627` maxDD `-0.7008`
- `market_context_high->equity_1h` score `0.1346` n `134` status `ready` deltaP `4.4821` edge `0.0689` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.1117` n `134` status `ready` deltaP `12.7184` edge `0.0464` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0444` n `134` status `ready` deltaP `7.3152` edge `0.0577` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0956` n `134` status `ready` deltaP `3.7291` edge `-0.0013` maxDD `-0.1986`
- `market_context_high->equity_4h` score `-0.22` n `134` status `ready` deltaP `2.2388` edge `0.1153` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3439` n `134` status `ready` deltaP `1.4948` edge `0.0128` maxDD `-0.4475`
- `news_risk_high->index_1h` score `-0.476` n `46` status `ready` deltaP `1.9526` edge `-0.0047` maxDD `-0.5475`
- `market_context_high->fx_4h` score `-0.5487` n `134` status `ready` deltaP `-0.9305` edge `-0.0043` maxDD `-0.4545`
- `news_risk_high->metal_4h` score `-0.7317` n `34` status `ready` deltaP `4.5283` edge `-0.0243` maxDD `-2.6424`
- `news_risk_high->commodity_1h` score `-0.7472` n `46` status `ready` deltaP `-10.1211` edge `0.0123` maxDD `-0.5826`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
