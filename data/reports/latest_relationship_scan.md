# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T01:52:37.503964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4392`

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

- `market_context_high->unknown_24h` score `1947.1355` n `55` status `ready` deltaP `3.4483` edge `162.2383` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.6742` n `50` status `ready` deltaP `59.2069` edge `4.2321` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.571` n `50` status `ready` deltaP `36.9655` edge `2.377` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.0576` n `55` status `ready` deltaP `14.2946` edge `1.5267` maxDD `-12.3757`
- `news_risk_high->equity_4h` score `14.5802` n `50` status `ready` deltaP `44.5549` edge `1.031` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.8454` n `55` status `ready` deltaP `40.7837` edge `1.702` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3393` n `50` status `ready` deltaP `21.931` edge `1.5017` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1359` n `50` status `ready` deltaP `50.2414` edge `0.3734` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.1004` n `50` status `ready` deltaP `44.3103` edge `0.2963` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3369` n `50` status `ready` deltaP `46.9756` edge `0.1692` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5609` n `50` status `ready` deltaP `22.6946` edge `0.2918` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4824` n `50` status `ready` deltaP `26.3841` edge `0.3412` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.2932` n `50` status `ready` deltaP `21.7561` edge `0.3503` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1033` n `50` status `ready` deltaP `37.1829` edge `0.1194` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1516` n `50` status `ready` deltaP `29.5244` edge `0.1008` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2785` n `50` status `ready` deltaP `25.4431` edge `0.0457` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5323` n `50` status `ready` deltaP `19.5928` edge `0.0272` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8535` n `50` status `ready` deltaP `18.3448` edge `0.2044` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8404` n `50` status `ready` deltaP `17.4431` edge `0.0894` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7999` n `50` status `ready` deltaP `18.994` edge `0.0811` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
