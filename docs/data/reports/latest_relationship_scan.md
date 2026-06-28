# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T03:22:24.737619+00:00`
- Price records: `672`
- Market context records: `5001`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10290`

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

- `market_context_high->unknown_1h` score `15.2947` n `93` status `ready` deltaP `4.1176` edge `1.2972` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `5.8871` n `89` status `ready` deltaP `17.4945` edge `0.5324` maxDD `-8.3416`
- `market_context_high->unknown_24h` score `5.6725` n `74` status `ready` deltaP `29.8142` edge `0.3082` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.0821` n `89` status `ready` deltaP `12.3904` edge `0.4803` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `4.7879` n `89` status `ready` deltaP `21.6617` edge `0.3568` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1827` n `89` status `ready` deltaP `12.0684` edge `0.126` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8764` n `93` status `ready` deltaP `8.1868` edge `0.0758` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8572` n `93` status `ready` deltaP `6.553` edge `0.1195` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.6301` n `89` status `ready` deltaP `5.3439` edge `0.1833` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3736` n `93` status `ready` deltaP `6.4033` edge `0.0381` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.2839` n `89` status `ready` deltaP `5.8406` edge `0.0426` maxDD `-0.9634`
- `market_context_high->crypto_alt_1h` score `0.175` n `93` status `ready` deltaP `5.1107` edge `0.0906` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.1914` n `74` status `ready` deltaP `6.9539` edge `0.0053` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.2909` n `93` status `ready` deltaP `2.157` edge `0.0143` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5563` n `93` status `ready` deltaP `2.2117` edge `0.013` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7995` n `89` status `ready` deltaP `4.0901` edge `-0.0045` maxDD `-5.021`
- `market_context_high->fx_4h` score `-0.875` n `89` status `ready` deltaP `-1.9903` edge `-0.0014` maxDD `-1.1346`
- `market_context_high->fx_1h` score `-1.7473` n `93` status `ready` deltaP `-11.8489` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-4.1296` n `74` status `ready` deltaP `6.142` edge `-0.0595` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.1486` n `74` status `ready` deltaP `0.3472` edge `0.0113` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
