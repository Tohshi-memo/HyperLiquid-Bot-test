# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T04:52:26.741542+00:00`
- Price records: `672`
- Market context records: `5007`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10258`

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

- `market_context_high->unknown_1h` score `15.4783` n `93` status `ready` deltaP `4.2673` edge `1.3115` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.7841` n `93` status `ready` deltaP `22.3642` edge `0.8518` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.6663` n `93` status `ready` deltaP `17.4043` edge `0.5146` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.2142` n `93` status `ready` deltaP `14.0261` edge `0.4804` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `4.2928` n `74` status `ready` deltaP `29.2934` edge `0.1967` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3157` n `93` status `ready` deltaP `14.0014` edge `0.1242` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8896` n `93` status `ready` deltaP `8.3365` edge `0.0759` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8069` n `93` status `ready` deltaP `6.2536` edge `0.1173` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5184` n `93` status `ready` deltaP `4.0356` edge `0.1777` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3233` n `93` status `ready` deltaP `5.8045` edge `0.0379` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1119` n `93` status `ready` deltaP `4.3622` edge `0.0875` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0547` n `93` status `ready` deltaP `4.6289` edge `0.0407` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.1341` n `74` status `ready` deltaP `7.9955` edge `0.0057` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2683` n `93` status `ready` deltaP `2.4564` edge `0.0152` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5694` n `93` status `ready` deltaP `2.062` edge `0.0129` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.797` n `93` status `ready` deltaP `4.0028` edge `-0.0036` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.984` n `93` status `ready` deltaP `-3.7634` edge `-0.0022` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7461` n `93` status `ready` deltaP `-11.8489` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-4.0835` n `74` status `ready` deltaP `1.3889` edge `0.0127` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.2282` n `74` status `ready` deltaP `5.1004` edge `-0.0652` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
