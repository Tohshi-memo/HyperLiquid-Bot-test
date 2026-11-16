# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T08:52:33.286588+00:00`
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

- `market_context_high->unknown_24h` score `92.4962` n `30` status `ready` deltaP `3.9931` edge `7.6814` maxDD `0.0`
- `news_risk_high->equity_24h` score `49.9947` n `50` status `ready` deltaP `53.7986` edge `3.8782` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1301` n `50` status `ready` deltaP `40.6389` edge `2.5524` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.4982` n `30` status `ready` deltaP `12.1527` edge `1.5316` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.2656` n `30` status `ready` deltaP `42.6389` edge `1.6153` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.1989` n `50` status `ready` deltaP `38.6098` edge `0.8722` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.5984` n `50` status `ready` deltaP `22.8194` edge `1.529` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.2711` n `50` status `ready` deltaP `44.7708` edge `0.3378` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0966` n `50` status `ready` deltaP `40.9722` edge `0.2349` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0208` n `50` status `ready` deltaP `44.689` edge `0.1581` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.333` n `50` status `ready` deltaP `26.8415` edge `0.3257` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.256` n `50` status `ready` deltaP `20.8415` edge `0.3533` maxDD `-9.0062`
- `market_context_high->metal_24h` score `3.8772` n `30` status `ready` deltaP `47.5695` edge `0.2691` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.7947` n `50` status `ready` deltaP `19.4012` edge `0.2499` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.671` n `50` status `ready` deltaP `34.1341` edge `0.1037` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5535` n `50` status `ready` deltaP `24.4939` edge `0.0845` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2077` n `50` status `ready` deltaP `24.994` edge `0.0428` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.1801` n `50` status `ready` deltaP `15.8503` edge `0.0228` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9987` n `50` status `ready` deltaP `18.9028` edge `0.2193` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8178` n `50` status `ready` deltaP `19.7425` edge `0.0784` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
