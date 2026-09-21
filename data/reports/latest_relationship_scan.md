# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T18:22:32.206100+00:00`
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

- `market_context_high->unknown_4h` score `28.4617` n `58` status `ready` deltaP `1.23` edge `2.3786` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `16.662` n `101` status `ready` deltaP `4.3248` edge `2.0455` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `10.8924` n `101` status `ready` deltaP `4.7098` edge `1.3644` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7203` n `101` status `ready` deltaP `17.3946` edge `0.315` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1971` n `101` status `ready` deltaP `19.6812` edge `0.261` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6466` n `101` status `ready` deltaP `16.0817` edge `0.1599` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9333` n `101` status `ready` deltaP `17.5787` edge `0.0962` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.8374` n `101` status `ready` deltaP `26.8427` edge `0.1872` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7037` n `58` status `ready` deltaP `4.9608` edge `0.0509` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5586` n `101` status `ready` deltaP `13.9992` edge `0.0134` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5376` n `58` status `ready` deltaP `8.631` edge `0.0128` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3293` n `101` status `ready` deltaP `9.8602` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.3245` n `101` status `ready` deltaP `14.8122` edge `0.0337` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2806` n `58` status `ready` deltaP `5.5493` edge `0.0172` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.1306` n `58` status `ready` deltaP `11.885` edge `0.0012` maxDD `-1.0949`
- `market_context_high->index_24h` score `0.0015` n `36` status `ready` deltaP `-7.6389` edge `0.13` maxDD `-1.644`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`
- `market_context_high->crypto_major_1h` score `-0.3516` n `58` status `ready` deltaP `-2.2403` edge `0.0575` maxDD `-2.7494`
- `news_risk_high->equity_1h` score `-0.3712` n `101` status `ready` deltaP `0.5736` edge `0.0058` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
