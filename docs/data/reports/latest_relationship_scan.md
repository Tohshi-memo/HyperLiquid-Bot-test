# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T22:52:24.970686+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.1793` n `146` status `ready` deltaP `14.7552` edge `0.0672` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8756` n `158` status `ready` deltaP `11.2295` edge `0.0324` maxDD `-0.7439`
- `market_context_high->metal_24h` score `0.7567` n `125` status `ready` deltaP `4.4486` edge `0.091` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.4775` n `125` status `ready` deltaP `18.7625` edge `0.0228` maxDD `-1.9329`
- `market_context_high->equity_24h` score `0.3666` n `125` status `ready` deltaP `2.75` edge `0.3182` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.1648` n `125` status `ready` deltaP `3.3931` edge `0.1094` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5068` n `158` status `ready` deltaP `1.6676` edge `-0.0038` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.6543` n `146` status `ready` deltaP `-2.0653` edge `-0.0096` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.66` n `158` status `ready` deltaP `-4.6407` edge `-0.006` maxDD `-0.8146`
- `market_context_high->fx_4h` score `-0.7121` n `146` status `ready` deltaP `2.9674` edge `-0.0038` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7405` n `158` status `ready` deltaP `-4.5384` edge `-0.0092` maxDD `-1.438`
- `market_context_high->metal_4h` score `-1.0429` n `146` status `ready` deltaP `-2.1488` edge `-0.0185` maxDD `-2.7373`
- `market_context_high->equity_1h` score `-1.0817` n `158` status `ready` deltaP `-1.1825` edge `0.0006` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.1772` n `158` status `ready` deltaP `-8.7508` edge `-0.0284` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.645` n `146` status `ready` deltaP `-2.6833` edge `-0.0688` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.208` n `158` status `ready` deltaP `-11.1063` edge `-0.057` maxDD `-7.5698`
- `market_context_high->crypto_alt_4h` score `-4.1125` n `146` status `ready` deltaP `-9.069` edge `-0.1166` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.1173` n `125` status `ready` deltaP `2.1778` edge `-0.1082` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.8591` n `125` status `ready` deltaP `-14.1181` edge `-0.1665` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7652` n `158` status `ready` deltaP `-6.1794` edge `-0.5602` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
