# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T15:52:26.194773+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9998`

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

- `market_context_high->unknown_24h` score `534.9494` n `64` status `ready` deltaP `3.8128` edge `44.5537` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.7619` n `50` status `ready` deltaP `50.2184` edge `3.466` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.0794` n `64` status `ready` deltaP `46.5934` edge `3.1835` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.235` n `64` status `ready` deltaP `61.3302` edge `2.4684` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.4828` n `50` status `ready` deltaP `46.3882` edge `2.8157` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2281` n `50` status `ready` deltaP `38.9146` edge `0.8726` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.9872` n `50` status `ready` deltaP `17.8302` edge `1.4839` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.0933` n `64` status `ready` deltaP `49.5586` edge `0.3527` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.839` n `50` status `ready` deltaP `45.4073` edge `0.2672` maxDD `0.0`
- `market_context_high->metal_24h` score `6.5731` n `64` status `ready` deltaP `62.018` edge `0.5184` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.4991` n `50` status `ready` deltaP `42.2461` edge `0.2903` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.2007` n `50` status `ready` deltaP `22.9756` edge `0.4178` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.8564` n `50` status `ready` deltaP `43.7744` edge `0.1505` maxDD `-1.0104`
- `market_context_high->crypto_major_24h` score `4.8274` n `64` status `ready` deltaP `13.3882` edge `1.2468` maxDD `-69.0352`
- `news_risk_high->crypto_alt_4h` score `4.4724` n `50` status `ready` deltaP `26.9939` edge `0.3363` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0139` n `50` status `ready` deltaP `21.497` edge `0.2542` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7475` n `50` status `ready` deltaP `34.8963` edge `0.105` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6597` n `50` status `ready` deltaP `25.8659` edge `0.0842` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2376` n `50` status `ready` deltaP `25.5928` edge `0.0413` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2699` n `50` status `ready` deltaP `16.8982` edge `0.0233` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
