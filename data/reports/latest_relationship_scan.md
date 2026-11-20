# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T07:22:29.008025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2754`

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

- `market_context_high->unknown_1h` score `11998.4132` n `108` status `ready` deltaP `1.1367` edge `999.88` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7437.6683` n `108` status `ready` deltaP `0.0621` edge `619.8337` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4349` n `102` status `ready` deltaP `30.77` edge `1.3404` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.4252` n `102` status `ready` deltaP `16.8812` edge `1.1102` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.5956` n `108` status `ready` deltaP `4.703` edge `0.3835` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.5486` n `108` status `ready` deltaP `6.3798` edge `0.2941` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7347` n `108` status `ready` deltaP `19.0888` edge `0.0684` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0823` n `108` status `ready` deltaP `5.988` edge `0.0197` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2483` n `108` status `ready` deltaP `3.5651` edge `0.0056` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.3077` n `108` status `ready` deltaP `4.6962` edge `0.0689` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.6724` n `108` status `ready` deltaP `-1.3362` edge `0.0449` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.0907` n `108` status `ready` deltaP `6.792` edge `0.0417` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.5965` n `108` status `ready` deltaP `-11.2497` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7736` n `108` status `ready` deltaP `-1.6147` edge `-0.0027` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3739` n `108` status `ready` deltaP `-14.7979` edge `-0.0041` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.3756` n `108` status `ready` deltaP `-9.3702` edge `-0.0273` maxDD `-3.9892`
- `market_context_high->metal_24h` score `-4.9811` n `102` status `ready` deltaP `14.5425` edge `0.0843` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5474` n `102` status `ready` deltaP `-16.8913` edge `-0.0057` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0202` n `108` status `ready` deltaP `-28.1955` edge `-0.1111` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.1907` n `108` status `ready` deltaP `-6.2895` edge `-0.0418` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
