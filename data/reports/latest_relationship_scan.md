# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T03:07:28.055872+00:00`
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

- `market_context_high->unknown_24h` score `2163.2987` n `59` status `ready` deltaP `3.4483` edge `180.2519` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.9688` n `50` status `ready` deltaP `59.3793` edge `4.2555` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.3767` n `50` status `ready` deltaP `36.6207` edge `2.3544` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.6362` n `59` status `ready` deltaP `13.3518` edge `1.5097` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.4944` n `50` status `ready` deltaP `44.0976` edge `1.0269` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.5916` n `59` status `ready` deltaP `37.9427` edge `1.6884` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3303` n `50` status `ready` deltaP `21.7586` edge `1.5017` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.2073` n `50` status `ready` deltaP `50.7586` edge `0.3759` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.2798` n `50` status `ready` deltaP `45.1724` edge `0.3055` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2811` n `50` status `ready` deltaP `46.5183` edge `0.1676` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.578` n `50` status `ready` deltaP `26.9939` edge `0.3451` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5286` n `50` status `ready` deltaP `22.5449` edge `0.2901` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.3268` n `50` status `ready` deltaP `21.7561` edge `0.3531` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0973` n `50` status `ready` deltaP `37.1829` edge `0.1189` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1078` n `50` status `ready` deltaP `29.0671` edge `0.1002` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2461` n `50` status `ready` deltaP `25.1437` edge `0.045` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5323` n `50` status `ready` deltaP `19.5928` edge `0.0272` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8254` n `50` status `ready` deltaP `18.3448` edge `0.2008` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8046` n `50` status `ready` deltaP `19.1437` edge `0.0807` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8014` n `50` status `ready` deltaP `16.994` edge `0.0874` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
