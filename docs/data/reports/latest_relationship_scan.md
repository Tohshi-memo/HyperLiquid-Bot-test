# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T09:52:23.327897+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `6933`

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

- `market_context_high->unknown_4h` score `42.4959` n `85` status `ready` deltaP `-12.9484` edge `3.6857` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.3648` n `62` status `ready` deltaP `36.1783` edge `0.5821` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `6.4172` n `62` status `ready` deltaP `6.9669` edge `1.0911` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.3615` n `85` status `ready` deltaP `19.6539` edge `0.0108` maxDD `-0.2692`
- `market_context_high->index_24h` score `1.0685` n `62` status `ready` deltaP `19.03` edge `0.1168` maxDD `-1.2012`
- `market_context_high->commodity_4h` score `0.2904` n `85` status `ready` deltaP `10.2655` edge `0.0091` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.283` n `94` status `ready` deltaP `5.9976` edge `0.0087` maxDD `-0.3417`
- `market_context_high->fx_1h` score `0.0131` n `94` status `ready` deltaP `3.5705` edge `0.0021` maxDD `-0.271`
- `market_context_high->fx_24h` score `-0.2151` n `62` status `ready` deltaP `9.6774` edge `0.0131` maxDD `-1.0826`
- `market_context_high->crypto_major_1h` score `-0.4125` n `94` status `ready` deltaP `1.0798` edge `0.0288` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.6271` n `94` status `ready` deltaP `-3.3253` edge `0.0013` maxDD `-0.7626`
- `market_context_high->metal_4h` score `-0.7349` n `85` status `ready` deltaP `-5.556` edge `0.0151` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `-0.9961` n `85` status `ready` deltaP `-2.6596` edge `0.0943` maxDD `-10.6751`
- `market_context_high->crypto_alt_1h` score `-1.0535` n `94` status `ready` deltaP `-5.7364` edge `0.0191` maxDD `-4.9401`
- `market_context_high->metal_24h` score `-1.2264` n `62` status `ready` deltaP `-7.2189` edge `0.0394` maxDD `-3.5466`
- `market_context_high->index_4h` score `-1.3147` n `85` status `ready` deltaP `-11.3289` edge `0.0002` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.4191` n `94` status `ready` deltaP `-4.3891` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.4518` n `94` status `ready` deltaP `-4.1438` edge `-0.0064` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-2.2152` n `85` status `ready` deltaP `-10.434` edge `0.0414` maxDD `-13.8008`
- `market_context_high->equity_4h` score `-2.7134` n `85` status `ready` deltaP `-9.1912` edge `-0.0056` maxDD `-6.4057`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
