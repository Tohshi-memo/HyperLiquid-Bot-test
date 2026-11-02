# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T09:52:36.046968+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4861`

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

- `news_risk_high->crypto_alt_24h` score `4.0501` n `109` status `ready` deltaP `23.6175` edge `0.7849` maxDD `-28.8484`
- `news_risk_high->crypto_alt_4h` score `1.2794` n `131` status `ready` deltaP `9.2429` edge `0.2591` maxDD `-8.5356`
- `news_risk_high->crypto_alt_1h` score `-0.3279` n `143` status `ready` deltaP `2.3471` edge `0.0513` maxDD `-4.719`
- `news_risk_high->fx_1h` score `-0.5048` n `143` status `ready` deltaP `1.1495` edge `-0.0023` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.6815` n `143` status `ready` deltaP `-0.1486` edge `-0.0064` maxDD `-1.3981`
- `news_risk_high->metal_24h` score `-0.8784` n `109` status `ready` deltaP `12.8823` edge `0.1271` maxDD `-14.0483`
- `news_risk_high->metal_1h` score `-1.2334` n `143` status `ready` deltaP `-4.1006` edge `-0.0086` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.3854` n `131` status `ready` deltaP `-5.7229` edge `-0.0143` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-2.243` n `131` status `ready` deltaP `-4.3451` edge `-0.0285` maxDD `-4.0745`
- `news_risk_high->fx_24h` score `-2.4538` n `109` status `ready` deltaP `-18.363` edge `-0.0213` maxDD `-2.336`
- `news_risk_high->commodity_1h` score `-2.5004` n `143` status `ready` deltaP `-9.7421` edge `-0.0068` maxDD `-3.263`
- `news_risk_high->metal_4h` score `-2.8179` n `131` status `ready` deltaP `-1.9165` edge `-0.028` maxDD `-9.3056`
- `news_risk_high->equity_1h` score `-2.9598` n `143` status `ready` deltaP `-7.7918` edge `-0.0599` maxDD `-16.4088`
- `news_risk_high->crypto_major_1h` score `-3.2216` n `143` status `ready` deltaP `-8.042` edge `-0.0423` maxDD `-9.4709`
- `news_risk_high->index_24h` score `-3.3523` n `109` status `ready` deltaP `-15.0883` edge `-0.045` maxDD `-7.402`
- `news_risk_high->commodity_4h` score `-3.7741` n `131` status `ready` deltaP `-12.4477` edge `-0.0144` maxDD `-8.0364`
- `news_risk_high->equity_24h` score `-6.42` n `109` status `ready` deltaP `3.3337` edge `0.1642` maxDD `-67.0937`
- `news_risk_high->crypto_major_24h` score `-7.0152` n `109` status `ready` deltaP `-19.626` edge `-0.165` maxDD `-36.9504`
- `news_risk_high->crypto_major_4h` score `-7.1535` n `131` status `ready` deltaP `-13.6625` edge `-0.1031` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-8.5604` n `131` status `ready` deltaP `-3.5829` edge `-0.2375` maxDD `-52.2214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
