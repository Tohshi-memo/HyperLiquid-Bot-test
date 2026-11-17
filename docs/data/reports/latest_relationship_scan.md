# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T02:22:27.616338+00:00`
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

- `market_context_high->unknown_24h` score `2060.6927` n `57` status `ready` deltaP `3.4483` edge `171.7014` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.7666` n `50` status `ready` deltaP `59.2069` edge `4.2398` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.4941` n `50` status `ready` deltaP `36.7931` edge `2.3683` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.0773` n `57` status `ready` deltaP `14.6007` edge `1.5263` maxDD `-12.3757`
- `news_risk_high->equity_4h` score `14.5404` n `50` status `ready` deltaP `44.4024` edge `1.0287` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.8336` n `57` status `ready` deltaP `40.1966` edge `1.7044` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3303` n `50` status `ready` deltaP `21.7586` edge `1.5017` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1455` n `50` status `ready` deltaP `50.2414` edge `0.3742` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.1724` n `50` status `ready` deltaP `44.6552` edge `0.3` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3199` n `50` status `ready` deltaP `46.8232` edge `0.1688` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5308` n `50` status `ready` deltaP `26.689` edge `0.3432` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5298` n `50` status `ready` deltaP `22.5449` edge `0.2902` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.3064` n `50` status `ready` deltaP `21.7561` edge `0.3514` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1009` n `50` status `ready` deltaP `37.1829` edge `0.1192` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1346` n `50` status `ready` deltaP `29.372` edge `0.1004` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2761` n `50` status `ready` deltaP `25.4431` edge `0.0455` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5311` n `50` status `ready` deltaP `19.5928` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8457` n `50` status `ready` deltaP `18.3448` edge `0.2034` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8349` n `50` status `ready` deltaP `17.4431` edge `0.0887` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7983` n `50` status `ready` deltaP `18.994` edge `0.0809` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
