# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T02:52:27.716414+00:00`
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

- `market_context_high->unknown_24h` score `2174.5463` n `59` status `ready` deltaP `3.4483` edge `181.1892` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.8914` n `50` status `ready` deltaP `59.2069` edge `4.2502` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.4247` n `50` status `ready` deltaP `36.7931` edge `2.3594` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.6422` n `59` status `ready` deltaP `13.3518` edge `1.5102` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.5052` n `50` status `ready` deltaP `44.0976` edge `1.0278` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6396` n `59` status `ready` deltaP `38.1151` edge `1.6934` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3342` n `50` status `ready` deltaP `21.7586` edge `1.5022` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1875` n `50` status `ready` deltaP `50.5862` edge `0.3754` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.2456` n `50` status `ready` deltaP `45.0` edge `0.3038` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2993` n `50` status `ready` deltaP `46.6707` edge `0.1681` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5756` n `50` status `ready` deltaP `26.9939` edge `0.3449` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.531` n `50` status `ready` deltaP `22.5449` edge `0.2903` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.3232` n `50` status `ready` deltaP `21.7561` edge `0.3528` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0973` n `50` status `ready` deltaP `37.1829` edge `0.1189` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.109` n `50` status `ready` deltaP `29.0671` edge `0.1003` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2617` n `50` status `ready` deltaP `25.2934` edge `0.0453` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5323` n `50` status `ready` deltaP `19.5928` edge `0.0272` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8324` n `50` status `ready` deltaP `18.3448` edge `0.2017` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8147` n `50` status `ready` deltaP `17.1437` edge `0.0881` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8085` n `50` status `ready` deltaP `19.1437` edge `0.0812` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
