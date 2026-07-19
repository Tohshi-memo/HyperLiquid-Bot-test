# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T23:22:29.133888+00:00`
- Price records: `672`
- Market context records: `7301`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.0976` n `126` status `ready` deltaP `5.148` edge `0.0021` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5201` n `126` status `ready` deltaP `0.1716` edge `-0.0106` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.5295` n `126` status `ready` deltaP `0.1497` edge `0.035` maxDD `-5.9775`
- `market_context_high->commodity_4h` score `-0.6952` n `121` status `ready` deltaP `2.7472` edge `-0.0106` maxDD `-2.4139`
- `market_context_high->fx_24h` score `-0.8725` n `117` status `ready` deltaP `1.3393` edge `0.002` maxDD `-2.1564`
- `market_context_high->fx_4h` score `-0.9667` n `121` status `ready` deltaP `3.5914` edge `0.0121` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-1.0222` n `126` status `ready` deltaP `3.4146` edge `0.0331` maxDD `-7.6171`
- `market_context_high->index_1h` score `-1.2905` n `126` status `ready` deltaP `-5.2124` edge `-0.0086` maxDD `-2.1355`
- `market_context_high->unknown_4h` score `-1.2944` n `121` status `ready` deltaP `6.061` edge `0.0876` maxDD `-6.2031`
- `market_context_high->metal_1h` score `-1.3337` n `126` status `ready` deltaP `-8.8062` edge `-0.0019` maxDD `-1.4971`
- `market_context_high->unknown_1h` score `-1.8632` n `126` status `ready` deltaP `0.8079` edge `-0.0983` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-2.0995` n `121` status `ready` deltaP `1.3996` edge `-0.0042` maxDD `-15.2776`
- `market_context_high->metal_4h` score `-2.3829` n `121` status `ready` deltaP `-8.558` edge `-0.0029` maxDD `-4.6441`
- `market_context_high->crypto_major_4h` score `-3.0396` n `121` status `ready` deltaP `2.0019` edge `-0.0136` maxDD `-23.4879`
- `market_context_high->unknown_24h` score `-3.2315` n `118` status `ready` deltaP `-8.1686` edge `-0.0406` maxDD `-13.5391`
- `market_context_high->commodity_24h` score `-3.318` n `117` status `ready` deltaP `-6.6949` edge `-0.1521` maxDD `-2.3815`
- `market_context_high->equity_1h` score `-4.3314` n `126` status `ready` deltaP `-8.5371` edge `-0.0664` maxDD `-14.3442`
- `market_context_high->index_4h` score `-4.8029` n `121` status `ready` deltaP `-14.5614` edge `-0.0544` maxDD `-9.5678`
- `market_context_high->metal_24h` score `-10.9022` n `118` status `ready` deltaP `-28.5164` edge `-0.1258` maxDD `-20.7422`
- `market_context_high->index_24h` score `-12.7689` n `117` status `ready` deltaP `-30.3055` edge `-0.1627` maxDD `-32.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
