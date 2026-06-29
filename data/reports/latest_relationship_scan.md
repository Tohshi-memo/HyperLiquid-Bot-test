# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T18:37:37.312980+00:00`
- Price records: `672`
- Market context records: `5170`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `27.7418` n `69` status `ready` deltaP `32.7446` edge `2.1125` maxDD `-0.8515`
- `market_context_high->crypto_alt_24h` score `8.1437` n `69` status `ready` deltaP `22.0864` edge `0.8701` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `6.0131` n `145` status `ready` deltaP `20.4468` edge `0.467` maxDD `-5.5109`
- `market_context_high->crypto_major_24h` score `5.6122` n `69` status `ready` deltaP `20.5163` edge `0.9489` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.9198` n `145` status `ready` deltaP `15.2702` edge `0.4681` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4339` n `145` status `ready` deltaP `14.1958` edge `0.5041` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `3.2594` n `152` status `ready` deltaP `10.1048` edge `0.2684` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.0883` n `145` status `ready` deltaP `8.9329` edge `0.195` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.7551` n `152` status `ready` deltaP `7.8711` edge `0.135` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.687` n `152` status `ready` deltaP `5.0859` edge `0.1195` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.3061` n `152` status `ready` deltaP `7.9853` edge `0.0688` maxDD `-5.0555`
- `market_context_high->commodity_24h` score `0.1876` n `69` status `ready` deltaP `14.855` edge `0.1117` maxDD `-8.2675`
- `market_context_high->index_1h` score `-0.0249` n `152` status `ready` deltaP `5.2041` edge `0.0136` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0278` n `152` status `ready` deltaP `5.5074` edge `0.0189` maxDD `-2.0682`
- `market_context_high->metal_24h` score `-0.1205` n `69` status `ready` deltaP `-2.3702` edge `0.1945` maxDD `-8.5317`
- `market_context_high->fx_1h` score `-0.2371` n `152` status `ready` deltaP `2.1825` edge `0.0003` maxDD `-0.6194`
- `market_context_high->fx_24h` score `-0.2976` n `69` status `ready` deltaP `7.9257` edge `0.0119` maxDD `-0.8294`
- `market_context_high->index_4h` score `-0.5023` n `145` status `ready` deltaP `5.3826` edge `0.034` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.524` n `145` status `ready` deltaP `4.3524` edge `0.0072` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5607` n `152` status `ready` deltaP `1.2567` edge `0.0006` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
