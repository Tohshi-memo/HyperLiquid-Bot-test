# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T06:07:34.892987+00:00`
- Price records: `672`
- Market context records: `4696`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9750`

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

- `market_context_high->unknown_1h` score `79.0182` n `140` status `ready` deltaP `13.3661` edge `6.5375` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2036` n `135` status `ready` deltaP `10.9169` edge `0.4819` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.3469` n `135` status `ready` deltaP `12.3612` edge `0.2055` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3905` n `140` status `ready` deltaP `1.0693` edge `0.0224` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7812` n `135` status `ready` deltaP `3.7692` edge `-0.013` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9267` n `135` status `ready` deltaP `-1.3302` edge `-0.0017` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-1.131` n `140` status `ready` deltaP `-1.3131` edge `0.0132` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2328` n `135` status `ready` deltaP `5.5511` edge `0.0157` maxDD `-9.1941`
- `market_context_high->fx_1h` score `-1.2706` n `140` status `ready` deltaP `-5.4277` edge `-0.0059` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-1.2906` n `135` status `ready` deltaP `1.0897` edge `0.0042` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6432` n `140` status `ready` deltaP `-3.858` edge `-0.0108` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8366` n `140` status `ready` deltaP `-4.645` edge `-0.0759` maxDD `-17.2107`
- `market_context_high->crypto_alt_1h` score `-3.2855` n `140` status `ready` deltaP `-0.7485` edge `-0.0875` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-4.0339` n `140` status `ready` deltaP `-3.8366` edge `-0.1163` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.6853` n `135` status `ready` deltaP `14.8495` edge `0.061` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7853` n `135` status `ready` deltaP `-13.044` edge `-0.0158` maxDD `-5.3476`
- `market_context_high->index_24h` score `-8.4011` n `135` status `ready` deltaP `-10.6366` edge `-0.0917` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6197` n `135` status `ready` deltaP `-3.1595` edge `-0.2183` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.1213` n `135` status `ready` deltaP `-0.5488` edge `-0.2804` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.5853` n `135` status `ready` deltaP `-3.5953` edge `-0.3713` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
