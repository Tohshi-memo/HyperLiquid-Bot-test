# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T11:22:28.678752+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9175`

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

- `market_context_high->unknown_4h` score `32.1973` n `58` status `ready` deltaP `1.23` edge `2.6899` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `21.3786` n `101` status `ready` deltaP `9.0123` edge `2.4073` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `15.759` n `101` status `ready` deltaP `9.3973` edge `1.7387` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.5743` n `101` status `ready` deltaP `16.7849` edge `0.3069` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.2597` n `101` status `ready` deltaP `19.8337` edge `0.2652` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4668` n `101` status `ready` deltaP `15.1835` edge `0.1509` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8614` n `101` status `ready` deltaP `17.1296` edge `0.0932` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2682` n `101` status `ready` deltaP `23.8913` edge `0.1339` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7623` n `58` status `ready` deltaP `5.7093` edge `0.0508` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6442` n `58` status `ready` deltaP `9.8286` edge `0.0137` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5741` n `101` status `ready` deltaP `14.2986` edge `0.0127` maxDD `-0.8144`
- `news_risk_high->fx_4h` score `0.4048` n `101` status `ready` deltaP `10.7748` edge `0.0255` maxDD `-0.421`
- `market_context_high->fx_1h` score `0.3858` n `58` status `ready` deltaP `9.2247` edge `0.0063` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.2962` n `58` status `ready` deltaP `5.8487` edge `0.0165` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.2835` n `101` status `ready` deltaP `14.6598` edge `0.0313` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2467` n `58` status `ready` deltaP `13.5618` edge `0.0049` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1633` n `101` status `ready` deltaP `3.5913` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3125` n `101` status `ready` deltaP `1.3221` edge `0.0057` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.3728` n `58` status `ready` deltaP `2.5809` edge `-0.0026` maxDD `-0.6588`
- `market_context_high->crypto_major_1h` score `-0.4236` n `58` status `ready` deltaP `-2.6894` edge `0.0545` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
