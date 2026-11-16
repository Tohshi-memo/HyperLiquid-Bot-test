# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T19:50:13.406546+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4412`

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

- `news_risk_high->equity_24h` score `53.629` n `50` status `ready` deltaP `59.2069` edge `4.145` maxDD `-3.6503`
- `market_context_high->unknown_24h` score `52.1176` n `31` status `ready` deltaP `3.9655` edge `4.3167` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `20.6422` n `50` status `ready` deltaP `39.8966` edge `2.4948` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.8079` n `31` status `ready` deltaP `11.9133` edge `1.559` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.3691` n `50` status `ready` deltaP `43.9271` edge `1.0176` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.7629` n `31` status `ready` deltaP `39.9611` edge `1.5687` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.8322` n `50` status `ready` deltaP `23.6552` edge `1.5534` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0399` n `50` status `ready` deltaP `50.2414` edge `0.3654` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3235` n `50` status `ready` deltaP `41.3793` edge `0.2511` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3356` n `50` status `ready` deltaP `47.0942` edge `0.1683` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.8205` n `50` status `ready` deltaP `28.0304` edge `0.3584` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.499` n `50` status `ready` deltaP `22.3343` edge `0.3636` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.4588` n `50` status `ready` deltaP `21.8685` edge `0.2888` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0609` n `50` status `ready` deltaP `36.8632` edge `0.118` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.6139` n `31` status `ready` deltaP `44.8609` edge `0.2534` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.1087` n `50` status `ready` deltaP `29.0638` edge `0.1003` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2852` n `50` status `ready` deltaP `25.6622` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5139` n `50` status `ready` deltaP `19.3632` edge `0.0272` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9065` n `50` status `ready` deltaP `18.3448` edge `0.2112` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9047` n `50` status `ready` deltaP `18.2601` edge `0.0922` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
