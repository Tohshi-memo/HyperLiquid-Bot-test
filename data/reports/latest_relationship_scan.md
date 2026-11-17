# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T00:52:23.024528+00:00`
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

- `market_context_high->unknown_24h` score `1711.1531` n `51` status `ready` deltaP `3.4483` edge `142.5731` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.5122` n `50` status `ready` deltaP `59.2069` edge `4.2186` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.7831` n `50` status `ready` deltaP `37.6552` edge `2.3996` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.6334` n `51` status `ready` deltaP `11.7816` edge `1.5044` maxDD `-12.0798`
- `news_risk_high->equity_4h` score `14.6791` n `50` status `ready` deltaP `45.0122` edge `1.0362` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.4494` n `51` status `ready` deltaP `38.4787` edge `1.6666` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.4114` n `50` status `ready` deltaP `22.4483` edge `1.5075` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1215` n `50` status `ready` deltaP `50.2414` edge `0.3722` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.9553` n `50` status `ready` deltaP `43.6207` edge `0.2888` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.4013` n `50` status `ready` deltaP `47.5854` edge `0.1705` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6233` n `50` status `ready` deltaP `22.994` edge `0.295` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4692` n `50` status `ready` deltaP `26.3841` edge `0.3401` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.3244` n `50` status `ready` deltaP `21.7561` edge `0.3529` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1117` n `50` status `ready` deltaP `37.1829` edge `0.1201` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2123` n `50` status `ready` deltaP `30.1341` edge `0.1018` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.312` n `50` status `ready` deltaP `25.7425` edge `0.0465` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5898` n `50` status `ready` deltaP `20.1916` edge `0.028` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8706` n `50` status `ready` deltaP `18.3448` edge `0.2066` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8599` n `50` status `ready` deltaP `17.7425` edge `0.0899` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.842` n `50` status `ready` deltaP `19.4431` edge `0.0835` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
