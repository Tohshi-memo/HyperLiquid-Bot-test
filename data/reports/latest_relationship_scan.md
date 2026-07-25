# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T03:37:29.866907+00:00`
- Price records: `672`
- Market context records: `7840`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `10.0746` n `132` status `ready` deltaP `28.5507` edge `0.7834` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3425` n `133` status `ready` deltaP `5.792` edge `0.3248` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.1524` n `133` status `ready` deltaP `10.5915` edge `0.2345` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0921` n `133` status `ready` deltaP `13.3076` edge `0.0464` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0797` n `133` status `ready` deltaP `13.7367` edge `0.1702` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `0.9249` n `132` status `ready` deltaP `19.3834` edge `0.1062` maxDD `-7.0012`
- `market_context_high->fx_24h` score `0.8304` n `132` status `ready` deltaP `25.2187` edge `0.0471` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7562` n `133` status `ready` deltaP `8.1961` edge `0.0943` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.7116` n `133` status `ready` deltaP `7.7423` edge `0.1194` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.4637` n `133` status `ready` deltaP `8.6098` edge `0.0406` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3626` n `133` status `ready` deltaP `8.4943` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2659` n `133` status `ready` deltaP `5.0268` edge `0.0319` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1002` n `133` status `ready` deltaP `6.0975` edge `0.0136` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0666` n `133` status `ready` deltaP `12.8521` edge `0.0516` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3846` n `133` status `ready` deltaP `0.9743` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8255` n `133` status `ready` deltaP `1.7165` edge `0.0201` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2354` n `132` status `ready` deltaP `-5.3136` edge `0.0873` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.3859` n `133` status `ready` deltaP `1.9003` edge `0.0773` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.431` n `133` status `ready` deltaP `-3.2443` edge `0.001` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-2.0014` n `133` status `ready` deltaP `14.9164` edge `0.1735` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
