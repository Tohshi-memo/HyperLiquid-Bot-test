# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T09:22:30.772897+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9168`

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

- `market_context_high->unknown_4h` score `33.0361` n `58` status `ready` deltaP `1.23` edge `2.7598` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `22.5721` n `101` status `ready` deltaP `10.4012` edge `2.4975` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `17.2165` n `101` status `ready` deltaP `10.7862` edge `1.8509` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.0307` n `101` status `ready` deltaP `18.0044` edge `0.3368` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7023` n `101` status `ready` deltaP `20.5958` edge `0.297` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5879` n `101` status `ready` deltaP `15.7823` edge `0.157` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9621` n `101` status `ready` deltaP `17.7284` edge `0.0976` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1482` n `101` status `ready` deltaP `23.0232` edge `0.1243` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8115` n `58` status `ready` deltaP `6.1584` edge `0.0519` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6789` n `58` status `ready` deltaP `10.2777` edge `0.0136` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5046` n `101` status `ready` deltaP `13.5501` edge `0.0119` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3714` n `58` status `ready` deltaP `9.075` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3261` n `101` status `ready` deltaP `15.1171` edge `0.0318` maxDD `-2.0994`
- `news_risk_high->fx_4h` score `0.2941` n `101` status `ready` deltaP `9.5553` edge `0.0244` maxDD `-0.421`
- `market_context_high->index_4h` score `0.2917` n `58` status `ready` deltaP `14.1716` edge `0.0066` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2267` n `58` status `ready` deltaP `5.1002` edge `0.0157` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1777` n `101` status `ready` deltaP `3.4416` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2634` n `101` status `ready` deltaP `1.7712` edge `0.0068` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.3229` n `58` status `ready` deltaP `-2.0906` edge `0.0589` maxDD `-2.7494`
- `market_context_high->fx_4h` score `-0.4448` n `58` status `ready` deltaP `1.3614` edge `-0.0037` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
