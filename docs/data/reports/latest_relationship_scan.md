# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T09:07:26.283136+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4096`

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

- `market_context_high->unknown_24h` score `2174.0435` n `75` status `ready` deltaP `3.4483` edge `181.1473` maxDD `0.0`
- `news_risk_high->equity_24h` score `57.1694` n `50` status `ready` deltaP `63.5172` edge `4.4113` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.0688` n `50` status `ready` deltaP `32.4828` edge `2.2143` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6451` n `50` status `ready` deltaP `44.7073` edge `1.0354` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.9688` n `75` status `ready` deltaP `42.4828` edge `1.8347` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.7695` n `75` status `ready` deltaP `24.1609` edge `1.6884` maxDD `-13.3222`
- `news_risk_high->crypto_alt_24h` score `8.7825` n `50` status `ready` deltaP `18.8276` edge `1.451` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.7591` n `50` status `ready` deltaP `54.8966` edge `0.3943` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.2972` n `50` status `ready` deltaP `49.3103` edge `0.3627` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.04` n `50` status `ready` deltaP `44.689` edge `0.1597` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6352` n `50` status `ready` deltaP `23.2934` edge `0.294` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4504` n `50` status `ready` deltaP `26.689` edge `0.3365` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0282` n `50` status `ready` deltaP `20.9939` edge `0.3333` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.9325` n `50` status `ready` deltaP `35.9634` edge `0.1133` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2171` n `50` status `ready` deltaP `30.1341` edge `0.1022` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2042` n `50` status `ready` deltaP `24.6946` edge `0.0445` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5503` n `50` status `ready` deltaP `19.7425` edge `0.0277` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8124` n `50` status `ready` deltaP `16.994` edge `0.0888` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7866` n `50` status `ready` deltaP `18.994` edge `0.0794` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7236` n `50` status `ready` deltaP `17.4828` edge `0.1935` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
