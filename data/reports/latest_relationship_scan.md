# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T09:07:34.000413+00:00`
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

- `market_context_high->unknown_4h` score `33.1729` n `58` status `ready` deltaP `1.23` edge `2.7712` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `22.706` n `101` status `ready` deltaP `10.5748` edge `2.5075` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `17.3768` n `101` status `ready` deltaP `10.9598` edge `1.8631` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.0837` n `101` status `ready` deltaP `18.1568` edge `0.3402` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7455` n `101` status `ready` deltaP `20.5958` edge `0.3006` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6047` n `101` status `ready` deltaP `15.7823` edge `0.1584` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9813` n `101` status `ready` deltaP `17.7284` edge `0.0992` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1412` n `101` status `ready` deltaP `23.0232` edge `0.1234` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.8115` n `58` status `ready` deltaP `6.1584` edge `0.0519` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6789` n `58` status `ready` deltaP `10.2777` edge `0.0136` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5034` n `101` status `ready` deltaP `13.5501` edge `0.0118` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3594` n `58` status `ready` deltaP `8.9253` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3249` n `101` status `ready` deltaP `15.1171` edge `0.0317` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2932` n `58` status `ready` deltaP `14.1716` edge `0.0068` maxDD `-1.0949`
- `news_risk_high->fx_4h` score `0.2795` n `101` status `ready` deltaP `9.4029` edge `0.0242` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2255` n `58` status `ready` deltaP `5.1002` edge `0.0156` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1897` n `101` status `ready` deltaP `3.2919` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.2634` n `101` status `ready` deltaP `1.7712` edge `0.0068` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.3037` n `58` status `ready` deltaP `-2.0906` edge `0.0605` maxDD `-2.7494`
- `market_context_high->fx_4h` score `-0.4543` n `58` status `ready` deltaP `1.209` edge `-0.0039` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
