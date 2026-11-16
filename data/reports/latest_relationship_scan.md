# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T07:37:28.286449+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7466`

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

- `news_risk_high->equity_24h` score `49.3901` n `50` status `ready` deltaP `52.9306` edge `3.8336` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1199` n `50` status `ready` deltaP `40.6389` edge `2.5511` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.0144` n `50` status `ready` deltaP `37.8476` edge `0.8619` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.4487` n `50` status `ready` deltaP `22.8194` edge `1.5098` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.1996` n `50` status `ready` deltaP `44.5972` edge `0.333` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1146` n `50` status `ready` deltaP `40.9722` edge `0.2364` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9588` n `50` status `ready` deltaP `44.0793` edge `0.157` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.163` n `50` status `ready` deltaP `20.3841` edge `0.3486` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0908` n `50` status `ready` deltaP `26.0793` edge `0.3106` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.8258` n `50` status `ready` deltaP `19.7006` edge `0.2505` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7268` n `50` status `ready` deltaP `34.5915` edge `0.1053` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5061` n `50` status `ready` deltaP `24.0366` edge `0.0836` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2197` n `50` status `ready` deltaP `25.1437` edge `0.0428` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2196` n `50` status `ready` deltaP `16.2994` edge `0.0231` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.987` n `50` status `ready` deltaP `18.9028` edge `0.2178` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.7889` n `50` status `ready` deltaP `19.4431` edge `0.0767` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.7647` n `50` status `ready` deltaP `17.7425` edge `0.0777` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.255` n `50` status `ready` deltaP `3.1976` edge `0.0334` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.8409` n `67` status `ready` deltaP `-2.0802` edge `-0.0006` maxDD `-1.7817`
- `market_context_high->fx_1h` score `-1.2816` n `67` status `ready` deltaP `-8.0459` edge `-0.0001` maxDD `-0.2448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
