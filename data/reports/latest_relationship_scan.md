# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T18:07:31.004133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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

- `market_context_high->unknown_4h` score `28.4677` n `58` status `ready` deltaP `1.23` edge `2.3791` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `16.8511` n `101` status `ready` deltaP `4.4984` edge `2.0601` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `11.0455` n `101` status `ready` deltaP `4.8834` edge `1.376` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7287` n `101` status `ready` deltaP `17.3946` edge `0.3157` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.2369` n `101` status `ready` deltaP `19.8337` edge `0.2633` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.661` n `101` status `ready` deltaP `16.2314` edge `0.1601` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9393` n `101` status `ready` deltaP `17.5787` edge `0.0967` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.8097` n `101` status `ready` deltaP `26.669` edge `0.1848` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7264` n `58` status `ready` deltaP `5.1105` edge `0.0518` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5742` n `101` status `ready` deltaP `14.1489` edge `0.0137` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5507` n `58` status `ready` deltaP `8.7807` edge `0.0129` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4217` n `58` status `ready` deltaP `9.6738` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3415` n `101` status `ready` deltaP `10.0126` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.3257` n `101` status `ready` deltaP `14.8122` edge `0.0338` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2962` n `58` status `ready` deltaP `5.699` edge `0.0175` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.1417` n `58` status `ready` deltaP `12.0374` edge `0.0016` maxDD `-1.0949`
- `market_context_high->index_24h` score `-0.1221` n `35` status `ready` deltaP `-8.5764` edge `0.1204` maxDD `-1.644`
- `news_risk_high->fx_1h` score `-0.1274` n `101` status `ready` deltaP `4.0404` edge `0.0068` maxDD `-0.2147`
- `market_context_high->crypto_major_1h` score `-0.3456` n `58` status `ready` deltaP `-2.2403` edge `0.058` maxDD `-2.7494`
- `news_risk_high->equity_1h` score `-0.3484` n `101` status `ready` deltaP `0.7233` edge `0.0067` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
