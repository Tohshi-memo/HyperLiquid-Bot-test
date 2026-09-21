# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T09:37:31.849426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9184`

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

- `market_context_high->unknown_4h` score `32.8897` n `58` status `ready` deltaP `1.23` edge `2.7476` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `22.4226` n `101` status `ready` deltaP `10.2276` edge `2.4862` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `17.049` n `101` status `ready` deltaP `10.6126` edge `1.8381` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.9705` n `101` status `ready` deltaP `17.8519` edge `0.3328` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.6471` n `101` status `ready` deltaP `20.5958` edge `0.2924` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5699` n `101` status `ready` deltaP `15.7823` edge `0.1555` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9381` n `101` status `ready` deltaP `17.7284` edge `0.0956` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.165` n `101` status `ready` deltaP `23.1968` edge `0.1253` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8127` n `58` status `ready` deltaP `6.1584` edge `0.052` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6801` n `58` status `ready` deltaP `10.2777` edge `0.0137` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5178` n `101` status `ready` deltaP `13.6998` edge `0.012` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3714` n `58` status `ready` deltaP `9.075` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3261` n `101` status `ready` deltaP `15.1171` edge `0.0318` maxDD `-2.0994`
- `news_risk_high->fx_4h` score `0.3087` n `101` status `ready` deltaP `9.7078` edge `0.0246` maxDD `-0.421`
- `market_context_high->index_4h` score `0.2901` n `58` status `ready` deltaP `14.1716` edge `0.0064` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2399` n `58` status `ready` deltaP `5.2499` edge `0.0158` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1777` n `101` status `ready` deltaP `3.4416` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2622` n `101` status `ready` deltaP `1.7712` edge `0.0069` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.3469` n `58` status `ready` deltaP `-2.0906` edge `0.0569` maxDD `-2.7494`
- `market_context_high->fx_4h` score `-0.4353` n `58` status `ready` deltaP `1.5139` edge `-0.0035` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
