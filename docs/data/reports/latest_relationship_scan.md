# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T17:07:27.955408+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10008`

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

- `market_context_high->unknown_24h` score `535.4618` n `64` status `ready` deltaP `3.8128` edge `44.5964` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.1106` n `50` status `ready` deltaP `50.3917` edge `3.4939` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.4281` n `64` status `ready` deltaP `46.7667` edge `3.2114` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.5131` n `64` status `ready` deltaP `62.1967` edge `2.4858` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.381` n `50` status `ready` deltaP `46.2149` edge `2.8038` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2825` n `50` status `ready` deltaP `39.2195` edge `0.8751` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.168` n `50` status `ready` deltaP `18.6967` edge `1.5013` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1293` n `64` status `ready` deltaP `49.5586` edge `0.3557` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.7337` n `50` status `ready` deltaP `44.5407` edge `0.2642` maxDD `0.0`
- `market_context_high->metal_24h` score `6.6579` n `64` status `ready` deltaP `62.8845` edge `0.5235` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.5351` n `50` status `ready` deltaP `42.2461` edge `0.2933` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.2895` n `50` status `ready` deltaP `22.9756` edge `0.4252` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9222` n `50` status `ready` deltaP `44.5366` edge `0.1509` maxDD `-1.0104`
- `market_context_high->crypto_major_24h` score `4.6707` n `64` status `ready` deltaP `13.2149` edge `1.2349` maxDD `-69.0352`
- `news_risk_high->crypto_alt_4h` score `4.5648` n `50` status `ready` deltaP `26.9939` edge `0.344` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9564` n `50` status `ready` deltaP `21.0479` edge `0.2524` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7415` n `50` status `ready` deltaP `34.8963` edge `0.1045` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6609` n `50` status `ready` deltaP `25.8659` edge `0.0843` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1993` n `50` status `ready` deltaP `25.1437` edge `0.0411` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2436` n `50` status `ready` deltaP `16.5988` edge `0.0231` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
