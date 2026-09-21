# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T15:52:31.874182+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10240`

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

- `market_context_high->unknown_4h` score `29.9821` n `58` status `ready` deltaP `1.23` edge `2.5053` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `18.3993` n `101` status `ready` deltaP `6.0609` edge `2.1787` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `12.4041` n `101` status `ready` deltaP `6.4459` edge `1.4788` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.5565` n `101` status `ready` deltaP `16.9373` edge `0.3044` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1927` n `101` status `ready` deltaP `19.9861` edge `0.2586` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4608` n `101` status `ready` deltaP `15.1835` edge `0.1504` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7786` n `101` status `ready` deltaP `16.6805` edge `0.0893` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.5404` n `101` status `ready` deltaP `25.1065` edge `0.1607` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7348` n `58` status `ready` deltaP `5.2602` edge `0.0515` maxDD `-0.36`
- `market_context_high->index_1h` score `0.5783` n `58` status `ready` deltaP `9.0801` edge `0.0132` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.543` n `101` status `ready` deltaP `13.8495` edge `0.0131` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3594` n `58` status `ready` deltaP `8.9253` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3149` n `101` status `ready` deltaP `14.8122` edge `0.0329` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2651` n `58` status `ready` deltaP `5.3996` edge `0.0169` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.2513` n `101` status `ready` deltaP `8.9456` edge `0.0249` maxDD `-0.421`
- `market_context_high->index_4h` score `0.2458` n `58` status `ready` deltaP `13.4094` edge `0.0058` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1897` n `101` status `ready` deltaP `3.2919` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.34` n `101` status `ready` deltaP `0.873` edge `0.0064` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.4726` n `58` status `ready` deltaP `0.7517` edge `-0.0032` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4757` n `101` status `ready` deltaP `8.7355` edge `-0.0348` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
