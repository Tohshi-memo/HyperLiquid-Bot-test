# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T16:37:26.170746+00:00`
- Price records: `672`
- Market context records: `3091`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `17.2099` n `84` status `ready` deltaP `13.5416` edge `2.5573` maxDD `-26.6275`
- `market_context_high->commodity_24h` score `15.1319` n `84` status `ready` deltaP `45.3621` edge `1.0014` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.7301` n `84` status `ready` deltaP `22.9911` edge `1.1207` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.1124` n `84` status `ready` deltaP `35.6151` edge `0.9533` maxDD `-11.5093`
- `market_context_high->equity_24h` score `9.1789` n `84` status `ready` deltaP `22.0238` edge `1.4644` maxDD `-30.0893`
- `market_context_high->commodity_4h` score `2.9521` n `118` status `ready` deltaP `17.7165` edge `0.1737` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.5301` n `118` status `ready` deltaP `4.5964` edge `0.1007` maxDD `-2.9732`
- `market_context_high->commodity_1h` score `-0.1029` n `125` status `ready` deltaP `1.303` edge `0.025` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4838` n `125` status `ready` deltaP `4.1473` edge `0.0166` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6925` n `125` status `ready` deltaP `-7.5018` edge `-0.0015` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7687` n `125` status `ready` deltaP `3.6467` edge `0.0901` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.8833` n `84` status `ready` deltaP `2.4057` edge `-0.0044` maxDD `-0.4862`
- `market_context_high->equity_1h` score `-1.2353` n `125` status `ready` deltaP `-1.4994` edge `0.0002` maxDD `-8.8863`
- `market_context_high->crypto_major_1h` score `-1.332` n `125` status `ready` deltaP `-0.012` edge `0.0556` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.3808` n `118` status `ready` deltaP `-12.9676` edge `-0.0062` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4491` n `118` status `ready` deltaP `9.3039` edge `0.0431` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.2756` n `125` status `ready` deltaP `-6.0096` edge `-0.0102` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-3.0507` n `125` status `ready` deltaP `1.3078` edge `-0.0785` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.3719` n `118` status `ready` deltaP `15.957` edge `0.2658` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.9058` n `118` status `ready` deltaP `7.3222` edge `-0.0257` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
