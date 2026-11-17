# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T10:52:27.934972+00:00`
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

- `market_context_high->unknown_24h` score `1934.7275` n `82` status `ready` deltaP `3.4483` edge `161.2043` maxDD `0.0`
- `news_risk_high->equity_24h` score `57.9728` n `50` status `ready` deltaP `64.7241` edge `4.4702` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.7323` n `50` status `ready` deltaP `31.2759` edge `2.1792` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6727` n `50` status `ready` deltaP `44.7073` edge `1.0377` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.1753` n `82` status `ready` deltaP `44.0076` edge `1.851` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.0759` n `82` status `ready` deltaP `27.2792` edge `1.7069` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.9313` n `50` status `ready` deltaP `56.1034` edge `0.4006` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.5798` n `50` status `ready` deltaP `50.5172` edge `0.3782` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.5645` n `50` status `ready` deltaP `17.6207` edge `1.4311` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0364` n `50` status `ready` deltaP `44.689` edge `0.1594` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.7288` n `50` status `ready` deltaP `23.7425` edge `0.2988` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4948` n `50` status `ready` deltaP `26.689` edge `0.3402` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0318` n `50` status `ready` deltaP `20.9939` edge `0.3336` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.8501` n `50` status `ready` deltaP `35.3537` edge `0.1105` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2171` n `50` status `ready` deltaP `30.1341` edge `0.1022` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2138` n `50` status `ready` deltaP `24.8443` edge `0.0443` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5527` n `50` status `ready` deltaP `19.7425` edge `0.0279` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8256` n `50` status `ready` deltaP `16.994` edge `0.0905` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7812` n `50` status `ready` deltaP `18.994` edge `0.0787` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7751` n `50` status `ready` deltaP `18.1724` edge `0.1955` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
