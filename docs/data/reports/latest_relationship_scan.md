# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T15:37:32.881253+00:00`
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

- `market_context_high->unknown_24h` score `534.8282` n `64` status `ready` deltaP `3.8128` edge `44.5436` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.6905` n `50` status `ready` deltaP `50.0451` edge `3.4612` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.0079` n `64` status `ready` deltaP `46.4201` edge `3.1787` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.1563` n `64` status `ready` deltaP `61.1568` edge `2.463` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.4929` n `50` status `ready` deltaP `46.3882` edge `2.817` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2075` n `50` status `ready` deltaP `38.7622` edge `0.8719` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.9361` n `50` status `ready` deltaP `17.6568` edge `1.4785` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.0873` n `64` status `ready` deltaP `49.5586` edge `0.3522` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.8624` n `50` status `ready` deltaP `45.5806` edge `0.268` maxDD `0.0`
- `market_context_high->metal_24h` score `6.5555` n `64` status `ready` deltaP `61.8447` edge `0.5173` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.4931` n `50` status `ready` deltaP `42.2461` edge `0.2898` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.1827` n `50` status `ready` deltaP `22.9756` edge `0.4163` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.8564` n `50` status `ready` deltaP `43.7744` edge `0.1505` maxDD `-1.0104`
- `market_context_high->crypto_major_24h` score `4.843` n `64` status `ready` deltaP `13.3882` edge `1.2481` maxDD `-69.0352`
- `news_risk_high->crypto_alt_4h` score `4.452` n `50` status `ready` deltaP `26.9939` edge `0.3346` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0283` n `50` status `ready` deltaP `21.6467` edge `0.2544` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7499` n `50` status `ready` deltaP `34.8963` edge `0.1052` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6597` n `50` status `ready` deltaP `25.8659` edge `0.0842` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2376` n `50` status `ready` deltaP `25.5928` edge `0.0413` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2819` n `50` status `ready` deltaP `17.0479` edge `0.0233` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
