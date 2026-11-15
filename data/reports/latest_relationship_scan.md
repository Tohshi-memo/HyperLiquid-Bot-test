# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T19:22:27.667719+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8284`

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

- `market_context_high->unknown_24h` score `577.6485` n `61` status `ready` deltaP `3.9861` edge `48.1108` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.7881` n `50` status `ready` deltaP `50.565` edge `3.5492` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.8833` n `61` status `ready` deltaP `46.1716` edge `3.2533` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.0303` n `61` status `ready` deltaP `63.1417` edge `2.5226` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.1645` n `50` status `ready` deltaP `46.0416` edge `2.7772` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.1533` n `50` status `ready` deltaP `38.6098` edge `0.8684` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.4862` n `50` status `ready` deltaP `20.2565` edge `1.5317` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1649` n `61` status `ready` deltaP `49.3281` edge `0.3602` maxDD `-0.0251`
- `market_context_high->metal_24h` score `6.7061` n `61` status `ready` deltaP `63.6759` edge `0.5244` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.6095` n `50` status `ready` deltaP `42.2461` edge `0.2995` maxDD `-0.4279`
- `market_context_high->crypto_major_24h` score `6.5684` n `61` status `ready` deltaP `14.2711` edge `1.2791` maxDD `-61.4831`
- `news_risk_high->commodity_24h` score `6.5477` n `50` status `ready` deltaP `42.9809` edge `0.2591` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.2435` n `50` status `ready` deltaP `22.6707` edge `0.4234` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9016` n `50` status `ready` deltaP `44.3841` edge `0.1502` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6108` n `50` status `ready` deltaP `27.2988` edge `0.3458` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0163` n `50` status `ready` deltaP `21.497` edge `0.2544` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.682` n `50` status `ready` deltaP `34.2866` edge `0.1036` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5513` n `50` status `ready` deltaP `24.6463` edge `0.0833` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1849` n `50` status `ready` deltaP `24.994` edge `0.0409` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.307` n `50` status `ready` deltaP `17.3473` edge `0.0234` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
