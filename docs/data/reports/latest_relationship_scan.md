# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T14:52:29.337213+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4080`

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

- `market_context_high->unknown_24h` score `68.5791` n `30` status `ready` deltaP `3.9792` edge `5.6884` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.7207` n `50` status `ready` deltaP `57.7232` edge `4.0792` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.5301` n `50` status `ready` deltaP `42.2561` edge `2.5929` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.6652` n `30` status `ready` deltaP `14.9942` edge `1.6099` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.6159` n `50` status `ready` deltaP `41.9514` edge `0.968` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6656` n `30` status `ready` deltaP `44.2561` edge `1.6558` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3569` n `50` status `ready` deltaP `25.6609` edge `1.6073` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.8395` n `50` status `ready` deltaP `48.7266` edge `0.3588` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0949` n `50` status `ready` deltaP `41.1765` edge `0.2334` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.1759` n `50` status `ready` deltaP `29.3982` edge `0.3789` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.0877` n `50` status `ready` deltaP `45.2705` edge `0.1598` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.7674` n `50` status `ready` deltaP `23.0942` edge `0.3809` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.1004` n `50` status `ready` deltaP `21.1976` edge `0.2634` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.858` n `50` status `ready` deltaP `35.6474` edge `0.1092` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8337` n `30` status `ready` deltaP `46.9435` edge `0.2677` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.8556` n `50` status `ready` deltaP `26.7842` edge `0.0944` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2413` n `50` status `ready` deltaP `25.2934` edge `0.0436` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3298` n `50` status `ready` deltaP `17.497` edge `0.0243` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9552` n `50` status `ready` deltaP `18.2768` edge `0.2179` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9136` n `50` status `ready` deltaP `18.491` edge `0.0918` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
