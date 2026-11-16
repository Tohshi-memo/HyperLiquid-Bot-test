# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T09:07:48.809411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4052`

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

- `market_context_high->unknown_24h` score `96.0002` n `30` status `ready` deltaP `3.9931` edge `7.9734` maxDD `0.0`
- `news_risk_high->equity_24h` score `50.1418` n `50` status `ready` deltaP `53.9722` edge `3.8893` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1773` n `50` status `ready` deltaP `40.8125` edge `2.5573` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.6033` n `30` status `ready` deltaP `12.3264` edge `1.5392` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.3129` n `30` status `ready` deltaP `42.8125` edge `1.6202` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.2423` n `50` status `ready` deltaP `38.7622` edge `0.8748` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.6668` n `50` status `ready` deltaP `22.9931` edge `1.5366` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.2982` n `50` status `ready` deltaP `44.9444` edge `0.3389` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0942` n `50` status `ready` deltaP `40.9722` edge `0.2347` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.022` n `50` status `ready` deltaP `44.689` edge `0.1582` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.404` n `50` status `ready` deltaP `26.9939` edge `0.3306` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.297` n `50` status `ready` deltaP `20.9939` edge `0.3557` maxDD `-9.0062`
- `market_context_high->metal_24h` score `3.8803` n `30` status `ready` deltaP `47.5695` edge `0.2695` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.827` n `50` status `ready` deltaP `19.5509` edge `0.2516` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6686` n `50` status `ready` deltaP `34.1341` edge `0.1035` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5559` n `50` status `ready` deltaP `24.4939` edge `0.0847` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2077` n `50` status `ready` deltaP `24.994` edge `0.0428` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.1945` n `50` status `ready` deltaP `16.0` edge `0.023` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0018` n `50` status `ready` deltaP `18.9028` edge `0.2197` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8474` n `50` status `ready` deltaP `19.8922` edge `0.0812` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
