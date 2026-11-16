# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T09:31:19.079281+00:00`
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

- `market_context_high->unknown_24h` score `102.7442` n `30` status `ready` deltaP `3.9931` edge `8.5354` maxDD `0.0`
- `news_risk_high->equity_24h` score `50.412` n `50` status `ready` deltaP `54.3194` edge `3.9095` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.2469` n `50` status `ready` deltaP `41.1597` edge `2.5639` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.7667` n `30` status `ready` deltaP `12.6736` edge `1.5505` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.3824` n `30` status `ready` deltaP `43.1597` edge `1.6268` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.3123` n `50` status `ready` deltaP `39.0671` edge `0.8786` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.7729` n `50` status `ready` deltaP `23.3403` edge `1.5479` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.3512` n `50` status `ready` deltaP `45.2917` edge `0.341` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.093` n `50` status `ready` deltaP `40.9722` edge `0.2346` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0536` n `50` status `ready` deltaP `44.9939` edge `0.1588` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5196` n `50` status `ready` deltaP `27.2988` edge `0.3382` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.367` n `50` status `ready` deltaP `21.2988` edge `0.3595` maxDD `-9.0062`
- `market_context_high->metal_24h` score `3.8956` n `30` status `ready` deltaP `47.7431` edge `0.2703` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.8714` n `50` status `ready` deltaP `19.8503` edge `0.2533` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6698` n `50` status `ready` deltaP `34.1341` edge `0.1036` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5717` n `50` status `ready` deltaP `24.6463` edge `0.085` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2089` n `50` status `ready` deltaP `24.994` edge `0.0429` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2196` n `50` status `ready` deltaP `16.2994` edge `0.0231` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0171` n `50` status `ready` deltaP `19.0764` edge `0.2205` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.877` n `50` status `ready` deltaP `20.1916` edge `0.083` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
