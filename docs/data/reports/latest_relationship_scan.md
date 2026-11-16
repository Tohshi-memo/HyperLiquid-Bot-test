# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T06:22:22.782446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8956`

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

- `news_risk_high->equity_24h` score `48.8239` n `50` status `ready` deltaP `52.0625` edge `3.7922` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.1465` n `50` status `ready` deltaP `40.6389` edge `2.5545` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.8782` n `50` status `ready` deltaP `37.3902` edge `0.8536` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.2925` n `50` status `ready` deltaP `22.125` edge `1.4944` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.0738` n `50` status `ready` deltaP `43.7292` edge `0.3283` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.141` n `50` status `ready` deltaP `40.9722` edge `0.2386` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.977` n `50` status `ready` deltaP `44.2317` edge `0.1575` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1608` n `50` status `ready` deltaP `20.5366` edge `0.3474` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9349` n `50` status `ready` deltaP `20.2994` edge `0.2556` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `3.9122` n `50` status `ready` deltaP `25.3171` edge `0.3008` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.7605` n `50` status `ready` deltaP `34.7439` edge `0.1071` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.46` n `50` status `ready` deltaP `23.5793` edge `0.0828` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.27` n `50` status `ready` deltaP `25.5928` edge `0.044` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2747` n `50` status `ready` deltaP `16.8982` edge `0.0237` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9823` n `50` status `ready` deltaP `18.9028` edge `0.2172` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8606` n `50` status `ready` deltaP `20.0419` edge `0.0819` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8224` n `50` status `ready` deltaP `18.1916` edge `0.0821` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.3066` n `50` status `ready` deltaP `3.6467` edge `0.0347` maxDD `-0.3438`
- `market_context_high->crypto_alt_4h` score `-0.7041` n `64` status `ready` deltaP `4.1921` edge `0.1628` maxDD `-17.1476`
- `market_context_high->metal_1h` score `-0.8359` n `67` status `ready` deltaP `-6.1087` edge `-0.0108` maxDD `-1.7844`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
