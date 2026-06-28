# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T10:07:25.728472+00:00`
- Price records: `672`
- Market context records: `5029`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10174`

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

- `market_context_high->unknown_1h` score `15.182` n `93` status `ready` deltaP `3.8182` edge `1.2898` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0299` n `93` status `ready` deltaP `21.602` edge `0.7107` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.5361` n `93` status `ready` deltaP `16.947` edge `0.5068` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3457` n `93` status `ready` deltaP `14.6358` edge `0.4873` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2696` n `93` status `ready` deltaP `13.5441` edge `0.1234` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8764` n `93` status `ready` deltaP `8.3365` edge `0.0748` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7757` n `93` status `ready` deltaP `6.1039` edge `0.1157` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.4357` n `93` status `ready` deltaP `3.1209` edge `0.1732` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3868` n `93` status `ready` deltaP `6.553` edge `0.0382` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1944` n `93` status `ready` deltaP `5.2604` edge `0.0921` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0533` n `74` status `ready` deltaP `9.3844` edge `0.0068` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1107` n `93` status `ready` deltaP `4.0191` edge `0.0401` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3213` n `93` status `ready` deltaP `1.5582` edge `0.0144` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5479` n `93` status `ready` deltaP `2.3614` edge `0.0127` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8186` n `93` status `ready` deltaP `3.393` edge `-0.0023` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0196` n `93` status `ready` deltaP `-4.3732` edge `-0.0027` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.8336` n `93` status `ready` deltaP `-12.8968` edge `-0.0058` maxDD `-0.5482`
- `market_context_high->unknown_24h` score `-3.023` n `74` status `ready` deltaP `27.0364` edge `-0.3979` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.766` n `74` status `ready` deltaP `5.0347` edge `0.0291` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.5605` n `74` status `ready` deltaP `1.4545` edge `-0.0835` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
