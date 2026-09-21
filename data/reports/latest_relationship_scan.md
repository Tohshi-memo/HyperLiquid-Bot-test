# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T15:07:38.711316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8584`

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

- `market_context_high->unknown_4h` score `30.5953` n `58` status `ready` deltaP `1.23` edge `2.5564` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `18.957` n `101` status `ready` deltaP `6.5817` edge `2.2217` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `12.9593` n `101` status `ready` deltaP `6.9668` edge `1.5216` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4697` n `101` status `ready` deltaP `16.6324` edge `0.2992` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1615` n `101` status `ready` deltaP `19.9861` edge `0.256` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.4032` n `101` status `ready` deltaP `14.8841` edge `0.1476` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7475` n `101` status `ready` deltaP `16.5308` edge `0.0877` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.4642` n `101` status `ready` deltaP `24.5857` edge `0.1544` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7372` n `58` status `ready` deltaP `5.2602` edge `0.0517` maxDD `-0.36`
- `market_context_high->index_1h` score `0.5771` n `58` status `ready` deltaP `9.0801` edge `0.0131` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.5262` n `101` status `ready` deltaP `13.6998` edge `0.0127` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3834` n `58` status `ready` deltaP `9.2247` edge `0.0061` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3113` n `101` status `ready` deltaP `14.8122` edge `0.0326` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2592` n `58` status `ready` deltaP `13.5618` edge `0.0065` maxDD `-1.0949`
- `news_risk_high->fx_4h` score `0.2501` n `101` status `ready` deltaP `8.9456` edge `0.0248` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2483` n `58` status `ready` deltaP `5.2499` edge `0.0165` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1657` n `101` status `ready` deltaP `3.5913` edge `0.0066` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3376` n `101` status `ready` deltaP `0.873` edge `0.0066` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `-0.4651` n `101` status `ready` deltaP `8.9091` edge `-0.0346` maxDD `-2.4203`
- `market_context_high->fx_4h` score `-0.4734` n `58` status `ready` deltaP `0.7517` edge `-0.0033` maxDD `-0.6588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
