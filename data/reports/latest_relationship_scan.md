# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T15:37:28.937810+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4122`

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

- `market_context_high->unknown_24h` score `53.9943` n `30` status `ready` deltaP `3.9792` edge `4.473` maxDD `0.0`
- `news_risk_high->equity_24h` score `53.0022` n `50` status `ready` deltaP `58.2422` edge `4.0992` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.4977` n `50` status `ready` deltaP `42.083` edge `2.5899` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.6664` n `30` status `ready` deltaP `14.9942` edge `1.61` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.8964` n `50` status `ready` deltaP `42.3379` edge `0.9888` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.6332` n `30` status `ready` deltaP `44.083` edge `1.6528` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.3577` n `50` status `ready` deltaP `25.6609` edge `1.6074` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.9075` n `50` status `ready` deltaP `49.2457` edge `0.361` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1021` n `50` status `ready` deltaP `41.1765` edge `0.234` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.228` n `50` status `ready` deltaP `29.6438` edge `0.3816` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.0899` n `50` status `ready` deltaP `45.2085` edge `0.1604` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.8568` n `50` status `ready` deltaP `23.4916` edge `0.3857` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.2827` n `50` status `ready` deltaP `21.6467` edge `0.2756` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.9153` n `50` status `ready` deltaP `36.0335` edge `0.1114` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8283` n `30` status `ready` deltaP `46.9435` edge `0.267` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.9122` n `50` status `ready` deltaP `27.1629` edge `0.0966` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2736` n `50` status `ready` deltaP `25.5928` edge `0.0443` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3813` n `50` status `ready` deltaP `17.9461` edge `0.0256` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.9619` n `50` status `ready` deltaP `18.7904` edge `0.096` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.9498` n `50` status `ready` deltaP `18.2768` edge `0.2172` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
