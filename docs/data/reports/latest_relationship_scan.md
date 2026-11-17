# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T06:22:25.707457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4408`

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

- `market_context_high->unknown_24h` score `2322.5615` n `64` status `ready` deltaP `3.4483` edge `193.5238` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.0625` n `50` status `ready` deltaP `61.6207` edge `4.3317` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.6752` n `50` status `ready` deltaP `34.3793` edge `2.2794` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.8044` n `64` status `ready` deltaP `17.3491` edge `1.5804` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.4462` n `50` status `ready` deltaP `43.9451` edge `1.0239` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.0412` n `64` status `ready` deltaP `38.8793` edge `1.7398` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.1432` n `50` status `ready` deltaP `20.7241` edge `1.4846` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.497` n `50` status `ready` deltaP `53.0` edge `0.3851` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.8371` n `50` status `ready` deltaP `47.4138` edge `0.337` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1028` n `50` status `ready` deltaP `44.9939` edge `0.1629` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6112` n `50` status `ready` deltaP `23.2934` edge `0.292` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5012` n `50` status `ready` deltaP `26.9939` edge `0.3387` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.1874` n `50` status `ready` deltaP `21.6037` edge `0.3425` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1251` n `50` status `ready` deltaP `37.3354` edge `0.1202` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2075` n `50` status `ready` deltaP `30.1341` edge `0.1014` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2054` n `50` status `ready` deltaP `24.6946` edge `0.0446` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5718` n `50` status `ready` deltaP `20.0419` edge `0.0275` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7827` n `50` status `ready` deltaP `16.8443` edge `0.086` maxDD `-6.1688`
- `news_risk_high->metal_24h` score `0.7525` n `50` status `ready` deltaP `17.8276` edge `0.1949` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7484` n `50` status `ready` deltaP `18.6946` edge `0.0765` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
