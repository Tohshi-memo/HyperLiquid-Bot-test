# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T18:07:31.047624+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4248`

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

- `news_risk_high->equity_24h` score `53.4866` n `50` status `ready` deltaP `59.1073` edge `4.1338` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.9994` n `50` status `ready` deltaP `40.526` edge `2.5364` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.2695` n `30` status `ready` deltaP `13.7831` edge `1.585` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.256` n `50` status `ready` deltaP `43.4878` edge `1.0111` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.135` n `30` status `ready` deltaP `42.526` edge `1.5993` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.0997` n `50` status `ready` deltaP `24.4498` edge `1.5824` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0151` n `50` status `ready` deltaP `50.1107` edge `0.3642` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1681` n `50` status `ready` deltaP `41.1765` edge `0.2395` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2219` n `50` status `ready` deltaP `46.2134` edge `0.1647` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9425` n `50` status `ready` deltaP `28.6707` edge `0.3643` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.5605` n `50` status `ready` deltaP `22.5183` edge `0.3675` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.477` n `50` status `ready` deltaP `22.0958` edge `0.2888` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0199` n `50` status `ready` deltaP `36.7256` edge `0.1155` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.7971` n `30` status `ready` deltaP `46.9435` edge `0.263` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.019` n `50` status `ready` deltaP `28.1524` edge `0.0989` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.276` n `50` status `ready` deltaP `25.5928` edge `0.0445` maxDD `-0.3692`
- `market_context_high->unknown_24h` score `1.5411` n `30` status `ready` deltaP `3.9792` edge `0.1019` maxDD `0.0`
- `news_risk_high->index_1h` score `1.4568` n `50` status `ready` deltaP `18.6946` edge `0.0269` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9186` n `50` status `ready` deltaP `18.2768` edge `0.2132` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9051` n `50` status `ready` deltaP `18.1916` edge `0.0927` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
