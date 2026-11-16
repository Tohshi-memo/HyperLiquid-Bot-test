# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T09:22:33.482976+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4058`

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

- `market_context_high->unknown_24h` score `99.4118` n `30` status `ready` deltaP `3.9931` edge `8.2577` maxDD `0.0`
- `news_risk_high->equity_24h` score `50.2817` n `50` status `ready` deltaP `54.1458` edge `3.8998` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.2176` n `50` status `ready` deltaP `40.9861` edge `2.5613` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.6892` n `30` status `ready` deltaP `12.5` edge `1.5452` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.3531` n `30` status `ready` deltaP `42.9861` edge `1.6242` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.2833` n `50` status `ready` deltaP `38.9146` edge `0.8772` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.7226` n `50` status `ready` deltaP `23.1667` edge `1.5426` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.3253` n `50` status `ready` deltaP `45.1181` edge `0.34` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0942` n `50` status `ready` deltaP `40.9722` edge `0.2347` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.039` n `50` status `ready` deltaP `44.8415` edge `0.1586` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.4654` n `50` status `ready` deltaP `27.1463` edge `0.3347` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3356` n `50` status `ready` deltaP `21.1463` edge `0.3579` maxDD `-9.0062`
- `market_context_high->metal_24h` score `3.8834` n `30` status `ready` deltaP `47.5695` edge `0.2699` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.8522` n `50` status `ready` deltaP `19.7006` edge `0.2527` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6674` n `50` status `ready` deltaP `34.1341` edge `0.1034` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5705` n `50` status `ready` deltaP `24.6463` edge `0.0849` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2089` n `50` status `ready` deltaP `24.994` edge `0.0429` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2076` n `50` status `ready` deltaP `16.1497` edge `0.0231` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0049` n `50` status `ready` deltaP `18.9028` edge `0.2201` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.863` n `50` status `ready` deltaP `20.0419` edge `0.0822` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
