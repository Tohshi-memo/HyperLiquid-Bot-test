# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T03:52:43.600951+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8904`

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

- `news_risk_high->equity_24h` score `47.9831` n `50` status `ready` deltaP `50.6736` edge `3.7314` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `39.4677` n `64` status `ready` deltaP `6.1738` edge `3.2564` maxDD `-0.02`
- `news_risk_high->crypto_major_24h` score `21.2903` n `50` status `ready` deltaP `41.6806` edge `2.566` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.913` n `50` status `ready` deltaP `37.3902` edge `0.8565` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.0978` n `50` status `ready` deltaP `20.7361` edge `1.4787` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.893` n `50` status `ready` deltaP `42.3403` edge `0.3225` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2334` n `50` status `ready` deltaP `40.9722` edge `0.2463` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9976` n `50` status `ready` deltaP `44.3841` edge `0.1582` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3328` n `50` status `ready` deltaP `20.8415` edge `0.3597` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1192` n `50` status `ready` deltaP `25.7744` edge `0.315` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9253` n `50` status `ready` deltaP `20.2994` edge `0.2548` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8923` n `50` status `ready` deltaP `35.5061` edge `0.113` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4636` n `50` status `ready` deltaP `23.5793` edge `0.0831` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2437` n `50` status `ready` deltaP `25.2934` edge `0.0438` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2879` n `50` status `ready` deltaP `17.0479` edge `0.0238` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9964` n `50` status `ready` deltaP `18.9028` edge `0.219` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8458` n `50` status `ready` deltaP `19.7425` edge `0.082` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8099` n `50` status `ready` deltaP `18.0419` edge `0.0815` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.3809` n `50` status `ready` deltaP `4.2455` edge `0.0369` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.901` n `76` status `ready` deltaP `-4.6013` edge `-0.009` maxDD `-2.067`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
