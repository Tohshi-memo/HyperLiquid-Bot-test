# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T09:37:27.683683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11286`

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

- `market_context_high->unknown_1h` score `84.7966` n `47` status `ready` deltaP `8.3196` edge `7.018` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2153` n `47` status `ready` deltaP `30.9434` edge `4.0176` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.1988` n `47` status `ready` deltaP `24.782` edge `2.556` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6707` n `47` status `ready` deltaP `34.5892` edge `1.9442` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.3865` n `111` status `ready` deltaP `3.5659` edge `0.939` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.9331` n `47` status `ready` deltaP `35.9781` edge `0.4342` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6316` n `47` status `ready` deltaP `39.225` edge `0.1483` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6792` n `47` status `ready` deltaP `30.4226` edge `0.1386` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.7321` n `47` status `ready` deltaP `31.5873` edge `0.0325` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.2104` n `47` status `ready` deltaP `15.3152` edge `0.1239` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.0092` n `47` status `ready` deltaP `9.5355` edge `0.0873` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.8935` n `47` status `ready` deltaP `11.167` edge `0.0403` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8912` n `47` status `ready` deltaP `13.8616` edge `0.0097` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.741` n `111` status `ready` deltaP `7.9814` edge `0.0996` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4841` n `47` status `ready` deltaP `10.2592` edge `0.0076` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0136` n `111` status `ready` deltaP `3.7601` edge `0.0065` maxDD `-0.3863`
- `market_context_high->metal_1h` score `0.0126` n `47` status `ready` deltaP `3.2775` edge `0.0114` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `-0.0032` n `111` status `ready` deltaP `8.3954` edge `0.0067` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0535` n `47` status `ready` deltaP `3.2552` edge `0.0556` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.0744` n `111` status `ready` deltaP `1.9664` edge `0.0281` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
