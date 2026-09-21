# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T19:52:36.271627+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10156`

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

- `market_context_high->unknown_4h` score `28.1455` n `58` status `ready` deltaP `1.6874` edge `2.3492` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `15.3427` n `101` status `ready` deltaP `3.2831` edge `1.9425` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `9.8239` n `101` status `ready` deltaP `3.6682` edge `1.2823` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.6951` n `101` status `ready` deltaP `17.3946` edge `0.3129` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.0115` n `101` status `ready` deltaP `19.0715` edge `0.2496` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6407` n `101` status `ready` deltaP `15.932` edge `0.1604` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.0242` n `101` status `ready` deltaP `27.8843` edge `0.2042` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.9513` n `101` status `ready` deltaP `17.5787` edge `0.0977` maxDD `-2.8494`
- `market_context_high->index_24h` score `0.7976` n `41` status `ready` deltaP `-3.938` edge `0.1716` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.615` n `58` status `ready` deltaP `4.362` edge `0.0475` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.4975` n `101` status `ready` deltaP `13.4004` edge `0.0123` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4669` n `58` status `ready` deltaP `7.8825` edge `0.0119` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4097` n `58` status `ready` deltaP `9.5241` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3537` n `101` status `ready` deltaP `10.1651` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2515` n `101` status `ready` deltaP `14.05` edge `0.0327` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2195` n `58` status `ready` deltaP `4.9505` edge `0.0161` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.077` n `58` status `ready` deltaP `11.1228` edge `-0.0006` maxDD `-1.0949`
- `market_context_high->equity_24h` score `-0.0835` n `41` status `ready` deltaP `-7.931` edge `0.3219` maxDD `-17.7117`
- `market_context_high->metal_24h` score `-0.1041` n `41` status `ready` deltaP `12.2417` edge `-0.0669` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `-0.1393` n `101` status `ready` deltaP `3.8907` edge `0.0068` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
