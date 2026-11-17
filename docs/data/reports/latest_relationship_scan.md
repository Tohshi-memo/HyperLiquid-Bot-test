# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T14:07:41.299835+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3874`

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

- `market_context_high->unknown_24h` score `1694.9456` n `90` status `ready` deltaP `3.4602` edge `141.2224` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.1135` n `50` status `ready` deltaP `66.8927` edge `4.5508` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.1574` n `50` status `ready` deltaP `29.2803` edge `2.1188` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.7434` n `90` status `ready` deltaP `44.6136` edge `1.9198` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.1334` n `50` status `ready` deltaP `43.3354` edge `1.0019` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `13.8759` n `90` status `ready` deltaP `29.4041` edge `1.7953` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.202` n `50` status `ready` deltaP `58.2422` edge `0.4089` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.088` n `50` status `ready` deltaP `52.5952` edge `0.4067` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.123` n `50` status `ready` deltaP `15.6263` edge `1.3878` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.9188` n `50` status `ready` deltaP `43.7744` edge `0.1557` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.4566` n `50` status `ready` deltaP `22.5449` edge `0.2841` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.2596` n `50` status `ready` deltaP `25.7744` edge `0.3267` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.6378` n `50` status `ready` deltaP `33.5244` edge `0.105` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.533` n `50` status `ready` deltaP `19.4695` edge `0.3022` maxDD `-9.0062`
- `news_risk_high->index_4h` score `3.0616` n `50` status `ready` deltaP `28.6098` edge `0.0994` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1718` n `50` status `ready` deltaP `24.3952` edge `0.0438` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4712` n `50` status `ready` deltaP `18.8443` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9618` n `50` status `ready` deltaP `20.3529` edge `0.2049` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7375` n `50` status `ready` deltaP `16.5449` edge `0.0822` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6557` n `50` status `ready` deltaP `18.0958` edge `0.0686` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
