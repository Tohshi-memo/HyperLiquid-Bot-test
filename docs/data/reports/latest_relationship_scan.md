# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T09:52:30.857713+00:00`
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

- `market_context_high->unknown_24h` score `2069.6831` n `78` status `ready` deltaP `3.4483` edge `172.4506` maxDD `0.0`
- `news_risk_high->equity_24h` score `57.5132` n `50` status `ready` deltaP `64.0345` edge `4.4365` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.9054` n `50` status `ready` deltaP `31.9655` edge `2.1968` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6883` n `50` status `ready` deltaP `44.7073` edge `1.039` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.13` n `78` status `ready` deltaP `43.1963` edge `1.8506` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.9149` n `78` status `ready` deltaP `25.5924` edge `1.6975` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.8341` n `50` status `ready` deltaP `55.4138` edge `0.3971` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.6838` n `50` status `ready` deltaP `18.3103` edge `1.4418` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.4094` n `50` status `ready` deltaP `49.8276` edge `0.3686` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0412` n `50` status `ready` deltaP `44.689` edge `0.1598` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.7144` n `50` status `ready` deltaP `23.5928` edge `0.2986` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4756` n `50` status `ready` deltaP `26.689` edge `0.3386` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0318` n `50` status `ready` deltaP `20.9939` edge `0.3336` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.8913` n `50` status `ready` deltaP `35.6585` edge `0.1119` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2195` n `50` status `ready` deltaP `30.1341` edge `0.1024` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2317` n `50` status `ready` deltaP `24.994` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5802` n `50` status `ready` deltaP `20.0419` edge `0.0282` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8249` n `50` status `ready` deltaP `16.994` edge `0.0904` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7827` n `50` status `ready` deltaP `18.994` edge `0.0789` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7462` n `50` status `ready` deltaP `17.8276` edge `0.1941` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
