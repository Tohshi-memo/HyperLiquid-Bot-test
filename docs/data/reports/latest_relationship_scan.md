# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T02:07:26.722675+00:00`
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

- `market_context_high->unknown_24h` score `2000.4155` n `56` status `ready` deltaP `3.4483` edge `166.6783` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.715` n `50` status `ready` deltaP `59.2069` edge `4.2355` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.5214` n `50` status `ready` deltaP `36.7931` edge `2.3718` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.2031` n `56` status `ready` deltaP `15.2586` edge `1.5324` maxDD `-12.3757`
- `news_risk_high->equity_4h` score `14.55` n `50` status `ready` deltaP `44.4024` edge `1.0295` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.9234` n `56` status `ready` deltaP `41.2931` edge `1.7086` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3241` n `50` status `ready` deltaP `21.7586` edge `1.5009` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1395` n `50` status `ready` deltaP `50.2414` edge `0.3737` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.137` n `50` status `ready` deltaP `44.4828` edge `0.2982` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3211` n `50` status `ready` deltaP `46.8232` edge `0.1689` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5358` n `50` status `ready` deltaP `22.5449` edge `0.2907` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5066` n `50` status `ready` deltaP `26.5366` edge `0.3422` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.298` n `50` status `ready` deltaP `21.7561` edge `0.3507` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1021` n `50` status `ready` deltaP `37.1829` edge `0.1193` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.137` n `50` status `ready` deltaP `29.372` edge `0.1006` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2773` n `50` status `ready` deltaP `25.4431` edge `0.0456` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5311` n `50` status `ready` deltaP `19.5928` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8488` n `50` status `ready` deltaP `18.3448` edge `0.2038` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8381` n `50` status `ready` deltaP `17.4431` edge `0.0891` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7975` n `50` status `ready` deltaP `18.994` edge `0.0808` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
