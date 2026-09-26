# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T11:07:30.000887+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11882`

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

- `news_risk_high->unknown_24h` score `4097.5855` n `90` status `ready` deltaP `-0.7639` edge `341.475` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.7437` n `47` status `ready` deltaP `8.4693` edge `5.7626` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.3916` n `47` status `ready` deltaP `22.4364` edge `3.839` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.077` n `47` status `ready` deltaP `19.4001` edge `2.2484` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5519` n `47` status `ready` deltaP `33.3739` edge `1.9424` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.0547` n `47` status `ready` deltaP `29.0337` edge `0.4073` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.43` n `47` status `ready` deltaP `29.1556` edge `0.1153` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7533` n `47` status `ready` deltaP `17.6018` edge `0.1539` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.6176` n `47` status `ready` deltaP `30.2154` edge `0.0321` maxDD `-0.2323`
- `news_risk_high->index_24h` score `1.8108` n `90` status `ready` deltaP `22.0834` edge `0.0607` maxDD `-2.2287`
- `market_context_high->crypto_alt_4h` score `1.4113` n `47` status `ready` deltaP `11.5172` edge `0.1076` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.2637` n `90` status `ready` deltaP `28.0208` edge `0.141` maxDD `-6.9298`
- `market_context_high->equity_1h` score `1.0374` n `47` status `ready` deltaP `11.9155` edge `0.0473` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8011` n `47` status `ready` deltaP `6.9765` edge `0.1107` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.7822` n `47` status `ready` deltaP `12.5143` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.5081` n `47` status `ready` deltaP `10.5586` edge `0.0076` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.3818` n `47` status `ready` deltaP `5.5007` edge `0.0769` maxDD `-4.5405`
- `news_risk_high->crypto_alt_24h` score `0.369` n `90` status `ready` deltaP `8.1945` edge `0.3713` maxDD `-29.2814`
- `news_risk_high->index_1h` score `0.0931` n `137` status `ready` deltaP `4.9511` edge `0.0039` maxDD `-0.3322`
- `market_context_high->metal_1h` score `0.0204` n `47` status `ready` deltaP `3.5769` edge `0.0104` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
