# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-05T00:52:27.786249+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3815`

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

- `news_risk_high->crypto_alt_4h` score `-0.3072` n `146` status `ready` deltaP `6.9997` edge `0.1776` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.4855` n `146` status `ready` deltaP `2.631` edge `0.043` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7245` n `146` status `ready` deltaP `-2.9714` edge `-0.003` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.7897` n `146` status `ready` deltaP `2.3952` edge `-0.0018` maxDD `-1.3981`
- `news_risk_high->metal_1h` score `-1.4535` n `146` status `ready` deltaP `-7.3435` edge `-0.0152` maxDD `-3.1082`
- `news_risk_high->fx_4h` score `-1.5794` n `146` status `ready` deltaP `-9.6037` edge `-0.0133` maxDD `-1.6794`
- `news_risk_high->index_4h` score `-1.9634` n `146` status `ready` deltaP `-1.2926` edge `-0.013` maxDD `-4.0745`
- `news_risk_high->commodity_1h` score `-2.161` n `146` status `ready` deltaP `-7.7291` edge `0.0081` maxDD `-3.2657`
- `news_risk_high->fx_24h` score `-2.455` n `146` status `ready` deltaP `-18.8368` edge `-0.0183` maxDD `-2.336`
- `news_risk_high->index_24h` score `-2.5219` n `146` status `ready` deltaP `-9.0486` edge `0.0212` maxDD `-7.402`
- `news_risk_high->equity_1h` score `-2.562` n `146` status `ready` deltaP `-6.0372` edge `-0.0206` maxDD `-16.4088`
- `news_risk_high->commodity_4h` score `-3.2152` n `146` status `ready` deltaP `-10.036` edge `0.0344` maxDD `-9.5011`
- `news_risk_high->crypto_major_1h` score `-3.3064` n `146` status `ready` deltaP `-7.4071` edge `-0.0536` maxDD `-9.4709`
- `news_risk_high->metal_24h` score `-4.851` n `146` status `ready` deltaP `-1.0594` edge `-0.039` maxDD `-16.6552`
- `news_risk_high->metal_4h` score `-5.0853` n `146` status `ready` deltaP `-7.4528` edge `-0.0536` maxDD `-9.3056`
- `news_risk_high->crypto_major_4h` score `-7.6543` n `146` status `ready` deltaP `-12.7068` edge `-0.1512` maxDD `-24.1554`
- `news_risk_high->equity_4h` score `-11.2556` n `146` status `ready` deltaP `-0.8353` edge `-0.0963` maxDD `-52.2214`
- `news_risk_high->crypto_alt_24h` score `-11.3087` n `146` status `ready` deltaP `10.6698` edge `0.1785` maxDD `-118.6236`
- `news_risk_high->commodity_24h` score `-11.3405` n `146` status `ready` deltaP `-20.6807` edge `0.0189` maxDD `-43.7525`
- `news_risk_high->equity_24h` score `-12.2263` n `146` status `ready` deltaP `11.8809` edge `0.3523` maxDD `-102.3626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
