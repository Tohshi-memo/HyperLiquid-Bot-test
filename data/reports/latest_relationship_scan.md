# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T15:22:29.977642+00:00`
- Price records: `672`
- Market context records: `8526`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6280.1565` n `52` status `ready` deltaP `44.7383` edge `523.0902` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6624` n `64` status `ready` deltaP `21.2652` edge `0.3898` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0447` n `64` status `ready` deltaP `16.8064` edge `0.0774` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7338` n `64` status `ready` deltaP `15.9525` edge `0.0858` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.902` n `64` status `ready` deltaP `6.1357` edge `0.1523` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8331` n `64` status `ready` deltaP `14.939` edge `0.1464` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5162` n `64` status `ready` deltaP `9.0101` edge `0.0588` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3275` n `64` status `ready` deltaP `6.4652` edge `0.0501` maxDD `-2.0972`
- `market_context_high->crypto_alt_4h` score `0.2139` n `42` status `ready` deltaP `4.82` edge `0.091` maxDD `-5.323`
- `news_risk_high->fx_1h` score `0.1142` n `64` status `ready` deltaP `5.7354` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0762` n `64` status `ready` deltaP `3.0869` edge `0.0368` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0535` n `64` status `ready` deltaP `4.3694` edge `0.0094` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0302` n `64` status `ready` deltaP `11.471` edge `0.0218` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0868` n `64` status `ready` deltaP `3.7051` edge `0.0084` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.1153` n `54` status `ready` deltaP `5.9492` edge `0.0081` maxDD `-2.0038`
- `market_context_high->commodity_4h` score `-0.4132` n `42` status `ready` deltaP `7.68` edge `0.0473` maxDD `-5.4508`
- `market_context_high->metal_1h` score `-0.5208` n `54` status `ready` deltaP `-0.693` edge `-0.0127` maxDD `-1.6224`
- `market_context_high->fx_4h` score `-0.6857` n `42` status `ready` deltaP `0.3847` edge `-0.0024` maxDD `-0.9178`
- `market_context_high->crypto_major_4h` score `-0.7006` n `42` status `ready` deltaP `0.7042` edge `0.0298` maxDD `-6.9453`
- `market_context_high->crypto_alt_1h` score `-0.9108` n `54` status `ready` deltaP `-8.0617` edge `-0.0003` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
